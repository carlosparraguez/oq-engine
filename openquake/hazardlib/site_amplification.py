# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright (C) 2020, GEM Foundation
#
# OpenQuake is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with OpenQuake.  If not, see <http://www.gnu.org/licenses/>.

import numpy
from scipy.stats import norm
from openquake.baselib.general import group_array
from openquake.hazardlib.imt import from_string
from openquake.hazardlib.probability_map import ProbabilityCurve
from openquake.commonlib.oqvalidation import check_same_levels


# this is necessary since norm.cdf for scale=0 returns NaNs
def norm_cdf(x, a, s):
    """
    Gaussian cumulative distribution function; if s=0, returns an
    Heaviside function instead. NB: for x=a, 0.5 is returned for all s.

    >>> norm_cdf(1.2, 1, .1)
    0.9772498680518208
    >>> norm_cdf(1.2, 1, 0)
    1.0
    >>> norm_cdf(.8, 1, .1)
    0.022750131948179216
    >>> norm_cdf(.8, 1, 0)
    0.0
    >>> norm_cdf(1, 1, .1)
    0.5
    >>> norm_cdf(1, 1, 0)
    0.5
    """
    if s == 0:
        return numpy.heaviside(x - a, .5)
    else:
        return norm.cdf(x, loc=a, scale=s)


def digitize(name, values, edges):
    """
    :param name: 'period' or 'level'
    :param values: periods or levels
    :param edges: available periods or levels
    :returns: the indices of the values in the bins

    If there are V values and E edges this functions returns an array
    with V elements in the range 0 .. E - 2; for instance:

    >>> digitize('period', [0, .1, .2], [0, .05, .1, .15, .20, .25])
    array([0, 2, 4])
    """
    if max(values) > max(edges):
        raise ValueError(
            f'The {name} {max(values)} is outside the edges {edges}')
    if min(values) < min(edges):
        raise ValueError(
            f'The {name} {min(values)} is outside the edges {edges}')
    return numpy.digitize(values, edges) - 1


class Amplifier(object):
    """
    :param imtls: intensity measure types and levels DictArray M x I
    :param ampl_funcs: an ArrayWrapper containing amplification functions
    :param amplevels: levels used for the amplified curves
    :attr periods: array of M periods
    :attr midlevels: array of I-1 levels
    :attr alpha: dict code, imt-> I-1 amplification coefficients
    :attr sigma: dict code, imt-> I-1 amplification sigmas
    """
    def __init__(self, imtls, ampl_funcs, amplevels=None):
        self.imtls = imtls
        self.periods, levels = check_same_levels(imtls)
        self.amplevels = levels if amplevels is None else amplevels
        self.midlevels = numpy.diff(levels) / 2 + levels[:-1]  # mid levels
        imls = ampl_funcs.imls
        imts = [from_string(imt) for imt in ampl_funcs.dtype.names[2:]
                if not imt.startswith('sigma_')]
        m_indices = digitize(
            'period', self.periods, [imt.period for imt in imts])
        self.imtdict = {imt: str(imts[m]) for m, imt in zip(m_indices, imtls)}
        l_indices = digitize('level', self.midlevels, imls)
        L = len(l_indices)
        self.alpha = {}  # code, imt -> alphas
        self.sigma = {}  # code, imt -> sigmas
        self.ampcodes = []
        for code, arr in group_array(ampl_funcs, 'ampcode').items():
            self.ampcodes.append(code)
            for m in set(m_indices):
                im = str(imts[m])
                self.alpha[code, im] = alpha = numpy.zeros(L)
                self.sigma[code, im] = sigma = numpy.zeros(L)
                idx = 0
                for rec in arr[l_indices]:
                    alpha[idx] = rec[im]
                    try:
                        sigma[idx] = rec['sigma_' + im]
                    except ValueError:  # missing sigma
                        pass
                    idx += 1

    def amplify_one(self, ampl_code, imt, poes):
        """
        :param ampl_code: 2-letter code for the amplification function
        :param imt: an intensity measure type
        :param poes: the original PoEs
        :returns: the amplified PoEs
        """
        if ampl_code == b'' and len(self.ampcodes) == 1:
            # manage the case of a site collection with empty ampcode
            ampl_code = self.ampcodes[0]
        stored_imt = self.imtdict[imt]
        alphas = self.alpha[ampl_code, stored_imt]
        sigmas = self.sigma[ampl_code, stored_imt]
        ampl_poes = numpy.zeros_like(self.amplevels)
        for mid, prob, a, s in zip(
                self.midlevels, -numpy.diff(poes), alphas, sigmas):
            ampl_poes += (1. - norm_cdf(self.amplevels / mid, a, s)) * prob
        return ampl_poes

    def amplify(self, ampl_code, pcurves):
        """
        :param ampl_code: 2-letter code for the amplification function
        :param pcurves: a list of ProbabilityCurves containing PoEs
        :returns: amplified ProbabilityCurves
        """
        out = []
        for pcurve in pcurves:
            lst = []
            for imt in self.imtls:
                slc = self.imtls(imt)
                new = self.amplify_one(ampl_code, imt, pcurve.array[slc, 0])
                lst.append(new)
            out.append(ProbabilityCurve(numpy.concatenate(lst).reshape(-1, 1)))
        return out
