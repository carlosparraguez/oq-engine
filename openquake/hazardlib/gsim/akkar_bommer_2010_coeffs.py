# coding: utf-8
# The Hazard Library
# Copyright (C) 2012 GEM Foundation
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from openquake.hazardlib.gsim.base import CoeffsTable
from openquake.hazardlib.imt import PGA, PGV, SA

#: Coefficient table constructed from the electronic suplements of the
#: original paper.


COEFFS_FS_ROCK_SWISS01 = CoeffsTable(sa_damping=5, table="""\
    IMT       k_adj     a1              a2              b1               b2             Rm             phi_11         phi_21         C2             Mc1    Mc2    Rc11    Rc21
    pga       0.7523    1.415563E+00    1.239239E+00    9.955898E-01     -2.168473E-01  1.972259E+03   0.58           0.47           0.35           5      7      11      34
    0.0100    0.7523    1.415563E+00    1.239239E+00    9.955898E-01     -2.168473E-01  1.972259E+03   0.58           0.47           0.35           5      7      11      34
    0.0200    0.7688    1.258943E+00    1.000000E+00    9.946932E-01     -2.457967E-01  1.144296E+03   0.5679588      0.4609691      0.3740824      5      7      11      34
    0.0300    0.8013    1.278509E+00    1.000000E+00    9.964649E-01     -2.377669E-01  1.322173E+03   0.56091515     0.455686362    0.3881697      5      7      11      34
    0.0400    0.7889    1.277566E+00    1.042382E+00    9.964251E-01     -2.773620E-01  8.688695E+02   0.5559176      0.4519382      0.398164799    5      7      11      34
    0.0500    0.7578    1.276418E+00    1.077745E+00    9.963578E-01     -3.093462E-01  5.009880E+02   0.5520412      0.4490309      0.4059176      5      7      11      34
    0.1000    0.7253    1.433038E+00    1.222753E+00    9.963723E-01     -4.006431E-01  2.404867E+02   0.54           0.44           0.43           5      7      11      34
    0.1500    0.7257    1.384642E+00    1.250938E+00    9.964175E-01     -3.190415E-01  6.310597E+02   0.580947375    0.47509775     0.400751875    5      7      11      34
    0.2000    0.7261    1.350304E+00    1.271328E+00    9.964495E-01     -2.611442E-01  9.081757E+02   0.61           0.5            0.38           5      7      11      34
    0.2500    0.7302    1.517877E+00    1.262536E+00    9.968063E-01     -2.750184E-01  7.664586E+02   0.626510191    0.5            0.374496603    5      7      11      34
    0.3000    0.7376    1.654794E+00    1.255398E+00    9.970978E-01     -2.863545E-01  6.506672E+02   0.64           0.5            0.37           5      7      11      34
    0.3500    0.7447    1.855761E+00    1.322266E+00    9.964436E-01     -3.280135E-01  4.672187E+02   0.627929292    0.493964646    0.37           5      7      11      34
    0.4000    0.7507    2.030328E+00    1.383505E+00    9.958719E-01     -3.642816E-01  3.078242E+02   0.617473168    0.488736584    0.37           5      7      11      34
    1.0000    0.7916    -5.169560E+00   1.000000E+00    1.010650E+00     6.221898E-01   1.000000E+09   0.54           0.45           0.4            5      7      11      34
    1.0500    0.7908    -6.821261E+00   1.000000E+00    1.016859E+00     8.337131E-01   1.000000E+09   0.539555893    0.447779464    0.4            5      7      11      34
    1.1000    0.7912    -8.396109E+00   1.000000E+00    1.022780E+00     1.035395E+00   1.000000E+09   0.539132449    0.445662247    0.4            5      7      11      34
    1.1500    0.7920    -9.900941E+00   1.000000E+00    1.028437E+00     1.228109E+00   1.000000E+09   0.538727832    0.44363916     0.4            5      7      11      34
    1.2000    0.7927    -1.134172E+01   1.000000E+00    1.033854E+00     1.412621E+00   1.000000E+09   0.538340438    0.441702188    0.4            5      7      11      34
    1.2500    0.7932    -1.272367E+01   1.000000E+00    1.039049E+00     1.589599E+00   1.000000E+09   0.53796886     0.439844299    0.4            5      7      11      34
    1.3000    0.7933    -1.405141E+01   1.000000E+00    1.044041E+00     1.759635E+00   1.000000E+09   0.537611858    0.438059288    0.4            5      7      11      34
    1.3500    0.7933    -1.532904E+01   1.000000E+00    1.048844E+00     1.923254E+00   1.000000E+09   0.53726833     0.436341651    0.4            5      7      11      34
    1.4000    0.7933    -1.656020E+01   1.000000E+00    1.053472E+00     2.080921E+00   1.000000E+09   0.536937298    0.434686489    0.4            5      7      11      34
    1.4500    0.7933    -1.774815E+01   1.000000E+00    1.057938E+00     2.233055E+00   1.000000E+09   0.536617883    0.433089414    0.4            5      7      11      34
    1.5000    0.7930    -1.889583E+01   1.000000E+00    1.062253E+00     2.380030E+00   1.000000E+09   0.536309298    0.431546488    0.4            5      7      11      34
    1.5500    0.7927    -2.000587E+01   1.000000E+00    1.066426E+00     2.522186E+00   1.000000E+09   0.536010832    0.430054159    0.4            5      7      11      34
    1.6000    0.7961    -2.108066E+01   1.000000E+00    1.070467E+00     2.659828E+00   1.000000E+09   0.535721843    0.428609213    0.4            5      7      11      34
    1.6500    0.7980    -2.212238E+01   1.000000E+00    1.074383E+00     2.793235E+00   1.000000E+09   0.535441747    0.427208734    0.4            5      7      11      34
    1.7000    0.7943    -2.313299E+01   1.000000E+00    1.078182E+00     2.922658E+00   1.000000E+09   0.535170014    0.425850068    0.4            5      7      11      34
    1.7500    0.7914    -2.411431E+01   1.000000E+00    1.081872E+00     3.048330E+00   1.000000E+09   0.534906158    0.424530788    0.4            5      7      11      34
    1.8000    0.7936    -2.506799E+01   1.000000E+00    1.085457E+00     3.170461E+00   1.000000E+09   0.534649735    0.423248676    0.4            5      7      11      34
    1.8500    0.7957    -2.599553E+01   1.000000E+00    1.088944E+00     3.289246E+00   1.000000E+09   0.534400339    0.422001695    0.4            5      7      11      34
    1.9000    0.7987    -2.689833E+01   1.000000E+00    1.092338E+00     3.404863E+00   1.000000E+09   0.534157594    0.420787971    0.4            5      7      11      34
    1.9500    0.8021    -2.777768E+01   1.000000E+00    1.095644E+00     3.517476E+00   1.000000E+09   0.533921155    0.419605775    0.4            5      7      11      34
    2.0000    0.8024    -2.863477E+01   1.000000E+00    1.098866E+00     3.627238E+00   1.000000E+09   0.533690702    0.418453512    0.4            5      7      11      34
    2.0500    0.8025    -2.863477E+01   1.000000E+00    1.098866E+00     3.627238E+00   1.000000E+09   0.533465941    0.417329703    0.4            5      7      11      34
    2.1000    0.8027    -2.863477E+01   1.000000E+00    1.098866E+00     3.627238E+00   1.000000E+09   0.533246595    0.416232976    0.4            5      7      11      34
    2.1500    0.8027    -2.863477E+01   1.000000E+00    1.098866E+00     3.627238E+00   1.000000E+09   0.533032411    0.415162057    0.4            5      7      11      34
    2.2000    0.8014    -2.863477E+01   1.000000E+00    1.098866E+00     3.627238E+00   1.000000E+09   0.532823152    0.414115759    0.4            5      7      11      34
    2.2500    0.8016    -2.863477E+01   1.000000E+00    1.098866E+00     3.627238E+00   1.000000E+09   0.532618595    0.413092975    0.4            5      7      11      34
    2.3000    0.8019    -2.863477E+01   1.000000E+00    1.098866E+00     3.627238E+00   1.000000E+09   0.532418534    0.412092672    0.4            5      7      11      34
    2.3500    0.8022    -2.863477E+01   1.000000E+00    1.098866E+00     3.627238E+00   1.000000E+09   0.532222777    0.411113883    0.4            5      7      11      34
    2.4000    0.8029    -2.863477E+01   1.000000E+00    1.098866E+00     3.627238E+00   1.000000E+09   0.53203114     0.410155701    0.4            5      7      11      34
    2.4500    0.8048    -2.863477E+01   1.000000E+00    1.098866E+00     3.627238E+00   1.000000E+09   0.531843455    0.409217276    0.4            5      7      11      34
    2.5000    0.8069    -2.863477E+01   1.000000E+00    1.098866E+00     3.627238E+00   1.000000E+09   0.531659562    0.408297812    0.4            5      7      11      34
    2.5500    0.8089    -2.863477E+01   1.000000E+00    1.098866E+00     3.627238E+00   1.000000E+09   0.531479311    0.407396555    0.4            5      7      11      34
    2.6000    0.8109    -2.863477E+01   1.000000E+00    1.098866E+00     3.627238E+00   1.000000E+09   0.53130256     0.4065128      0.4            5      7      11      34
    2.6500    0.8129    -2.863477E+01   1.000000E+00    1.098866E+00     3.627238E+00   1.000000E+09   0.531129176    0.405645879    0.4            5      7      11      34
    2.7000    0.8123    -2.863477E+01   1.000000E+00    1.098866E+00     3.627238E+00   1.000000E+09   0.530959033    0.404795164    0.4            5      7      11      34
    2.7500    0.8113    -2.863477E+01   1.000000E+00    1.098866E+00     3.627238E+00   1.000000E+09   0.530792012    0.403960058    0.4            5      7      11      34
    2.8000    0.8104    -2.863477E+01   1.000000E+00    1.098866E+00     3.627238E+00   1.000000E+09   0.530628       0.403140001    0.4            5      7      11      34
    2.8500    0.8094    -2.863477E+01   1.000000E+00    1.098866E+00     3.627238E+00   1.000000E+09   0.530466892    0.402334458    0.4            5      7      11      34
    2.9000    0.8089    -2.863477E+01   1.000000E+00    1.098866E+00     3.627238E+00   1.000000E+09   0.530308585    0.401542926    0.4            5      7      11      34
    2.9500    0.8097    -2.863477E+01   1.000000E+00    1.098866E+00     3.627238E+00   1.000000E+09   0.530152985    0.400764925    0.4            5      7      11      34
    3.0000    0.8104    -2.863477E+01   1.000000E+00    1.098866E+00     3.627238E+00   1.000000E+09   0.53           0.4            0.4            5      7      11      34
    4.0000    0.8232    -2.863477E+01   1.000000E+00    1.098866E+00     3.627238E+00   1.000000E+09   0.53           0.4            0.4            5      7      11      34
    """)

COEFFS_FS_ROCK_SWISS04 = CoeffsTable(sa_damping=5, table="""\
    IMT       k_adj     a1              a2              b1              b2              Rm              phi_11         phi_21         C2             Mc1    Mc2    Rc11    Rc21
    pga       1.1484    1.415563E+00    1.239239E+00    9.955898E-01    -2.168473E-01   1.972259E+03    0.58           0.47           0.35           5      7      11      34
    0.0100    1.1484    1.415563E+00    1.239239E+00    9.955898E-01    -2.168473E-01   1.972259E+03    0.58           0.47           0.35           5      7      11      34
    0.0200    1.3106    1.258943E+00    1.000000E+00    9.946932E-01    -2.457967E-01   1.144296E+03    0.5679588      0.4609691      0.3740824      5      7      11      34
    0.0300    1.6316    1.278509E+00    1.000000E+00    9.964649E-01    -2.377669E-01   1.322173E+03    0.56091515     0.455686362    0.3881697      5      7      11      34
    0.0400    1.7354    1.277566E+00    1.042382E+00    9.964251E-01    -2.773620E-01   8.688695E+02    0.5559176      0.4519382      0.398164799    5      7      11      34
    0.0500    1.6836    1.276418E+00    1.077745E+00    9.963578E-01    -3.093462E-01   5.009880E+02    0.5520412      0.4490309      0.4059176      5      7      11      34
    0.1000    1.1761    1.433038E+00    1.222753E+00    9.963723E-01    -4.006431E-01   2.404867E+02    0.54           0.44           0.43           5      7      11      34
    0.1500    1.0228    1.384642E+00    1.250938E+00    9.964175E-01    -3.190415E-01   6.310597E+02    0.580947375    0.47509775     0.400751875    5      7      11      34
    0.2000    0.9450    1.350304E+00    1.271328E+00    9.964495E-01    -2.611442E-01   9.081757E+02    0.61           0.5            0.38           5      7      11      34
    0.2500    0.9044    1.517877E+00    1.262536E+00    9.968063E-01    -2.750184E-01   7.664586E+02    0.626510191    0.5            0.374496603    5      7      11      34
    0.3000    0.8829    1.654794E+00    1.255398E+00    9.970978E-01    -2.863545E-01   6.506672E+02    0.64           0.5            0.37           5      7      11      34
    0.3500    0.8696    1.855761E+00    1.322266E+00    9.964436E-01    -3.280135E-01   4.672187E+02    0.627929292    0.493964646    0.37           5      7      11      34
    0.4000    0.8603    2.030328E+00    1.383505E+00    9.958719E-01    -3.642816E-01   3.078242E+02    0.617473168    0.488736584    0.37           5      7      11      34
    1.0000    0.8376    -5.169560E+00   1.000000E+00    1.010650E+00    6.221898E-01    1.000000E+09    0.54           0.45           0.4            5      7      11      34
    1.0500    0.8345    -6.821261E+00   1.000000E+00    1.016859E+00    8.337131E-01    1.000000E+09    0.539555893    0.447779464    0.4            5      7      11      34
    1.1000    0.8329    -8.396109E+00   1.000000E+00    1.022780E+00    1.035395E+00    1.000000E+09    0.539132449    0.445662247    0.4            5      7      11      34
    1.1500    0.8320    -9.900941E+00   1.000000E+00    1.028437E+00    1.228109E+00    1.000000E+09    0.538727832    0.44363916     0.4            5      7      11      34
    1.2000    0.8311    -1.134172E+01   1.000000E+00    1.033854E+00    1.412621E+00    1.000000E+09    0.538340438    0.441702188    0.4            5      7      11      34
    1.2500    0.8299    -1.272367E+01   1.000000E+00    1.039049E+00    1.589599E+00    1.000000E+09    0.53796886     0.439844299    0.4            5      7      11      34
    1.3000    0.8286    -1.405141E+01   1.000000E+00    1.044041E+00    1.759635E+00    1.000000E+09    0.537611858    0.438059288    0.4            5      7      11      34
    1.3500    0.8273    -1.532904E+01   1.000000E+00    1.048844E+00    1.923254E+00    1.000000E+09    0.53726833     0.436341651    0.4            5      7      11      34
    1.4000    0.8260    -1.656020E+01   1.000000E+00    1.053472E+00    2.080921E+00    1.000000E+09    0.536937298    0.434686489    0.4            5      7      11      34
    1.4500    0.8249    -1.774815E+01   1.000000E+00    1.057938E+00    2.233055E+00    1.000000E+09    0.536617883    0.433089414    0.4            5      7      11      34
    1.5000    0.8235    -1.889583E+01   1.000000E+00    1.062253E+00    2.380030E+00    1.000000E+09    0.536309298    0.431546488    0.4            5      7      11      34
    1.5500    0.8222    -2.000587E+01   1.000000E+00    1.066426E+00    2.522186E+00    1.000000E+09    0.536010832    0.430054159    0.4            5      7      11      34
    1.6000    0.8247    -2.108066E+01   1.000000E+00    1.070467E+00    2.659828E+00    1.000000E+09    0.535721843    0.428609213    0.4            5      7      11      34
    1.6500    0.8257    -2.212238E+01   1.000000E+00    1.074383E+00    2.793235E+00    1.000000E+09    0.535441747    0.427208734    0.4            5      7      11      34
    1.7000    0.8209    -2.313299E+01   1.000000E+00    1.078182E+00    2.922658E+00    1.000000E+09    0.535170014    0.425850068    0.4            5      7      11      34
    1.7500    0.8170    -2.411431E+01   1.000000E+00    1.081872E+00    3.048330E+00    1.000000E+09    0.534906158    0.424530788    0.4            5      7      11      34
    1.8000    0.8185    -2.506799E+01   1.000000E+00    1.085457E+00    3.170461E+00    1.000000E+09    0.534649735    0.423248676    0.4            5      7      11      34
    1.8500    0.8199    -2.599553E+01   1.000000E+00    1.088944E+00    3.289246E+00    1.000000E+09    0.534400339    0.422001695    0.4            5      7      11      34
    1.9000    0.8222    -2.689833E+01   1.000000E+00    1.092338E+00    3.404863E+00    1.000000E+09    0.534157594    0.420787971    0.4            5      7      11      34
    1.9500    0.8250    -2.777768E+01   1.000000E+00    1.095644E+00    3.517476E+00    1.000000E+09    0.533921155    0.419605775    0.4            5      7      11      34
    2.0000    0.8246    -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09    0.533690702    0.418453512    0.4            5      7      11      34
    2.0500    0.8242    -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09    0.533465941    0.417329703    0.4            5      7      11      34
    2.1000    0.8237    -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09    0.533246595    0.416232976    0.4            5      7      11      34
    2.1500    0.8232    -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09    0.533032411    0.415162057    0.4            5      7      11      34
    2.2000    0.8213    -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09    0.532823152    0.414115759    0.4            5      7      11      34
    2.2500    0.8211    -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09    0.532618595    0.413092975    0.4            5      7      11      34
    2.3000    0.8209    -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09    0.532418534    0.412092672    0.4            5      7      11      34
    2.3500    0.8207    -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09    0.532222777    0.411113883    0.4            5      7      11      34
    2.4000    0.8210    -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09    0.53203114     0.410155701    0.4            5      7      11      34
    2.4500    0.8226    -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09    0.531843455    0.409217276    0.4            5      7      11      34
    2.5000    0.8243    -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09    0.531659562    0.408297812    0.4            5      7      11      34
    2.5500    0.8260    -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09    0.531479311    0.407396555    0.4            5      7      11      34
    2.6000    0.8277    -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09    0.53130256     0.4065128      0.4            5      7      11      34
    2.6500    0.8293    -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09    0.531129176    0.405645879    0.4            5      7      11      34
    2.7000    0.8284    -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09    0.530959033    0.404795164    0.4            5      7      11      34
    2.7500    0.8272    -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09    0.530792012    0.403960058    0.4            5      7      11      34
    2.8000    0.8260    -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09    0.530628       0.403140001    0.4            5      7      11      34
    2.8500    0.8248    -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09    0.530466892    0.402334458    0.4            5      7      11      34
    2.9000    0.8241    -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09    0.530308585    0.401542926    0.4            5      7      11      34
    2.9500    0.8245    -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09    0.530152985    0.400764925    0.4            5      7      11      34
    3.0000    0.8250    -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09    0.53           0.4            0.4            5      7      11      34
    4.0000    0.8327    -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09    0.53           0.4            0.4            5      7      11      34
    """)

COEFFS_FS_ROCK_SWISS08 = CoeffsTable(sa_damping=5, table="""\
    IMT       k_adj      a1              a2              b1              b2              Rm             phi_11         phi_21         C2             Mc1    Mc2    Rc11    Rc21
    pga       1.3317     1.415563E+00    1.239239E+00    9.955898E-01    -2.168473E-01   1.972259E+03   0.58           0.47           0.35           5      7      11      34
    0.0100    1.3317     1.415563E+00    1.239239E+00    9.955898E-01    -2.168473E-01   1.972259E+03   0.58           0.47           0.35           5      7      11      34
    0.0200    1.6468     1.258943E+00    1.000000E+00    9.946932E-01    -2.457967E-01   1.144296E+03   0.5679588      0.4609691      0.3740824      5      7      11      34
    0.0300    2.1531     1.278509E+00    1.000000E+00    9.964649E-01    -2.377669E-01   1.322173E+03   0.56091515     0.455686362    0.3881697      5      7      11      34
    0.0400    2.2478     1.277566E+00    1.042382E+00    9.964251E-01    -2.773620E-01   8.688695E+02   0.5559176      0.4519382      0.398164799    5      7      11      34
    0.0500    2.1259     1.276418E+00    1.077745E+00    9.963578E-01    -3.093462E-01   5.009880E+02   0.5520412      0.4490309      0.4059176      5      7      11      34
    0.1000    1.3473     1.433038E+00    1.222753E+00    9.963723E-01    -4.006431E-01   2.404867E+02   0.54           0.44           0.43           5      7      11      34
    0.1500    1.1173     1.384642E+00    1.250938E+00    9.964175E-01    -3.190415E-01   6.310597E+02   0.580947375    0.47509775     0.400751875    5      7      11      34
    0.2000    1.0026     1.350304E+00    1.271328E+00    9.964495E-01    -2.611442E-01   9.081757E+02   0.61           0.5            0.38           5      7      11      34
    0.2500    0.9407     1.517877E+00    1.262536E+00    9.968063E-01    -2.750184E-01   7.664586E+02   0.626510191    0.5            0.374496603    5      7      11      34
    0.3000    0.9039     1.654794E+00    1.255398E+00    9.970978E-01    -2.863545E-01   6.506672E+02   0.64           0.5            0.37           5      7      11      34
    0.3500    0.8790     1.855761E+00    1.322266E+00    9.964436E-01    -3.280135E-01   4.672187E+02   0.627929292    0.493964646    0.37           5      7      11      34
    0.4000    0.8608     2.030328E+00    1.383505E+00    9.958719E-01    -3.642816E-01   3.078242E+02   0.617473168    0.488736584    0.37           5      7      11      34
    1.0000    0.8312     -5.169560E+00   1.000000E+00    1.010650E+00    6.221898E-01    1.000000E+09   0.54           0.45           0.4            5      7      11      34
    1.0500    0.8317     -6.821261E+00   1.000000E+00    1.016859E+00    8.337131E-01    1.000000E+09   0.539555893    0.447779464    0.4            5      7      11      34
    1.1000    0.8341     -8.396109E+00   1.000000E+00    1.022780E+00    1.035395E+00    1.000000E+09   0.539132449    0.445662247    0.4            5      7      11      34
    1.1500    0.8369     -9.900941E+00   1.000000E+00    1.028437E+00    1.228109E+00    1.000000E+09   0.538727832    0.44363916     0.4            5      7      11      34
    1.2000    0.8400     -1.134172E+01   1.000000E+00    1.033854E+00    1.412621E+00    1.000000E+09   0.538340438    0.441702188    0.4            5      7      11      34
    1.2500    0.8427     -1.272367E+01   1.000000E+00    1.039049E+00    1.589599E+00    1.000000E+09   0.53796886     0.439844299    0.4            5      7      11      34
    1.3000    0.8451     -1.405141E+01   1.000000E+00    1.044041E+00    1.759635E+00    1.000000E+09   0.537611858    0.438059288    0.4            5      7      11      34
    1.3500    0.8474     -1.532904E+01   1.000000E+00    1.048844E+00    1.923254E+00    1.000000E+09   0.53726833     0.436341651    0.4            5      7      11      34
    1.4000    0.8497     -1.656020E+01   1.000000E+00    1.053472E+00    2.080921E+00    1.000000E+09   0.536937298    0.434686489    0.4            5      7      11      34
    1.4500    0.8520     -1.774815E+01   1.000000E+00    1.057938E+00    2.233055E+00    1.000000E+09   0.536617883    0.433089414    0.4            5      7      11      34
    1.5000    0.8538     -1.889583E+01   1.000000E+00    1.062253E+00    2.380030E+00    1.000000E+09   0.536309298    0.431546488    0.4            5      7      11      34
    1.5500    0.8556     -2.000587E+01   1.000000E+00    1.066426E+00    2.522186E+00    1.000000E+09   0.536010832    0.430054159    0.4            5      7      11      34
    1.6000    0.8613     -2.108066E+01   1.000000E+00    1.070467E+00    2.659828E+00    1.000000E+09   0.535721843    0.428609213    0.4            5      7      11      34
    1.6500    0.8652     -2.212238E+01   1.000000E+00    1.074383E+00    2.793235E+00    1.000000E+09   0.535441747    0.427208734    0.4            5      7      11      34
    1.7000    0.8630     -2.313299E+01   1.000000E+00    1.078182E+00    2.922658E+00    1.000000E+09   0.535170014    0.425850068    0.4            5      7      11      34
    1.7500    0.8615     -2.411431E+01   1.000000E+00    1.081872E+00    3.048330E+00    1.000000E+09   0.534906158    0.424530788    0.4            5      7      11      34
    1.8000    0.8653     -2.506799E+01   1.000000E+00    1.085457E+00    3.170461E+00    1.000000E+09   0.534649735    0.423248676    0.4            5      7      11      34
    1.8500    0.8691     -2.599553E+01   1.000000E+00    1.088944E+00    3.289246E+00    1.000000E+09   0.534400339    0.422001695    0.4            5      7      11      34
    1.9000    0.8736     -2.689833E+01   1.000000E+00    1.092338E+00    3.404863E+00    1.000000E+09   0.534157594    0.420787971    0.4            5      7      11      34
    1.9500    0.8786     -2.777768E+01   1.000000E+00    1.095644E+00    3.517476E+00    1.000000E+09   0.533921155    0.419605775    0.4            5      7      11      34
    2.0000    0.8799     -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09   0.533690702    0.418453512    0.4            5      7      11      34
    2.0500    0.8810     -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09   0.533465941    0.417329703    0.4            5      7      11      34
    2.1000    0.8820     -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09   0.533246595    0.416232976    0.4            5      7      11      34
    2.1500    0.8830     -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09   0.533032411    0.415162057    0.4            5      7      11      34
    2.2000    0.8821     -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09   0.532823152    0.414115759    0.4            5      7      11      34
    2.2500    0.8829     -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09   0.532618595    0.413092975    0.4            5      7      11      34
    2.3000    0.8838     -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09   0.532418534    0.412092672    0.4            5      7      11      34
    2.3500    0.8846     -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09   0.532222777    0.411113883    0.4            5      7      11      34
    2.4000    0.8859     -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09   0.53203114     0.410155701    0.4            5      7      11      34
    2.4500    0.8883     -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09   0.531843455    0.409217276    0.4            5      7      11      34
    2.5000    0.8909     -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09   0.531659562    0.408297812    0.4            5      7      11      34
    2.5500    0.8934     -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09   0.531479311    0.407396555    0.4            5      7      11      34
    2.6000    0.8958     -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09   0.53130256     0.4065128      0.4            5      7      11      34
    2.6500    0.8982     -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09   0.531129176    0.405645879    0.4            5      7      11      34
    2.7000    0.8977     -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09   0.530959033    0.404795164    0.4            5      7      11      34
    2.7500    0.8966     -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09   0.530792012    0.403960058    0.4            5      7      11      34
    2.8000    0.8956     -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09   0.530628       0.403140001    0.4            5      7      11      34
    2.8500    0.8946     -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09   0.530466892    0.402334458    0.4            5      7      11      34
    2.9000    0.8942     -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09   0.530308585    0.401542926    0.4            5      7      11      34
    2.9500    0.8952     -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09   0.530152985    0.400764925    0.4            5      7      11      34
    3.0000    0.8963     -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09   0.53           0.4            0.4            5      7      11      34
    4.0000    0.9146     -2.863477E+01   1.000000E+00    1.098866E+00    3.627238E+00    1.000000E+09   0.53           0.4            0.4            5      7      11      34
    """)

COEFFS_PHI_SS_MEAN = CoeffsTable(sa_damping=5, table="""\
    IMT       phi_ss
    pga       0.46
    0.01      0.46
    0.02      0.4569897
    0.03      0.455228787
    0.04      0.4539794
    0.05      0.4530103
    0.1       0.45
    0.15      0.467548875
    0.2       0.48
    0.25      0.48
    0.3       0.48
    0.35      0.473964646
    0.4       0.468736584
    0.45      0.464125107
    0.5       0.46
    0.55      0.458624965
    0.6       0.457369656
    0.65      0.456214884
    0.7       0.455145732
    0.75      0.454150375
    0.8       0.453219281
    0.85      0.452344653
    0.9       0.451520031
    0.95      0.450740006
    1         0.45
    1.05      0.448223571
    1.1       0.446529797
    1.15      0.444911328
    1.2       0.443361751
    1.25      0.441875439
    1.3       0.44044743
    1.35      0.439073321
    1.4       0.437749191
    1.45      0.436471531
    1.5       0.43523719
    1.55      0.434043327
    1.6       0.43288737
    1.65      0.431766988
    1.7       0.430680054
    1.75      0.42962463
    1.8       0.428598941
    1.85      0.427601356
    1.9       0.426630377
    1.95      0.42568462
    2         0.42476281
    2.05      0.423863762
    2.1       0.422986381
    2.15      0.422129646
    2.2       0.421292607
    2.25      0.42047438
    2.3       0.419674138
    2.35      0.418891106
    2.4       0.418124561
    2.45      0.417373821
    2.5       0.416638249
    2.55      0.415917244
    2.6       0.41521024
    2.65      0.414516703
    2.7       0.413836131
    2.75      0.413168047
    2.8       0.412512001
    2.85      0.411867567
    2.9       0.411234341
    2.95      0.41061194
    3         0.41
    4         0.41
    """)
