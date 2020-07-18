#!/bin/bash

# Import utils.
source $CDF2CIM_INDEXER_PATH_SH/utils.sh

# Main entry point.
function main()
{
	source $CDF2CIM_INDEXER_PATH_SH/workers/stop.sh
	source $CDF2CIM_INDEXER_PATH_SH/workers/start.sh
}

# Invoke entry point.
main
