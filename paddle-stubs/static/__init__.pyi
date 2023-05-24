from __future__ import annotations

from typing import Any

from typing_extensions import TypeAlias

BuildStrategy: TypeAlias = Any

from ..fluid.backward import append_backward as append_backward
from ..fluid.backward import gradients as gradients
from ..fluid.compiler import CompiledProgram as CompiledProgram
from ..fluid.compiler import ExecutionStrategy as ExecutionStrategy
from ..fluid.compiler import IpuCompiledProgram as IpuCompiledProgram
from ..fluid.compiler import IpuStrategy as IpuStrategy
from ..fluid.executor import Executor as Executor
from ..fluid.executor import global_scope as global_scope
from ..fluid.executor import scope_guard as scope_guard
from ..fluid.framework import Program as Program
from ..fluid.framework import Variable as Variable
from ..fluid.framework import cpu_places as cpu_places
from ..fluid.framework import cuda_places as cuda_places
from ..fluid.framework import default_main_program as default_main_program
from ..fluid.framework import default_startup_program as default_startup_program
from ..fluid.framework import device_guard as device_guard
from ..fluid.framework import ipu_shard_guard as ipu_shard_guard
from ..fluid.framework import mlu_places as mlu_places
from ..fluid.framework import name_scope as name_scope
from ..fluid.framework import npu_places as npu_places
from ..fluid.framework import program_guard as program_guard
from ..fluid.framework import xpu_places as xpu_places
from ..fluid.io import load as load
from ..fluid.io import load_program_state as load_program_state
from ..fluid.io import save as save
from ..fluid.io import set_program_state as set_program_state
from ..fluid.layers import create_global_var as create_global_var
from ..fluid.layers import create_parameter as create_parameter
from ..fluid.layers.control_flow import Print as Print
from ..fluid.layers.metric_op import accuracy as accuracy
from ..fluid.layers.metric_op import auc as auc
from ..fluid.layers.nn import py_func as py_func
from ..fluid.optimizer import ExponentialMovingAverage as ExponentialMovingAverage
from ..fluid.parallel_executor import ParallelExecutor as ParallelExecutor
from ..fluid.param_attr import WeightNormParamAttr as WeightNormParamAttr
from .input import InputSpec as InputSpec
from .input import data as data
from .io import deserialize_persistables as deserialize_persistables
from .io import deserialize_program as deserialize_program
from .io import load_from_file as load_from_file
from .io import load_inference_model as load_inference_model
from .io import normalize_program as normalize_program
from .io import save_inference_model as save_inference_model
from .io import save_to_file as save_to_file
from .io import serialize_persistables as serialize_persistables
from .io import serialize_program as serialize_program
