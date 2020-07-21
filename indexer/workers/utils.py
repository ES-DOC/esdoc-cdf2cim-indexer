from indexer import mq



def setup_daemon():
    """Perform setup when run in daemon mode.
    
    """
    _setup()


def setup_interactive():
    """Perform setup when run in interactive mode.
    
    """
    _setup()


def _setup():
    """Perform setup tasks standard to all workers.
    
    """
    # Initialise broker.
    mq.initialise()


def start_indexation():
    """Starts indexation actors by JIT importing actors.
    
    """
    import indexer.handlers.cmip6.simulations.actors
