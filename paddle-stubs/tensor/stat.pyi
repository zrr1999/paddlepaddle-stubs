from __future__ import annotations

from typing import Any, Optional

from .._typing import IntSequence, Tensor

def mean(
    x: Tensor,
    axis: Optional[int | IntSequence] = ...,
    keepdim: bool = ...,
    name: Optional[str] = ...,
) -> Tensor: ...
def var(x: Any, axis: Optional[Any] = ..., unbiased: bool = ..., keepdim: bool = ..., name: Optional[Any] = ...): ...
def std(x: Any, axis: Optional[Any] = ..., unbiased: bool = ..., keepdim: bool = ..., name: Optional[Any] = ...): ...
def numel(x: Any, name: Optional[Any] = ...): ...
def median(x: Any, axis: Optional[Any] = ..., keepdim: bool = ..., name: Optional[Any] = ...): ...
def quantile(x: Any, q: Any, axis: Optional[Any] = ..., keepdim: bool = ...): ...
