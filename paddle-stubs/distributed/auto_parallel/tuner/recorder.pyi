from __future__ import annotations

from typing import Any, Optional

class MetricRecord:
    def __init__(self, value: Any, step: Any) -> None: ...
    @property
    def value(self): ...
    @value.setter
    def value(self, value: Any) -> None: ...
    @property
    def step(self): ...
    @step.setter
    def step(self, step: Any) -> None: ...
    def mean(self): ...
    def get_state(self): ...
    @classmethod
    def from_state(cls, state: Any): ...
    def __eq__(self, other: object) -> Any: ...

class MetricRecords:
    def __init__(self, direction: str = ...) -> None: ...
    @property
    def records(self): ...
    @records.setter
    def records(self, records: Any) -> None: ...
    @property
    def direction(self): ...
    @direction.setter
    def direction(self, direction: Any) -> None: ...
    def update(self, value: Any, step: int = ...) -> None: ...
    def get_best_value(self): ...
    def get_best_step(self): ...
    def get_statistics(self): ...
    def get_state(self): ...
    @classmethod
    def from_state(cls, state: Any): ...

class MetricsRecorder:
    def __init__(self, metrics: Any | None = ...) -> None: ...
    @property
    def records(self): ...
    def exists(self, name: Any): ...
    def register_metrics(self, metrics: Any | None = ...) -> None: ...
    def register(self, name: Any, direction: Any | None = ...) -> None: ...
    def update(self, name: Any, value: Any, step: int = ...): ...
    def get_records(self, name: Any): ...
    def set_records(self, name: Any, records: Any) -> None: ...
    def get_best_value(self, name: Any): ...
    def get_best_step(self, name: Any): ...
    def get_statistics(self, name: Any): ...
    def get_state(self): ...
    @classmethod
    def from_state(cls, state: Any): ...
