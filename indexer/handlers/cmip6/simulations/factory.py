from indexer.handlers.cmip6.simulations.models import Simulation
from indexer.handlers.cmip6.simulations.models import SimulationJSONBlob
from indexer.handlers.cmip6.simulations.models import SimulationTimeSeries
from indexer.handlers.cmip6.simulations.models import SimulationTimeSlice
from indexer.utils import io_mgr



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


    def _set_further_info_url(blob: SimulationJSONBlob, simulation: Simulation):
        """Set further info url associated with simulation."""
        simulation.further_info_url = simulation.further_info_url or blob.further_info_url


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
        )

        # Extend time series (if appropriate).
        time_series = simulation[blob.calendar]
        if not time_series[time_slice]:
            time_series.time_slices.append(time_slice)
        else:
            blob.is_duplicate_time_slice = True


    # Iterate published CDF2CIM blobs & build a simulation info wrapper.
    simulation = Simulation(institute, source_id, experiment)
    for blob in io_mgr.yield_json_blobs(
        simulation.mip_era,
        simulation.institute,
        simulation.source_id,
        simulation.experiment
        ):
        # Extend simulation info.
        for func in (
            _set_ensemble_axis,
            _set_further_info_url,
            _set_time_series,
            _set_time_slice,
        ):
            func(blob, simulation)

        # Move file to wip folder.
        io_mgr.write_json_blob(
            simulation.mip_era,
            simulation.institute,
            simulation.experiment,
            simulation.source_id,
            blob,
            )

    return simulation
