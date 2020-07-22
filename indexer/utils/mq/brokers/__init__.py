import os

from dramatiq.broker import Broker

from indexer.utils.mq.brokers import rabbitmq
from indexer.utils.mq.brokers import redis
from indexer.utils.mq.brokers import stub
from indexer.utils import env


# Environment variables required by this module.
class EnvVars:
    # Broker type.
    TYPE = env.get_var("BROKER_TYPE", "REDIS")


# Map: Broker type -> factory.
FACTORIES = {
    "RABBIT": rabbitmq,
    "REDIS": redis,
    "STUB": stub
}


def get_broker() -> Broker:
    """Returns an MQ broker instance for integration with dramatiq framework.

    :returns: A configured message broker.

    """
    try:
        factory = FACTORIES[EnvVars.TYPE]
    except KeyError:
        raise ValueError(f"Invalid environment variable: CDF2CIM_INDEXER_BROKER_TYPE :: {EnvVars.TYPE}")

    return factory.get_broker()
