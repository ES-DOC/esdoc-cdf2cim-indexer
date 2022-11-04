#!/bin/bash

# Import utils.
source $CDF2CIM_INDEXER_HOME/sh/utils/misc.sh

# Main entry point.
function main()
{
    # Flush partition: broker.
    _flush_partition $CDF2CIM_INDEXER_BROKER_REDIS_DB

    # Flush partition: data.
    _flush_partition $CDF2CIM_INDEXER_CACHE_REDIS_DB

    log "cache successfully flushed"
}

function _flush_partition()
{
    local REDIS_DB_IDX=${1}

    redis-cli -h $CDF2CIM_INDEXER_CACHE_REDIS_HOST \
              -p $CDF2CIM_INDEXER_CACHE_REDIS_PORT \
              -n $REDIS_DB_IDX FLUSHDB \
              > /dev/null
}

# Invoke entry point.
main
