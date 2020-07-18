import pyessv



# Returns set of institutional model configurations.
get_cmip6_institute_sources = pyessv.WCRP.cmip6.get_institute_sources

# Returns set of experiments.
get_cmip6_experiments = lambda: pyessv.WCRP.cmip6.experiment_id


def get_cmip6_institutes(institution_id=None):
    """Returns set of institutes to be processed.

    """
    collection = pyessv.WCRP.cmip6.institution_id if institution_id in (None, '', 'all') else [pyessv.WCRP.cmip6.institution_id[institution_id]]

    return sorted(collection, key=lambda i: i.canonical_name)


def yield_cmip6_simulations():
    """Yields set of model sources (optionally filtered by institution).

    """
    for i, s in yield_cmip6_sources(None):
        for e in get_cmip6_experiments():    
            yield i, s, e


def yield_cmip6_sources(institution_id):
    """Yields set of model sources (optionally filtered by institution).

    """
    for i in get_cmip6_institutes(institution_id):
        for s in get_cmip6_institute_sources(i):
            yield i, s
