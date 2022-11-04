#!/bin/bash

# Import utils.
source $CDF2CIM_INDEXER_HOME/sh/utils/misc.sh

# Main entry point.
function main()
{
    local PROJECT=${1}

    log_banner
    log "EXECUTING PRODUCER"
    log_banner
    log "For each combination of $PROJECT/institute/model/experiment:"
    log "1. A message is dispatched -> broker."
    log "2. Broker routes message -> consumer."
    log "3. Consumer scans cdf2cim-archive and maps published metadata."
    log_banner
    log "May take some time so please wait :)"
    log_banner

	pushd $CDF2CIM_INDEXER_HOME
	pipenv run python $CDF2CIM_INDEXER_HOME/sh/mq/producer.py --project $PROJECT
	popd -1
}

# Invoke entry point.
for ARGUMENT in "$@"
do
    KEY=$(echo "$ARGUMENT" | cut -f1 -d=)
    VALUE=$(echo "$ARGUMENT" | cut -f2 -d=)
    case "$KEY" in
        project) PROJECT=${VALUE} ;;
        *)
    esac
done

main "${PROJECT:-cmip6}"
