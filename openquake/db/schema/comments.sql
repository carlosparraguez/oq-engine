/*
  Documentation for the OpenQuake database schema.
  Please keep these alphabetical by table.

    Copyright (c) 2010-2011, GEM Foundation.

    OpenQuake database is made available under the Open Database License:
    http://opendatacommons.org/licenses/odbl/1.0/. Any rights in individual
    contents of the database are licensed under the Database Contents License:
    http://opendatacommons.org/licenses/dbcl/1.0/

*/



-- schemas ------------------------------------------------------
COMMENT ON SCHEMA admin IS 'Administrative data';
COMMENT ON SCHEMA eqcat IS 'Earthquake catalog';
COMMENT ON SCHEMA hzrdi IS 'Hazard input model';
COMMENT ON SCHEMA hzrdr IS 'Hazard result data';
COMMENT ON SCHEMA oqmif IS 'OpenQuake tables for interfacing with external parties';
COMMENT ON SCHEMA riski IS 'Risk input model';
COMMENT ON SCHEMA riskr IS 'Risk result data';
COMMENT ON SCHEMA uiapi IS 'Data required by the API presented to the various OpenQuake UIs';



-- admin schema tables ------------------------------------------
COMMENT ON TABLE admin.organization IS 'An organization that is utilising the OpenQuake database';


COMMENT ON TABLE admin.oq_user IS 'An OpenQuake user that is utilising the OpenQuake database';
COMMENT ON COLUMN admin.oq_user.data_is_open IS 'Whether the data owned by the user is visible to the general public.';


COMMENT ON TABLE admin.revision_info IS 'Facilitates the keeping of revision information for the OpenQuake database and/or its artefacts (schemas, tables etc.)';
COMMENT ON COLUMN admin.revision_info.artefact IS 'The name of the database artefact for which we wish to store revision information.';
COMMENT ON COLUMN admin.revision_info.revision IS 'The revision information for the associated database artefact.';
COMMENT ON COLUMN admin.revision_info.step IS 'A simple counter that will be used to facilitate schema upgrades and/or data migration.';
COMMENT ON COLUMN admin.revision_info.last_update IS 'The date/time when the revision information was last updated. Please note: this time stamp is not refreshed automatically. It is expected that schema/data migration scripts will modify this as appropriate.';



-- eqcat schema tables ------------------------------------------
COMMENT ON TABLE eqcat.catalog IS 'Table with earthquake catalog data, the magnitude(s) and the event surface is kept in separate tables.';
COMMENT ON COLUMN eqcat.catalog.depth IS 'Earthquake depth (in km)';
COMMENT ON COLUMN eqcat.catalog.event_class IS 'Either unknown (NULL) or one of: ''aftershock'', ''foreshock''.';
COMMENT ON COLUMN eqcat.catalog.magnitude_id IS 'Foreign key to the row with the magnitude data.';
COMMENT ON COLUMN eqcat.catalog.surface_id IS 'Foreign key to the row with the earthquake surface data.';
COMMENT ON COLUMN eqcat.catalog.time IS 'Earthquake date and time';


COMMENT ON TABLE eqcat.magnitude IS 'Table with earthquake magnitudes in different units of measurement. At least one magnitude value must be set.';


COMMENT ON TABLE eqcat.surface IS 'Table with earthquake surface data, basically an ellipse and a strike angle.';
COMMENT ON COLUMN eqcat.surface.semi_minor IS 'Semi-minor axis: The shortest radius of an ellipse.';
COMMENT ON COLUMN eqcat.surface.semi_major IS 'Semi-major axis: The longest radius of an ellipse.';

COMMENT ON VIEW eqcat.catalog_allfields IS 'A global catalog view, needed for geonode integration';



-- hzrdi schema tables ------------------------------------------
COMMENT ON TABLE hzrdi.complex_fault IS 'A complex (fault) geometry, in essence a sequence of fault edges. However, we only support a single fault edge at present.';
COMMENT ON COLUMN hzrdi.complex_fault.gid IS 'An alpha-numeric identifier for this complex fault geometry.';
COMMENT ON COLUMN hzrdi.complex_fault.mfd_tgr_id IS 'Foreign key to a magnitude frequency distribution (truncated Gutenberg-Richter).';
COMMENT ON COLUMN hzrdi.complex_fault.mfd_evd_id IS 'Foreign key to a magnitude frequency distribution (evenly discretized).';
COMMENT ON COLUMN hzrdi.complex_fault.fault_edge_id IS 'Foreign key to a fault edge.';
COMMENT ON COLUMN hzrdi.complex_fault.outline IS 'The outline of the fault surface, computed by using the top/bottom fault edges.';

COMMENT ON VIEW hzrdi.complex_rupture IS 'A complex rupture view, needed for opengeo server integration.';
COMMENT ON VIEW hzrdi.complex_source IS 'A complex source view, needed for opengeo server integration.';


COMMENT ON TABLE hzrdi.fault_edge IS 'Part of a complex (fault) geometry, describes the top and the bottom seismic edges.';
COMMENT ON COLUMN hzrdi.fault_edge.bottom IS 'Bottom fault edge.';
COMMENT ON COLUMN hzrdi.fault_edge.top IS 'Top fault edge.';


COMMENT ON TABLE hzrdi.focal_mechanism IS 'Holds strike, dip and rake values with the respective constraints.';


COMMENT ON TABLE hzrdi.mfd_evd IS 'Magnitude frequency distribution, evenly discretized.';
COMMENT ON COLUMN hzrdi.mfd_evd.magnitude_type IS 'Magnitude type i.e. one of:
    - body wave magnitude (Mb)
    - duration magnitude (Md)
    - local magnitude (Ml)
    - surface wave magnitude (Ms)
    - moment magnitude (Mw)';
COMMENT ON COLUMN hzrdi.mfd_evd.min_val IS 'Minimum magnitude value.';
COMMENT ON COLUMN hzrdi.mfd_evd.max_val IS 'Maximum magnitude value (will be derived/calculated for evenly discretized magnitude frequency distributions).';


COMMENT ON TABLE hzrdi.mfd_tgr IS 'Magnitude frequency distribution, truncated Gutenberg-Richter.';
COMMENT ON COLUMN hzrdi.mfd_tgr.magnitude_type IS 'Magnitude type i.e. one of:
    - body wave magnitude (Mb)
    - duration magnitude (Md)
    - local magnitude (Ml)
    - surface wave magnitude (Ms)
    - moment magnitude (Mw)';
COMMENT ON COLUMN hzrdi.mfd_tgr.min_val IS 'Minimum magnitude value.';
COMMENT ON COLUMN hzrdi.mfd_tgr.max_val IS 'Maximum magnitude value.';


COMMENT ON TABLE hzrdi.r_depth_distr IS 'Rupture depth distribution.';
COMMENT ON COLUMN hzrdi.r_depth_distr.magnitude_type IS 'Magnitude type i.e. one of:
    - body wave magnitude (Mb)
    - duration magnitude (Md)
    - local magnitude (Ml)
    - surface wave magnitude (Ms)
    - moment magnitude (Mw)';


COMMENT ON TABLE hzrdi.r_rate_mdl IS 'Rupture rate model.';


COMMENT ON TABLE hzrdi.rupture IS 'A rupture, can be based on a point or a complex or simple fault.';
COMMENT ON COLUMN hzrdi.rupture.si_type IS 'The rupture''s seismic input type: can be one of: point, complex or simple.';
COMMENT ON COLUMN hzrdi.rupture.magnitude_type IS 'Magnitude type i.e. one of:
    - body wave magnitude (Mb)
    - duration magnitude (Md)
    - local magnitude (Ml)
    - surface wave magnitude (Ms)
    - moment magnitude (Mw)';
COMMENT ON COLUMN hzrdi.rupture.tectonic_region IS 'Tectonic region type i.e. one of:
    - Active Shallow Crust (active)
    - Stable Shallow Crust (stable)
    - Subduction Interface (interface)
    - Subduction IntraSlab (intraslab)
    - Volcanic             (volcanic)';


COMMENT ON TABLE hzrdi.simple_fault IS 'A simple fault geometry.';
COMMENT ON COLUMN hzrdi.simple_fault.dip IS 'The fault''s inclination angle with respect to the plane.';
COMMENT ON COLUMN hzrdi.simple_fault.upper_depth IS 'The upper seismogenic depth.';
COMMENT ON COLUMN hzrdi.simple_fault.lower_depth IS 'The lower seismogenic depth.';
COMMENT ON COLUMN hzrdi.simple_fault.outline IS 'The outline of the fault surface, computed by using the dip and the upper/lower seismogenic depth.';

COMMENT ON VIEW hzrdi.simple_rupture IS 'A simple rupture view, needed for opengeo server integration.';
COMMENT ON VIEW hzrdi.simple_source IS 'A simple source view, needed for opengeo server integration.';


COMMENT ON TABLE hzrdi.source IS 'A seismic source, can be based on a point, area or a complex or simple fault.';
COMMENT ON COLUMN hzrdi.source.si_type IS 'The source''s seismic input type: can be one of: area, point, complex or simple.';
COMMENT ON COLUMN hzrdi.source.tectonic_region IS 'Tectonic region type i.e. one of:
    - Active Shallow Crust (active)
    - Stable Shallow Crust (stable)
    - Subduction Interface (interface)
    - Subduction IntraSlab (intraslab)
    - Volcanic             (volcanic)';



-- hzrdr schema tables ------------------------------------------
COMMENT ON TABLE hzrdr.hazard_curve IS 'Holds data for hazard curves associated with a branch label';
COMMENT ON COLUMN hzrdr.hazard_curve.output_id IS 'The foreign key to the output record that represents the corresponding hazard curve.';
COMMENT ON COLUMN hzrdr.hazard_curve.end_branch_label IS 'End branch label for this curve.';
COMMENT ON COLUMN hzrdr.hazard_curve.statistic_type IS 'Statistic type, one of:
    - Mean     (mean)
    - Median   (median)
    - Quantile (quantile)';
COMMENT ON COLUMN hzrdr.hazard_curve.quantile IS 'The quantile for quantile statistical data.';


COMMENT ON TABLE hzrdr.hazard_curve_data IS 'Holds location/POE data for hazard curves';
COMMENT ON COLUMN hzrdr.hazard_curve_data.hazard_curve_id IS 'The foreign key to the hazard curve record for this node.';
COMMENT ON COLUMN hzrdr.hazard_curve_data.poes IS 'Probabilities of exceedence.';


COMMENT ON TABLE hzrdr.gmf_data IS 'Holds data for the ground motion field';
COMMENT ON COLUMN hzrdr.gmf_data.ground_motion IS 'Ground motion for a specific site';
COMMENT ON COLUMN hzrdr.gmf_data.location IS 'Site coordinates';


COMMENT ON TABLE hzrdr.hazard_map IS 'Holds location/IML data for hazard maps';
COMMENT ON COLUMN hzrdr.hazard_map.output_id IS 'The foreign key to the hazard map record that represents the corresponding hazard map.';
COMMENT ON COLUMN hzrdr.hazard_map.poe IS 'Probability of exceedence';
COMMENT ON COLUMN hzrdr.hazard_map.statistic_type IS 'Statistic type, one of:
    - Median   (median)
    - Quantile (quantile)';
COMMENT ON COLUMN hzrdr.hazard_map.quantile IS 'The quantile for quantile statistical data.';


COMMENT ON TABLE hzrdr.hazard_map_data IS 'Holds location/IML data for hazard maps';
COMMENT ON COLUMN hzrdr.hazard_map_data.hazard_map_id IS 'The foreign key to the hazard map record that represents the corresponding hazard map.';
COMMENT ON COLUMN hzrdr.hazard_map_data.location IS 'Position in the hazard map';
COMMENT ON COLUMN hzrdr.hazard_map_data.value IS 'IML value for this location';



-- oqmif schema tables ------------------------------------------
COMMENT ON TABLE oqmif.exposure_data IS 'Per-asset risk exposure data';
COMMENT ON COLUMN oqmif.exposure_data.exposure_model_id IS 'Foreign key to the exposure model';
COMMENT ON COLUMN oqmif.exposure_data.asset_ref IS 'A unique identifier (within the exposure model) for the asset at hand';
COMMENT ON COLUMN oqmif.exposure_data.value IS 'The value of the asset at hand';
COMMENT ON COLUMN oqmif.exposure_data.vulnerability_function_id IS 'A reference to the vulnerability function that should be used for the asset at hand';
COMMENT ON COLUMN oqmif.exposure_data.structure_type IS 'An optional structure type for the asset at hand';
COMMENT ON COLUMN oqmif.exposure_data.retrofitting_cost IS 'An optional cost of retrofitting for the asset at hand';
COMMENT ON COLUMN oqmif.exposure_data.last_update IS 'Date/time of the last change of the exposure data for the asset at hand';


COMMENT ON TABLE oqmif.exposure_model IS 'A risk exposure model';
COMMENT ON COLUMN oqmif.exposure_model.owner_id IS 'The foreign key to the user who owns the exposure model in question';
COMMENT ON COLUMN oqmif.exposure_model.name IS 'The exposure model name';
COMMENT ON COLUMN oqmif.exposure_model.description IS 'An optional description of the risk exposure model at hand';
COMMENT ON COLUMN oqmif.exposure_model.category IS 'The risk category modelled';
COMMENT ON COLUMN oqmif.exposure_model.unit IS 'The unit of measurement for the exposure data in the model at hand';
COMMENT ON COLUMN oqmif.exposure_model.last_update IS 'Date/time of the last change of the model at hand';



-- riski schema tables ------------------------------------------
COMMENT ON TABLE riski.vulnerability_function IS 'A risk vulnerability function';
COMMENT ON COLUMN riski.vulnerability_function.vulnerability_model_id IS 'A reference to the vulnerability model this function belongs to';
COMMENT ON COLUMN riski.vulnerability_function.vf_ref IS 'The vulnerability function reference, unique within the vulnerability model.';
COMMENT ON COLUMN riski.vulnerability_function.loss_ratios IS 'Loss ratio values, one per IML value in the vulnerability model.';
COMMENT ON COLUMN riski.vulnerability_function.covs IS 'Coefficient of variation values, one per IML value in the vulnerability model.';
COMMENT ON COLUMN riski.vulnerability_function.last_update IS 'Date/time of the last change of the data at hand';


COMMENT ON TABLE riski.vulnerability_model IS 'A risk vulnerability model';
COMMENT ON COLUMN riski.vulnerability_model.description IS 'An optional description of the risk vulnerability model at hand';
COMMENT ON COLUMN riski.vulnerability_model.category IS 'The risk category modelled';
COMMENT ON COLUMN riski.vulnerability_model.last_update IS 'Date/time of the last change of the model at hand';



-- riskr schema tables ------------------------------------------
COMMENT ON TABLE riskr.loss_map IS 'Holds metadata for loss maps.';
COMMENT ON COLUMN riskr.loss_map.output_id IS 'The foreign key to the output record that represents the corresponding loss map.';
COMMENT ON COLUMN riskr.loss_map.deterministic IS 'Is the loss map result of deterministic calculations (deterministic event-based) or not (classical psha-based or probabilistic based)';
COMMENT ON COLUMN riskr.loss_map.loss_map_ref IS 'A simple identifier';
COMMENT ON COLUMN riskr.loss_map.end_branch_label IS 'End branch label';
COMMENT ON COLUMN riskr.loss_map.category IS 'Loss category (e.g. economic_loss).';
COMMENT ON COLUMN riskr.loss_map.unit IS 'Unit of measurement';
COMMENT ON COLUMN riskr.loss_map.poe IS 'Probability of exceedance (for probabilistic loss maps)';


COMMENT ON TABLE riskr.loss_map_data IS 'Holds an asset, its position and a value plus (for non-deterministic maps) the standard deviation for its loss.';
COMMENT ON COLUMN riskr.loss_map_data.loss_map_id IS 'The foreign key to the loss map';
COMMENT ON COLUMN riskr.loss_map_data.asset_ref IS 'The asset reference';
COMMENT ON COLUMN riskr.loss_map_data.location IS 'The position of the asset';
COMMENT ON COLUMN riskr.loss_map_data.value IS 'The value of the loss';
COMMENT ON COLUMN riskr.loss_map_data.std_dev IS 'The standard deviation of the loss (for deterministic maps, for non-deterministic maps the standard deviation is 0)';


COMMENT ON TABLE riskr.loss_curve IS 'Holds the parameters common to a set of loss curves.';
COMMENT ON COLUMN riskr.loss_curve.output_id IS 'The foreign key to the output record that represents the corresponding loss curve.';
COMMENT ON COLUMN riskr.loss_curve.aggregate IS 'Is the curve an aggregate curve?';
COMMENT ON COLUMN riskr.loss_curve.end_branch_label IS 'End branch label';
COMMENT ON COLUMN riskr.loss_curve.category IS 'The category of the losses';
COMMENT ON COLUMN riskr.loss_curve.unit IS 'Unit for the losses (e.g. currency)';


COMMENT ON TABLE riskr.loss_curve_data IS 'Holds the probabilities of exceedance for a given loss curve.';
COMMENT ON COLUMN riskr.loss_curve_data.loss_curve_id IS 'The foreign key to the curve record to which the loss curve data belongs';
COMMENT ON COLUMN riskr.loss_curve_data.asset_ref IS 'The asset id';
COMMENT ON COLUMN riskr.loss_curve_data.location IS 'The position of the asset';
COMMENT ON COLUMN riskr.loss_curve_data.losses IS 'Losses';
COMMENT ON COLUMN riskr.loss_curve_data.poes IS 'Probabilities of exceedence';


COMMENT ON TABLE riskr.aggregate_loss_curve_data IS 'Holds the probabilities of exceedance for the whole exposure model.';
COMMENT ON COLUMN riskr.aggregate_loss_curve_data.loss_curve_id IS 'The foreign key to the curve record to which the loss curve data belongs';
COMMENT ON COLUMN riskr.aggregate_loss_curve_data.losses IS 'Losses';
COMMENT ON COLUMN riskr.aggregate_loss_curve_data.poes IS 'Probabilities of exceedence';

COMMENT ON TABLE riskr.collapse_map IS 'Holds metadata for the collapse map';
COMMENT ON COLUMN riskr.collapse_map.output_id IS 'The foreign key to the output record that represents the corresponding collapse map.';
COMMENT ON COLUMN riskr.collapse_map.exposure_model_id IS 'The foreign key to the exposure model for this collapse map.';

COMMENT ON TABLE riskr.collapse_map_data IS 'Holds the actual data for the collapse map';
COMMENT ON COLUMN riskr.collapse_map_data.collapse_map_id IS 'The foreign key to the map record to which the collapse map data belongs';
COMMENT ON COLUMN riskr.collapse_map_data.asset_ref IS 'The asset id';
COMMENT ON COLUMN riskr.collapse_map_data.value IS 'The collapse amount';
COMMENT ON COLUMN riskr.collapse_map_data.std_dev IS 'The standard deviation of the collapse amount';

-- uiapi schema tables ------------------------------------------
COMMENT ON TABLE uiapi.input IS 'A single OpenQuake input file uploaded by the user';
COMMENT ON COLUMN uiapi.input.input_type IS 'Input file type, one of:
    - source model file (source)
    - source logic tree (lt_source)
    - GMPE logic tree (lt_gmpe)
    - exposure file (exposure)
    - vulnerability file (vulnerability)';
COMMENT ON COLUMN uiapi.input.path IS 'The full path of the input file on the server';
COMMENT ON COLUMN uiapi.input.size IS 'Number of bytes in file';


COMMENT ON TABLE uiapi.oq_job IS 'Date related to an OpenQuake job that was created in the UI.';
COMMENT ON COLUMN uiapi.oq_job.description IS 'A description of the OpenQuake job, allows users to browse jobs and their inputs/outputs at a later point.';
COMMENT ON COLUMN uiapi.oq_job.job_pid IS 'The process id (PID) of the OpenQuake engine runner process';
COMMENT ON COLUMN uiapi.oq_job.supervisor_pid IS 'The process id (PID) of the supervisor for this OpenQuake job';
COMMENT ON COLUMN uiapi.oq_job.job_type IS 'One of: classical, event_based or deterministic.';
COMMENT ON COLUMN uiapi.oq_job.status IS 'One of: pending, running, failed or succeeded.';
COMMENT ON COLUMN uiapi.oq_job.duration IS 'The job''s duration in seconds (only available once the jobs terminates).';


COMMENT ON TABLE uiapi.oq_params IS 'Holds the parameters needed to invoke the OpenQuake engine.';
COMMENT ON COLUMN uiapi.oq_params.job_type IS 'One of: classical, event_based or deterministic.';
COMMENT ON COLUMN uiapi.oq_params.histories IS 'Number of seismicity histories';
COMMENT ON COLUMN uiapi.oq_params.imls IS 'Intensity measure levels';
COMMENT ON COLUMN uiapi.oq_params.imt IS 'Intensity measure type, one of:
    - peak ground acceleration (pga)
    - spectral acceleration (sa)
    - peak ground velocity (pgv)
    - peak ground displacement (pgd)';
COMMENT ON COLUMN uiapi.oq_params.poes IS 'Probabilities of exceedence';


COMMENT ON TABLE uiapi.output IS 'A single OpenQuake calculation engine output. The data may reside in a file or in the database.';
COMMENT ON COLUMN uiapi.output.db_backed IS 'True if the output''s data resides in the database and not in a file.';
COMMENT ON COLUMN uiapi.output.display_name IS 'The GUI display name to be used for this output.';
COMMENT ON COLUMN uiapi.output.path IS 'The full path of the output file on the server (optional).';
COMMENT ON COLUMN uiapi.output.output_type IS 'Output type, one of:
    - unknown
    - hazard_curve
    - hazard_map
    - gmf
    - loss_curve
    - loss_map
    - collapse_map
    - bcr_distribution';
COMMENT ON COLUMN uiapi.output.shapefile_path IS 'The full path of the shapefile generated for a hazard or loss map (optional).';


COMMENT ON TABLE uiapi.upload IS 'A batch of OpenQuake input files uploaded by the user';
COMMENT ON COLUMN uiapi.upload.job_pid IS 'The process id (PID) of the NRML loader process';
COMMENT ON COLUMN uiapi.upload.path IS 'The directory where the input files belonging to a batch live on the server';
COMMENT ON COLUMN uiapi.upload.status IS 'One of: pending, running, failed or succeeded.';


-- uiapi.error_msg
COMMENT ON TABLE uiapi.error_msg IS 'A place to store error information in the case of a job failure.';
COMMENT ON COLUMN uiapi.error_msg.brief IS 'Summary of the error message.';
COMMENT ON COLUMN uiapi.error_msg.detailed IS 'The full error message.';
