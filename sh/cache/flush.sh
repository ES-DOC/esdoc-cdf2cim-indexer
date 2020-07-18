#!/bin/bash

# Import utils.
source $CDF2CIM_INDEXER_PATH_SH/utils.sh

# Main entry point.
function main()
{
    # Flush partition: broker.
    source $CDF2CIM_INDEXER_PATH_SH/cache/flush_partition.sh $CDF2CIM_INDEXER_BROKER_REDIS_DB

    # Flush partition: data.
    source $CDF2CIM_INDEXER_PATH_SH/cache/flush_partition.sh $CDF2CIM_INDEXER_CACHE_REDIS_DB

    log "cache successfully flushed"
}

# Invoke entry point.
main
