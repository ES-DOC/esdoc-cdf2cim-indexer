#!/bin/bash

# Import utils.
source $CDF2CIM_INDEXER_HOME/sh/utils.sh

# Main entry point.
function main()
{
    log "workers :: resetting logs ..."

	rm $CDF2CIM_INDEXER_HOME/ops/logs/*.log
}

# Invoke entry point.
main
