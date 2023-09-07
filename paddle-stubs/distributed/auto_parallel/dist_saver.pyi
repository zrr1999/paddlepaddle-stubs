from __future__ import annotations

from typing import Any

from paddle.base.framework import static_only as static_only

from ..utils import get_logger as get_logger
from .converter import Converter as Converter
from .utils import get_dist_attr as get_dist_attr

def check_filename(re_exp: Any, filename: Any): ...

class DistributedSaver:
    def __init__(self) -> None: ...
    def save(self, path: Any, serial_program: Any, dist_main_program: Any, dist_context: Any) -> None: ...
    def load(
        self, path: Any, program: Any, dist_context: Any, strict: bool = ..., load_optimizer: bool = ...
    ) -> None: ...
    def save_inference_model(self, path: Any, feed_vars: Any, fetch_vars: Any, exe: Any, **kwargs: Any): ...
