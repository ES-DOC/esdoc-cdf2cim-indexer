import argparse
import typing

from indexer import mq
from indexer.utils import vocabs


# Define command line argument parser.
_ARGS = argparse.ArgumentParser("Executes indexation message producer.")
_ARGS.add_argument(
    "--project",
    help="A project with published simulation metadata.",
    dest="project",
    default="cmip6",
    type=str
    )


def _produce_cmip6():
    """Dispatches CMIP6 related messages to broker.

    """
    # JIT import actor.
    from indexer.handlers.cmip6.simulations.actors import process_simulation as cmip6_simulation_producer

    # For each possible simulation, invoke actor via broker.
    for i, s, e in vocabs.yield_cmip6_simulations():
        cmip6_simulation_producer.send(
            i.canonical_name,
            s.canonical_name,
            e.canonical_name,
        )
    

# Map: project <-> message producer.
_PRODUCERS: typing.Dict[str, typing.Callable] = {
    "cmip6": _produce_cmip6,
}


def _main(args: argparse.Namespace):
    """Main entry point.
    
    """
    try:
        _PRODUCERS[args.project]
    except KeyError:
        raise ValueError(f"Unsupported project: {args.project}")
    else:
        mq.initialise()
        _PRODUCERS[args.project]()


if __name__ == '__main__':
    _main(_ARGS.parse_args())
