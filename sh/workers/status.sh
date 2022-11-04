#!/bin/bash

# Import utils.
source $CDF2CIM_INDEXER_HOME/sh/utils.sh

# Main entry point.
function main()
{
	pushd $CDF2CIM_INDEXER_HOME
	pipenv run supervisorctl -c $CDF2CIM_INDEXER_HOME/ops/config/supervisord.conf status all
	popd -1
}

# Invoke entry point.
main
