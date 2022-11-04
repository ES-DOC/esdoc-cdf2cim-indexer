#!/bin/bash

# Import utils.
source $CDF2CIM_INDEXER_HOME/sh/utils/misc.sh

# Main entry point.
function main()
{
	pushd $CDF2CIM_INDEXER_HOME
	pipenv run supervisorctl -c $CDF2CIM_INDEXER_HOME/ops/config/supervisord.conf stop all &>/dev/null 
	pipenv run supervisorctl -c $CDF2CIM_INDEXER_HOME/ops/config/supervisord.conf shutdown &>/dev/null
	popd -1

	log "workers  :: killed daemon"
}

# Invoke entry point.
main
