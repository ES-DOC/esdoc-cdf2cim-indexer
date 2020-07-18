#!/bin/bash

# Import utils.
source $CDF2CIM_INDEXER_PATH_SH/utils.sh

# Main entry point.
function main()
{
	pushd $CDF2CIM_INDEXER_HOME
	pipenv run supervisorctl -c $CDF2CIM_INDEXER_PATH_OPS/config/supervisord.conf status all
	popd -1
}

# Invoke entry point.
main
