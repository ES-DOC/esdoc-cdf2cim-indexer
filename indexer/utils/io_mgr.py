import json
import os
import pathlib
import typing

from indexer.handlers.cmip6.simulations.models import SimulationJSONBlob
from indexer.utils import logger



# CDF2CIM JSON archive.
_PATH_ARCHIVE = pathlib.Path(os.getenv("CDF2CIM_ARCHIVE_HOME")) / "data"

# CDF2CIM JSON file type wrappers.
_JSON_BLOB_TYPES = {
    "cmip6": SimulationJSONBlob
}


def yield_json_blobs(mip_era: str, institute: str, source_id: str, experiment: str) -> typing.Generator:
    """Factory method: yields published CDF2CIM json blobs.

    :param mip_era: Canonical (pyessv) name of mip_era.
    :param institute: Canonical (pyessv) name of institute.
    :param source_id: Canonical (pyessv) name of source_id.
    :param experiment: Canonical (pyessv) name of experiment.

    """
    # Set path.
    path = _PATH_ARCHIVE / mip_era / institute / source_id / experiment
    if path.exists == False:
        logger.log_warning(f"Invalid CDF2CIM archive folder: {path}")
        return
    
    # Set type.
    blob_cls = _JSON_BLOB_TYPES.get(mip_era)
    if not blob_cls:
        logger.log_warning(f"Invalid CDF2CIM blob type: {mip_era}")
        return

    # Yield blobs.
    for f in path.glob("*.json"):
        with open(f, 'r') as fstream:
            yield blob_cls(
                institute,
                source_id,
                experiment,
                json.loads(fstream.read())
                )


# 1951-01-01T00:00:00Z::1961-01-01T00:00:00Z
# {
#     "_hash_id": "83a4a507797407eb9df3774fde726f71",
#     "activity_id": [
#         "HighResMIP"
#     ],
#     "branch_time_in_child": "2001-01-01T00:00:00Z",
#     "branch_time_in_parent": "1950-01-01T00:00:00Z",
#     "calendar": "proleptic_gregorian",
#     "dataset_versions": [
#         "v20170825"
#     ],
#     "end_time": "2011-01-01T00:00:00Z",
#     "experiment_id": "control-1950",
#     "filenames": [
#         "/mnt/lustre02/work/ik1017/CMIP6/data/CMIP6/HighResMIP/AWI/AWI-CM-1-1-HR/control-1950/r1i1p1f2/Omon/wo/gn/v20170825/wo_Omon_AWI-CM-1-1-HR_control-1950_r1i1p1f2_gn_200101-201012.nc"
#     ],
#     "forcing_index": 2,
#     "further_info_url": "https://furtherinfo.es-doc.org/CMIP6.AWI.AWI-CM-1-1-HR.control-1950.none.r1i1p1f2",
#     "initialization_index": 1,
#     "institution_id": "AWI",
#     "mip_era": "CMIP6",
#     "parent_forcing_index": 2,
#     "parent_initialization_index": 1,
#     "parent_physics_index": 1,
#     "parent_realization_index": 1,
#     "physics_index": 1,
#     "realization_index": 1,
#     "source_id": "AWI-CM-1-1-HR",
#     "start_time": "2001-01-01T00:00:00Z",
#     "sub_experiment_id": "none"
# }
# 1951-01-01T01:30:00Z::1960-12-31T22:30:00Z
# {
#     "_hash_id": "83a4a507797407eb9df3774fde726f71",
#     "activity_id": [
#         "HighResMIP"
#     ],
#     "branch_time_in_child": "2001-01-01T00:00:00Z",
#     "branch_time_in_parent": "1950-01-01T00:00:00Z",
#     "calendar": "proleptic_gregorian",
#     "dataset_versions": [
#         "v20170825"
#     ],
#     "end_time": "2011-01-01T00:00:00Z",
#     "experiment_id": "control-1950",
#     "filenames": [
#         "/mnt/lustre02/work/ik1017/CMIP6/data/CMIP6/HighResMIP/AWI/AWI-CM-1-1-HR/control-1950/r1i1p1f2/Omon/wo/gn/v20170825/wo_Omon_AWI-CM-1-1-HR_control-1950_r1i1p1f2_gn_200101-201012.nc"
#     ],
#     "forcing_index": 2,
#     "further_info_url": "https://furtherinfo.es-doc.org/CMIP6.AWI.AWI-CM-1-1-HR.control-1950.none.r1i1p1f2",
#     "initialization_index": 1,
#     "institution_id": "AWI",
#     "mip_era": "CMIP6",
#     "parent_forcing_index": 2,
#     "parent_initialization_index": 1,
#     "parent_physics_index": 1,
#     "parent_realization_index": 1,
#     "physics_index": 1,
#     "realization_index": 1,
#     "source_id": "AWI-CM-1-1-HR",
#     "start_time": "2001-01-01T00:00:00Z",
#     "sub_experiment_id": "none"
# }