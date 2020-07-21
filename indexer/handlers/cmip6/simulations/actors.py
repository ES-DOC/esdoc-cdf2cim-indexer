import dramatiq

from indexer.handlers.cmip6.simulations.factory import get_simulation
from indexer.handlers.cmip6.simulations.models import Simulation



# Queue to which messages will be dispatched.
_QUEUE = "cmip6.simulations"


@dramatiq.actor(queue_name=_QUEUE)
def process_simulation(institute: str, source_id: str, experiment: str):
    """Process a CMIP6 simulation directory.
    
    :param institute: Canonical (pyessv) name of CMIP6 institute.
    :param source_id: Canonical (pyessv) name of CMIP6 source_id.
    :param experiment: Canonical (pyessv) name of CMIP6 experiment.

    """
    # Set simulation wrapper.
    simulation: Simulation = get_simulation(institute, source_id, experiment)

    # Write subsetted information.
    print(simulation)
    for time_series in simulation:
        print(f"\t{time_series}")
        for time_slice in time_series.time_slices:
            print(f"\t\t{time_slice}")
