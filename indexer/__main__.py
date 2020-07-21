import os
import pathlib

from indexer import mq
from indexer.utils import vocabs



# Initialise message broker connection.
mq.initialise()

# Import simulation processing actor. 
from indexer.handlers.cmip6.simulations.actors import process_simulation

# Iterate thourgh all combinations of cmip6 / institute / source-id / experiments 
# combinations where data has been published.
path_archive = pathlib.Path(os.getenv("CDF2CIM_ARCHIVE_HOME")) / "data" / "cmip6"
for i, s, e in vocabs.yield_cmip6_simulations():
    path = path_archive / i.canonical_name / s.canonical_name / e.canonical_name
    if path.exists():
        process_simulation.send(
            i.canonical_name,
            s.canonical_name,
            e.canonical_name,
        )
        break