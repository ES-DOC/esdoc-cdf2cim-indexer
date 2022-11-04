import dramatiq

from indexer.handlers.cmip6.simulations.factory import get_simulation
from indexer.handlers.cmip6.simulations.models import Simulation
from indexer.handlers.cmip6.simulations.models import SimulationTimeSeries
from indexer.handlers.cmip6.simulations.models import SimulationTimeSlice



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
    print(simulation)

    # TODO: create cim docs and write