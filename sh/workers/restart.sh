#!/bin/bash

# Import utils.
source $CDF2CIM_INDEXER_HOME/sh/utils/misc.sh

# Main entry point.
function main()
{
	source $CDF2CIM_INDEXER_HOME/sh/workers/stop.sh
    source $CDF2CIM_INDEXER_HOME/sh/cache/flush.sh
	source $CDF2CIM_INDEXER_HOME/sh/workers/start.sh
}

# Invoke entry point.
main
