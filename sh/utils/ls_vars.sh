#!/bin/bash

# Import utils.
source $CDF2CIM_INDEXER_PATH_SH/utils.sh

# Main entry point.
function main()
{
    printenv | grep CDF2CIM_INDEXER_ | sort
}

# Invoke entry point.
main
