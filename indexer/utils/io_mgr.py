import json
import os
import pathlib
import typing

from indexer.handlers.cmip6.simulations.models import SimulationJSONBlob
from indexer.utils import logger



# CDF2CIM JSON archive.
_PATH_ARCHIVE = pathlib.Path(os.getenv("CDF2CIM_ARCHIVE_HOME")) / "data"

# CDF2CIM work in progress folder.
_PATH_OUTPUT = pathlib.Path(os.getenv("CDF2CIM_INDEXER_HOME")) / "ops" / "output"

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
    for fpath in path.glob("*.json"):
        with open(fpath, 'r') as fstream:
            try:
                yield blob_cls(
                    fpath,
                    institute,
                    source_id,
                    experiment,
                    json.loads(fstream.read())
                )
            except Exception as err:
                logger.log_error(err)


def write_json_blob(mip_era: str, institute: str, experiment: str, source_id: str, blob: SimulationJSONBlob):
    """Writes a json blob to local file system as part of processing.
    
    :param mip_era: Canonical (pyessv) name of mip_era.
    :param institute: Canonical (pyessv) name of institute.
    :param source_id: Canonical (pyessv) name of source_id.
    :param experiment: Canonical (pyessv) name of experiment.
    :param blob: CDF2CIM JSON blob wrapper.

    """
    # Set base path.
    path_base = _PATH_OUTPUT / mip_era / institute / experiment / source_id / str(blob.ripf) / blob.calendar

    # Create directories raw path.
    for dpath in (
        path_base / "raw",
        path_base / "raw_duplicate",
        path_base / "raw_unique",
    ):
        if not dpath.exists():
            os.makedirs(dpath)

    # Filename reflects time range.
    fname = f"{blob.range}_{blob.hash_id}.json".replace(" :: ", "_")

    # Copy all -> raw.
    fpath = path_base / "raw" / fname
    if not fpath.exists():
        os.symlink(blob.fpath, fpath)

    # Copy duplicates -> raw_duplicates.
    if blob.is_duplicate_time_slice:
        fpath = path_base / "raw_duplicate" / fname
        if not fpath.exists():
            os.symlink(blob.fpath, fpath)

    # Copy unique -> raw_unique.
    if not blob.is_duplicate_time_slice:
        fpath = path_base / "raw_unique" / fname
        if not fpath.exists():
            os.symlink(blob.fpath, fpath)
