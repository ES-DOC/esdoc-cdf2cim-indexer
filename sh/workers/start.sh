#!/bin/bash

# Import utils.
source $CDF2CIM_INDEXER_PATH_SH/utils.sh

# Main entry point.
function main()
{
	# Escape if already running interactively.
	interactive_socket=$CDF2CIM_INDEXER_PATH_OPS/daemon/interactive.sock
    if [ -e $interactive_socket ]; then
        log "cdf2cim-indexer is already running in interactive mode:"
        log "- if the socket file ($interactive_socket) is stale then clear it and retry,"
		exit 0
    fi

	# Reset logs.
	source $CDF2CIM_INDEXER_PATH_SH/workers/reset_logs.sh

	# Launch daemon.
	pushd $CDF2CIM_INDEXER_HOME
	pipenv run supervisord -c $CDF2CIM_INDEXER_PATH_OPS/config/supervisord.conf
	popd -1
	log "workers :: launched supervisord"
	
	# Wait for daemon to start and display status.
	sleep 3.0
	source $CDF2CIM_INDEXER_PATH_SH/workers/status.sh
}

# Invoke entry point.
main
