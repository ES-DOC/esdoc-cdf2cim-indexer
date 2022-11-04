#!/bin/bash

# Wraps standard echo by adding application prefix.
function log()
{
    # Set timestamp.
	declare now=`date +%Y-%m-%dT%H:%M:%S:000000`

    # Support tabs.
	declare tabs=''

    # Emit log message.
	if [ "$1" ]; then
		if [ "$2" ]; then
			for ((i=0; i<$2; i++))
			do
				declare tabs+='\t'
			done
	    	echo -e $now" [INFO] [$$] CDF2CIM-INDEXER :: "$tabs$1
	    else
	    	echo -e $now" [INFO] [$$] CDF2CIM-INDEXER :: "$1
	    fi
	else
	    echo -e $now" [INFO] [$$] CDF2CIM-INDEXER :: "
	fi
}

# Wraps pushd command to suppress stdout.
function pushd () {
    command pushd "$@" > /dev/null
}

# Wraps popd command to suppress stdout.
function popd () {
    command popd "$@" > /dev/null

}