import datetime
import typing



class SimulationAxis():
    """Simulated axis in relation to associated ensemble.
    
    """
    def __init__(self, realization: int, initialization: int, physics: int, forcing: int):
        """Instance initialiser."""
        self.realization: int = realization
        self.initialization: int = initialization
        self.physics: int = physics
        self.forcing: int = forcing
    

    def __repr__(self) -> str:
        """Instance representation."""
        return f"r{self.realization}i{self.initialization}p{self.physics}f{self.forcing}"


class SimulationTimeRange():
    """Simulated time range during which a model run emits output.
    
    """
    def __init__(self, start: datetime.datetime, end: datetime.datetime):
        """Instance initialiser."""
        self.start: datetime.datetime = start
        self.end: datetime.datetime = end


    def __repr__(self) -> str:
        """Instance representation."""
        return f"{self.start.isoformat()} :: {self.end.isoformat()}"


class SimulationTimeSlice():
    def __init__(self, calendar: str, range: SimulationTimeRange, range_of_branch: SimulationTimeRange):
        """Instance initialiser."""
        self.calendar: str = calendar
        self.range: SimulationTimeRange = range
        self.range_of_branch: SimulationTimeRange = range_of_branch


    def __eq__(self, other) -> bool:
        """Instance equality."""
        return \
            self.calendar == other.calendar and \
            self.range.start == other.range.start and \
            self.range.end == other.range.end


    def __repr__(self) -> str:
        """Instance representation."""
        return f"{self.calendar} :: {self.range}"


class SimulationTimeSeries():
    """Simulated time series over which a model run emits output.
    
    """
    def __init__(self, calendar: str, range: SimulationTimeRange):
        """Instance initialiser."""
        self.calendar: str = calendar
        self.time_slices: list = list()
        self.range: SimulationTimeRange = range


    def __getitem__(self, time_slice: SimulationTimeSlice) -> typing.Optional[SimulationTimeSlice]:
        """Instance item accessor."""
        for item in self:
            if item == time_slice:
                return item


    def __iter__(self) -> typing.Iterable[SimulationTimeSlice]:
        """Instance iterator."""
        return iter(sorted(self.time_slices, key=lambda i: i.range.start))


    def __repr__(self) -> str:
        """Instance representation."""
        return f"{self.calendar} :: {self.range} :: {len(self.time_slices)}"


class Simulation():
    def __init__(self, institute: str, source_id: str, experiment: str):
        """Instance initialiser."""
        self.experiment: str = experiment
        self.institute: str = institute
        self.mip_era: str = "cmip6"
        self.source_id: str = source_id
        self.ripf: SimulationAxis = None
        self.ripf_parent: SimulationAxis = None
        self.time_series: list = list()


    def __getitem__(self, calendar: str) -> typing.Optional[SimulationTimeSeries]:
        """Instance item accessor."""
        for item in self:
            if item.calendar == calendar:
                return item


    def __iter__(self) -> typing.Iterable[SimulationTimeSeries]:
        """Instance iterator."""
        return iter(sorted(self.time_series, key=lambda i: i.calendar))


    def __repr__(self) -> str:
        """Instance representation."""
        return f"{self.mip_era} :: {self.institute} :: {self.source_id} :: {self.experiment} :: {self.ripf} :: {len(self.time_series)}"


class SimulationJSONBlob():
    """Wraps a JSON blob published from an esgf node.
    
    """ 
    def __init__(self, institute: str, source_id: str, experiment: str, blob: dict):
        """Instance initialiser."""
        self.calendar = blob['calendar']
        self.institute = institute
        self.source_id = source_id
        self.experiment = experiment
        self.hash_id = blob['_hash_id']
        self.mip_era = blob['mip_era'].lower()
        self.ripf = SimulationAxis(
            blob['realization_index'],
            blob['initialization_index'],
            blob['physics_index'],
            blob['forcing_index'],
        )
        self.ripf_parent = SimulationAxis(
            blob['parent_realization_index'],
            blob['parent_initialization_index'],
            blob['parent_physics_index'],
            blob['parent_forcing_index'],
        )
        self.range = SimulationTimeRange(
            datetime.datetime.strptime(blob['start_time'], "%Y-%m-%dT%H:%M:%SZ"),
            datetime.datetime.strptime(blob['end_time'], "%Y-%m-%dT%H:%M:%SZ"),
        )
        self.range_of_branch = SimulationTimeRange(
            datetime.datetime.strptime(blob['branch_time_in_child'], "%Y-%m-%dT%H:%M:%SZ"),
            datetime.datetime.strptime(blob['branch_time_in_parent'], "%Y-%m-%dT%H:%M:%SZ"),
        )
