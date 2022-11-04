#!/bin/bash

# Import utils.
source $CDF2CIM_INDEXER_HOME/sh/utils/misc.sh

# Main entry point.
function main()
{
    # Escape if daemon is already running.
    daemon_socket=$CDF2CIM_INDEXER_HOME/ops/daemon/supervisord.sock
    if [ -e "$daemon_socket" ]; then
        log "cdf2cim indexer consumers are running in daemon mode:"
        log "- if the socket file ($daemon_socket) is stale then clear it and retry,"
        log "- otherwise stop the consumers (cdf2cim-indexer-consumers-stop) and retry."
        exit 0
    fi

    # Mock a socket file to protect against repeatedly running in interactive mode.
    interactive_socket=$CDF2CIM_INDEXER_HOME/ops/daemon/interactive.sock
    if [ -e "$interactive_socket" ]; then
        log "cdf2cim indexer is already running in interactive mode:"
        log "- if the socket file ($interactive_socket) is stale then clear it and retry,"
        exit 0
    fi
    touch $interactive_socket

    # Launch worker.
    pushd $CDF2CIM_INDEXER_HOME
    pipenv run dramatiq interactive \
        --path $CDF2CIM_INDEXER_HOME/indexer/workers \
        --watch $CDF2CIM_INDEXER_HOME/indexer
    popd -1

    # Tidy up.
    rm $interactive_socket
}

# Invoke entry point.
main $1
