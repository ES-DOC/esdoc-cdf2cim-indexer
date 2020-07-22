import enum

import dramatiq

from indexer.utils.mq.brokers import get_broker



def execute():
    """Initialises MQ broker & connects dramatiq library.

    """
    # Configure broker.
    broker = get_broker()
    
    # Configure dramatiq.
    dramatiq.set_broker(broker)
