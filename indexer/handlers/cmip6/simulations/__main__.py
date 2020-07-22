import os
import pathlib

from indexer.utils import mq
from indexer.utils import vocabs



# Initialise message broker connection.
mq.initialise()

# Import simulation processing actor. 
from indexer.handlers.cmip6.simulations.actors import process_simulation

# Start jobs - one per institute / source-id / experiments combination.
for i, s, e in vocabs.yield_cmip6_simulations():
    process_simulation.send(
        i.canonical_name,
        s.canonical_name,
        e.canonical_name,
    )
