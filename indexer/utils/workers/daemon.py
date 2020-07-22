from indexer.utils import mq



# Initialise broker.
mq.initialise()

# Import actors.
import indexer.handlers.cmip6.simulations.actors
