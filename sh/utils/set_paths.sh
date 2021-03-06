# Root paths.
export CDF2CIM_INDEXER_PATH_ROOT=$HOME/.cdf2cim-indexer
export CDF2CIM_INDEXER_PATH_VARS=$CDF2CIM_INDEXER_PATH_ROOT/vars
export CDF2CIM_INDEXER_PATH_OPS=$CDF2CIM_INDEXER_PATH_ROOT/ops

# Repo internal paths.
export CDF2CIM_INDEXER_PATH_SH=$CDF2CIM_INDEXER_HOME/sh
export CDF2CIM_INDEXER_PATH_SCRIPTS=$CDF2CIM_INDEXER_HOME/sh/scripts
export CDF2CIM_INDEXER_PATH_SRC=$CDF2CIM_INDEXER_HOME/indexer

# Set python path.
export PYTHONPATH=$CDF2CIM_INDEXER_HOME:$PYTHONPATH

# Ensure shell scripts are executable.
chmod a+x $CDF2CIM_INDEXER_PATH_SH/*.sh
chmod a+x $CDF2CIM_INDEXER_PATH_SH/*/*.sh

# Ensure ops directories exist
mkdir -p $CDF2CIM_INDEXER_PATH_OPS
mkdir -p $CDF2CIM_INDEXER_PATH_OPS/config
mkdir -p $CDF2CIM_INDEXER_PATH_OPS/daemon
mkdir -p $CDF2CIM_INDEXER_PATH_OPS/logs
