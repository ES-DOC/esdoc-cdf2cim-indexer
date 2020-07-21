from indexer.handlers.cmip6.simulations.models import Simulation
from indexer.handlers.cmip6.simulations.models import SimulationJSONBlob
from indexer.handlers.cmip6.simulations.models import SimulationTimeSeries
from indexer.handlers.cmip6.simulations.models import SimulationTimeSlice
from indexer.utils import io_mgr
from indexer.utils import logger



def get_simulation(institute: str, source_id: str, experiment: str) -> Simulation:
    """Gets simulation information derived from a CDF2CIM publication folder.

    :param institute: Canonical (pyessv) name of CMIP6 institute.
    :param source_id: Canonical (pyessv) name of CMIP6 source_id.
    :param experiment: Canonical (pyessv) name of CMIP6 experiment.

    :returns: Simulation information wrapper.

    """
    def _set_ensemble_axis(blob: SimulationJSONBlob, simulation: Simulation):
        """Set ensemble axis info associated with simulation."""
        simulation.ripf = simulation.ripf or blob.ripf
        simulation.ripf_parent = simulation.ripf or blob.ripf_parent


    def _set_time_series(blob: SimulationJSONBlob, simulation: Simulation):
        """Set time series info associated with simulation."""
        # JIT instantiate.
        if not simulation[blob.calendar]:
            simulation.time_series.append(
                SimulationTimeSeries(blob.calendar, blob.range)
                )

        # Extend time series range (if appropriate).
        time_series = simulation[blob.calendar]
        if blob.range.start < time_series.range.start:
            time_series.range.start = blob.range.start
        if blob.range.end > time_series.range.end:
            time_series.range.end = blob.range.end


    def _set_time_slice(blob: SimulationJSONBlob, simulation: Simulation):
        """Set time slice info associated with simulation."""
        # Instantiate.
        time_slice = SimulationTimeSlice(
            calendar=blob.calendar,
            range=blob.range,
            range_of_branch=blob.range_of_branch,
        )

        # Extend time series (if appropriate).
        time_series = simulation[blob.calendar]
        if not time_series[time_slice]:
            time_series.time_slices.append(time_slice)
        else:
            logger.log_warning(f"Duplicate time slice detected: {time_slice}")


    # Iterate published CDF2CIM blobs & build a simulation info wrapper.
    simulation = Simulation(institute, source_id, experiment)
    for blob in io_mgr.yield_json_blobs(
        simulation.mip_era,
        simulation.institute,
        simulation.source_id,
        simulation.experiment
        ):
        for func in (
            _set_ensemble_axis,
            _set_time_series,
            _set_time_slice,
        ):
            func(blob, simulation)
    
    return simulation
