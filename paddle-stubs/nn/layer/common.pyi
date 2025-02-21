from __future__ import annotations

from typing import Any, Literal

from paddle.framework import ParamAttr
from paddle.nn import Layer
from typing_extensions import TypeAlias

from ..._typing import (
    DataLayout1D,
    DataLayout1DVariant,
    DataLayout2D,
    DataLayout3D,
    IntSequence,
    Numberic,
    NumbericSequence,
    Tensor,
)
from ...base.dygraph import Flatten as Flatten

InterpolationMode: TypeAlias = Literal["linear", "bilinear", "trilinear", "nearest", "bicubic"]

class Identity(Layer):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def forward(self, input: Tensor) -> Tensor: ...
    __call__ = forward

class Linear(Layer):
    weight: Tensor = ...
    bias: Tensor = ...
    def __init__(
        self,
        in_features: int,
        out_features: int,
        weight_attr: ParamAttr | None = ...,
        bias_attr: ParamAttr | None = ...,
        name: str | None = ...,
    ) -> None: ...
    def forward(self, input: Tensor) -> Tensor: ...
    def extra_repr(self) -> Tensor: ...
    __call__ = forward

class Upsample(Layer):
    size: Any = ...
    scale_factor: Any = ...
    mode: Any = ...
    align_corners: Any = ...
    align_mode: Any = ...
    data_format: Any = ...
    name: str = ...
    def __init__(
        self,
        size: IntSequence | Tensor | None = ...,
        scale_factor: Numberic | NumbericSequence | Tensor | None = ...,
        mode: InterpolationMode = ...,
        align_corners: bool = ...,
        align_mode: int = ...,
        data_format: str = ...,
        name: str | None = ...,
    ) -> None: ...
    def forward(self, x: Tensor) -> Tensor: ...
    def extra_repr(self) -> Tensor: ...
    __call__ = forward

class UpsamplingNearest2D(Layer):
    size: Any = ...
    scale_factor: Any = ...
    data_format: Any = ...
    name: str = ...
    def __init__(
        self,
        size: IntSequence | Tensor | None = ...,
        scale_factor: Numberic | NumbericSequence | Tensor | None = ...,
        data_format: DataLayout1DVariant | DataLayout2D | DataLayout3D = ...,
        name: str | None = ...,
    ) -> None: ...
    def forward(self, x: Tensor) -> Tensor: ...
    def extra_repr(self) -> Tensor: ...
    __call__ = forward

class UpsamplingBilinear2D(Layer):
    size: Any = ...
    scale_factor: Any = ...
    data_format: Any = ...
    name: str = ...
    def __init__(
        self,
        size: IntSequence | Tensor | None = ...,
        scale_factor: Numberic | NumbericSequence | Tensor | None = ...,
        data_format: DataLayout1DVariant | DataLayout2D | DataLayout3D = ...,
        name: str | None = ...,
    ) -> None: ...
    def forward(self, x: Tensor) -> Tensor: ...
    def extra_repr(self) -> Tensor: ...
    __call__ = forward

class Bilinear(Layer):
    weight: Tensor = ...
    bias: Tensor = ...
    def __init__(
        self,
        in1_features: int,
        in2_features: int,
        out_features: int,
        weight_attr: ParamAttr | None = ...,
        bias_attr: ParamAttr | None = ...,
        name: str | None = ...,
    ) -> None: ...
    def forward(self, x1: Tensor, x2: Tensor) -> Tensor: ...
    def extra_repr(self) -> Tensor: ...
    __call__ = forward

class Dropout(Layer):
    p: Any = ...
    axis: Any = ...
    mode: Any = ...
    name: str = ...
    def __init__(
        self,
        p: float = ...,
        axis: int | IntSequence | None = ...,
        mode: Literal["upscale_in_train", "downscale_in_infer"] = ...,
        name: str | None = ...,
    ) -> None: ...
    def forward(self, input: Tensor) -> Tensor: ...
    def extra_repr(self) -> Tensor: ...
    __call__ = forward

class Dropout2D(Layer):
    p: Any = ...
    data_format: Any = ...
    name: str = ...
    def __init__(
        self,
        p: float = ...,
        data_format: DataLayout2D = ...,
        name: str | None = ...,
    ) -> None: ...
    def forward(self, input: Tensor) -> Tensor: ...
    def extra_repr(self) -> Tensor: ...
    __call__ = forward

class Dropout3D(Layer):
    p: Any = ...
    data_format: Any = ...
    name: str = ...
    def __init__(
        self,
        p: float = ...,
        data_format: DataLayout3D = ...,
        name: str | None = ...,
    ) -> None: ...
    def forward(self, input: Tensor) -> Tensor: ...
    def extra_repr(self) -> Tensor: ...
    __call__ = forward

class AlphaDropout(Layer):
    p: Any = ...
    name: str = ...
    def __init__(self, p: float = ..., name: str | None = ...) -> None: ...
    def forward(self, input: Tensor) -> Tensor: ...
    def extra_repr(self) -> Tensor: ...
    __call__ = forward

class Pad1D(Layer):
    def __init__(
        self,
        padding: int | IntSequence | Tensor,
        mode: Literal["constant", "reflect", "replicate", "circular"] = ...,
        value: float = ...,
        data_format: DataLayout1D = ...,
        name: str | None = ...,
    ) -> None: ...
    def forward(self, x: Tensor) -> Tensor: ...
    def extra_repr(self) -> Tensor: ...
    __call__ = forward

class Pad2D(Layer):
    def __init__(
        self,
        padding: int | IntSequence | Tensor,
        mode: Literal["constant", "reflect", "replicate", "circular"] = ...,
        value: float = ...,
        data_format: DataLayout2D = ...,
        name: str | None = ...,
    ) -> None: ...
    def forward(self, x: Tensor) -> Tensor: ...
    def extra_repr(self) -> Tensor: ...
    __call__ = forward

class ZeroPad2D(Layer):
    def __init__(
        self,
        padding: int | IntSequence | Tensor,
        data_format: DataLayout2D = ...,
        name: str | None = ...,
    ) -> None: ...
    def forward(self, x: Tensor) -> Tensor: ...
    def extra_repr(self) -> Tensor: ...
    __call__ = forward

class Pad3D(Layer):
    def __init__(
        self,
        padding: int | IntSequence | Tensor,
        mode: Literal["constant", "reflect", "replicate", "circular"] = ...,
        value: float = ...,
        data_format: DataLayout3D = ...,
        name: str | None = ...,
    ) -> None: ...
    def forward(self, x: Tensor) -> Tensor: ...
    def extra_repr(self) -> Tensor: ...
    __call__ = forward

class CosineSimilarity(Layer):
    def __init__(self, axis: int = ..., eps: float = ...) -> None: ...
    def forward(self, x1: Tensor, x2: Tensor) -> Tensor: ...
    def extra_repr(self) -> Tensor: ...
    __call__ = forward

class Embedding(Layer):
    weight: Any = ...
    def __init__(
        self,
        num_embeddings: int,
        embedding_dim: int,
        padding_idx: int | None = ...,
        sparse: bool = ...,
        weight_attr: ParamAttr | None = ...,
        name: str | None = ...,
    ) -> None: ...
    def forward(self, x: Tensor) -> Tensor: ...
    def extra_repr(self) -> Tensor: ...
    __call__ = forward

class Unfold(Layer):
    kernel_sizes: Any = ...
    dilations: Any = ...
    paddings: Any = ...
    strides: Any = ...
    name: str = ...
    def __init__(
        self,
        kernel_sizes: int | IntSequence,
        dilations: int = ...,
        paddings: int = ...,
        strides: int = ...,
        name: str | None = ...,
    ) -> None: ...
    def forward(self, input: Tensor) -> Tensor: ...
    def extra_repr(self) -> Tensor: ...
    __call__ = forward

class Fold(Layer):
    output_sizes: Any = ...
    kernel_sizes: Any = ...
    dilations: Any = ...
    paddings: Any = ...
    strides: Any = ...
    name: str = ...
    def __init__(
        self,
        output_sizes: IntSequence,
        kernel_sizes: int | IntSequence,
        dilations: int | IntSequence = ...,
        paddings: int | IntSequence = ...,
        strides: int | IntSequence = ...,
        name: str | None = ...,
    ) -> None: ...
    def forward(self, input: Tensor) -> Tensor: ...
    def extra_repr(self) -> Tensor: ...
    __call__ = forward
