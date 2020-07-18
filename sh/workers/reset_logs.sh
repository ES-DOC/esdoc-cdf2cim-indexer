#!/bin/bash

# Import utils.
source $CDF2CIM_INDEXER_PATH_SH/utils.sh

# Main entry point.
function main()
{
    log "workers :: resetting logs ..."

	rm $CDF2CIM_INDEXER_PATH_OPS/logs/*.log

    # TODO
}

# Invoke entry point.
main
