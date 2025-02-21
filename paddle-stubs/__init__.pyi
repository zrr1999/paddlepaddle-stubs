from __future__ import annotations

__version__: str

from . import base as base
from . import hub as hub
from . import jit as jit
from . import linalg as linalg
from . import metric as metric
from . import nn as nn
from . import optimizer as optimizer
from . import regularizer as regularizer
from . import signal as signal
from . import static as static
from . import sysconfig as sysconfig
from . import utils as utils
from . import version as version
from . import vision as vision
from ._typing import Tensor as Tensor
from .autograd import grad as grad
from .autograd import is_grad_enabled as is_grad_enabled
from .autograd import no_grad as no_grad
from .autograd import set_grad_enabled as set_grad_enabled
from .batch import batch as batch
from .framework import CPUPlace as CPUPlace
from .framework import CUDAPinnedPlace as CUDAPinnedPlace
from .framework import CUDAPlace as CUDAPlace
from .framework import DataParallel as DataParallel
from .framework import NPUPlace as NPUPlace
from .framework import ParamAttr as ParamAttr
from .framework import create_parameter as create_parameter
from .framework import disable_signal_handler as disable_signal_handler
from .framework import disable_static as disable_static
from .framework import enable_static as enable_static
from .framework import get_default_dtype as get_default_dtype
from .framework import get_flags as get_flags
from .framework import in_dynamic_mode as in_dynamic_mode
from .framework import load as load
from .framework import save as save
from .framework import set_default_dtype as set_default_dtype
from .framework import set_flags as set_flags
from .framework.dtype import bfloat16 as bfloat16
from .framework.dtype import bool as bool
from .framework.dtype import complex64 as complex64
from .framework.dtype import complex128 as complex128
from .framework.dtype import dtype as dtype
from .framework.dtype import float16 as float16
from .framework.dtype import float32 as float32
from .framework.dtype import float64 as float64
from .framework.dtype import int8 as int8
from .framework.dtype import int16 as int16
from .framework.dtype import int32 as int32
from .framework.dtype import int64 as int64
from .framework.dtype import uint8 as uint8
from .framework.random import get_cuda_rng_state as get_cuda_rng_state
from .framework.random import seed as seed
from .framework.random import set_cuda_rng_state as set_cuda_rng_state
from .hapi import Model as Model
from .hapi import flops as flops
from .hapi import summary as summary
from .tensor.attribute import imag as imag
from .tensor.attribute import is_complex as is_complex
from .tensor.attribute import is_floating_point as is_floating_point
from .tensor.attribute import is_integer as is_integer
from .tensor.attribute import rank as rank
from .tensor.attribute import real as real
from .tensor.attribute import shape as shape
from .tensor.creation import arange as arange
from .tensor.creation import assign as assign
from .tensor.creation import clone as clone
from .tensor.creation import complex as complex
from .tensor.creation import diag as diag
from .tensor.creation import diagflat as diagflat
from .tensor.creation import empty as empty
from .tensor.creation import empty_like as empty_like
from .tensor.creation import eye as eye
from .tensor.creation import full as full
from .tensor.creation import full_like as full_like
from .tensor.creation import linspace as linspace
from .tensor.creation import meshgrid as meshgrid
from .tensor.creation import ones as ones
from .tensor.creation import ones_like as ones_like
from .tensor.creation import to_tensor as to_tensor
from .tensor.creation import tril as tril
from .tensor.creation import triu as triu
from .tensor.creation import zeros as zeros
from .tensor.creation import zeros_like as zeros_like
from .tensor.einsum import einsum as einsum
from .tensor.linalg import bincount as bincount
from .tensor.linalg import bmm as bmm
from .tensor.linalg import cross as cross
from .tensor.linalg import dist as dist
from .tensor.linalg import dot as dot
from .tensor.linalg import histogram as histogram
from .tensor.linalg import matmul as matmul
from .tensor.linalg import mv as mv
from .tensor.linalg import t as t
from .tensor.linalg import transpose as transpose
from .tensor.logic import allclose as allclose
from .tensor.logic import bitwise_and as bitwise_and
from .tensor.logic import bitwise_not as bitwise_not
from .tensor.logic import bitwise_or as bitwise_or
from .tensor.logic import bitwise_xor as bitwise_xor
from .tensor.logic import equal as equal
from .tensor.logic import equal_all as equal_all
from .tensor.logic import greater_equal as greater_equal
from .tensor.logic import greater_than as greater_than
from .tensor.logic import is_empty as is_empty
from .tensor.logic import is_tensor as is_tensor
from .tensor.logic import isclose as isclose
from .tensor.logic import less_equal as less_equal
from .tensor.logic import less_than as less_than
from .tensor.logic import logical_and as logical_and
from .tensor.logic import logical_not as logical_not
from .tensor.logic import logical_or as logical_or
from .tensor.logic import logical_xor as logical_xor
from .tensor.logic import not_equal as not_equal
from .tensor.manipulation import as_complex as as_complex
from .tensor.manipulation import as_real as as_real
from .tensor.manipulation import broadcast_tensors as broadcast_tensors
from .tensor.manipulation import broadcast_to as broadcast_to
from .tensor.manipulation import cast as cast
from .tensor.manipulation import chunk as chunk
from .tensor.manipulation import concat as concat
from .tensor.manipulation import crop as crop
from .tensor.manipulation import expand as expand
from .tensor.manipulation import expand_as as expand_as
from .tensor.manipulation import flatten as flatten
from .tensor.manipulation import flip as flip
from .tensor.manipulation import flip as reverse
from .tensor.manipulation import gather as gather
from .tensor.manipulation import gather_nd as gather_nd
from .tensor.manipulation import moveaxis as moveaxis
from .tensor.manipulation import put_along_axis as put_along_axis
from .tensor.manipulation import repeat_interleave as repeat_interleave
from .tensor.manipulation import reshape as reshape
from .tensor.manipulation import reshape_ as reshape_
from .tensor.manipulation import roll as roll
from .tensor.manipulation import rot90 as rot90
from .tensor.manipulation import scatter as scatter
from .tensor.manipulation import scatter_ as scatter_
from .tensor.manipulation import scatter_nd as scatter_nd
from .tensor.manipulation import scatter_nd_add as scatter_nd_add
from .tensor.manipulation import shard_index as shard_index
from .tensor.manipulation import slice as slice
from .tensor.manipulation import split as split
from .tensor.manipulation import squeeze as squeeze
from .tensor.manipulation import squeeze_ as squeeze_
from .tensor.manipulation import stack as stack
from .tensor.manipulation import strided_slice as strided_slice
from .tensor.manipulation import take_along_axis as take_along_axis
from .tensor.manipulation import tensordot as tensordot
from .tensor.manipulation import tile as tile
from .tensor.manipulation import tolist as tolist
from .tensor.manipulation import unbind as unbind
from .tensor.manipulation import unique as unique
from .tensor.manipulation import unique_consecutive as unique_consecutive
from .tensor.manipulation import unsqueeze as unsqueeze
from .tensor.manipulation import unsqueeze_ as unsqueeze_
from .tensor.manipulation import unstack as unstack
from .tensor.math import abs as abs
from .tensor.math import acos as acos
from .tensor.math import acosh as acosh
from .tensor.math import add as add
from .tensor.math import add_n as add_n
from .tensor.math import addmm as addmm
from .tensor.math import all as all
from .tensor.math import amax as amax
from .tensor.math import amin as amin
from .tensor.math import angle as angle
from .tensor.math import any as any
from .tensor.math import asin as asin
from .tensor.math import asinh as asinh
from .tensor.math import atan as atan
from .tensor.math import atan2 as atan2
from .tensor.math import atanh as atanh
from .tensor.math import broadcast_shape as broadcast_shape
from .tensor.math import ceil as ceil
from .tensor.math import clip as clip
from .tensor.math import conj as conj
from .tensor.math import cos as cos
from .tensor.math import cosh as cosh
from .tensor.math import cumprod as cumprod
from .tensor.math import cumsum as cumsum
from .tensor.math import deg2rad as deg2rad
from .tensor.math import diagonal as diagonal
from .tensor.math import diff as diff
from .tensor.math import digamma as digamma
from .tensor.math import divide as divide
from .tensor.math import erf as erf
from .tensor.math import erfinv as erfinv
from .tensor.math import exp as exp
from .tensor.math import expm1 as expm1
from .tensor.math import floor as floor
from .tensor.math import floor_divide as floor_divide
from .tensor.math import floor_mod as floor_mod
from .tensor.math import fmax as fmax
from .tensor.math import fmin as fmin
from .tensor.math import gcd as gcd
from .tensor.math import increment as increment
from .tensor.math import inner as inner
from .tensor.math import isfinite as isfinite
from .tensor.math import isinf as isinf
from .tensor.math import isnan as isnan
from .tensor.math import kron as kron
from .tensor.math import lcm as lcm
from .tensor.math import lerp as lerp
from .tensor.math import lgamma as lgamma
from .tensor.math import log as log
from .tensor.math import log1p as log1p
from .tensor.math import log2 as log2
from .tensor.math import log10 as log10
from .tensor.math import logit as logit
from .tensor.math import logsumexp as logsumexp
from .tensor.math import max as max
from .tensor.math import maximum as maximum
from .tensor.math import min as min
from .tensor.math import minimum as minimum
from .tensor.math import mm as mm
from .tensor.math import mod as mod
from .tensor.math import multiplex as multiplex
from .tensor.math import multiply as multiply
from .tensor.math import nanmean as nanmean
from .tensor.math import nansum as nansum
from .tensor.math import neg as neg
from .tensor.math import outer as outer
from .tensor.math import pow as pow
from .tensor.math import prod as prod
from .tensor.math import rad2deg as rad2deg
from .tensor.math import reciprocal as reciprocal
from .tensor.math import remainder as remainder
from .tensor.math import renorm as renorm
from .tensor.math import round as round
from .tensor.math import rsqrt as rsqrt
from .tensor.math import scale as scale
from .tensor.math import sign as sign
from .tensor.math import sin as sin
from .tensor.math import sinh as sinh
from .tensor.math import sqrt as sqrt
from .tensor.math import square as square
from .tensor.math import stanh as stanh
from .tensor.math import subtract as subtract
from .tensor.math import sum as sum
from .tensor.math import tan as tan
from .tensor.math import tanh as tanh
from .tensor.math import tanh_ as tanh_
from .tensor.math import trace as trace
from .tensor.math import trunc as trunc
from .tensor.random import bernoulli as bernoulli
from .tensor.random import check_shape as check_shape
from .tensor.random import multinomial as multinomial
from .tensor.random import normal as normal
from .tensor.random import poisson as poisson
from .tensor.random import rand as rand
from .tensor.random import randint as randint
from .tensor.random import randint_like as randint_like
from .tensor.random import randn as randn
from .tensor.random import randperm as randperm
from .tensor.random import standard_normal as standard_normal
from .tensor.random import uniform as uniform
from .tensor.search import argmax as argmax
from .tensor.search import argmin as argmin
from .tensor.search import argsort as argsort
from .tensor.search import index_sample as index_sample
from .tensor.search import index_select as index_select
from .tensor.search import kthvalue as kthvalue
from .tensor.search import masked_select as masked_select
from .tensor.search import mode as mode
from .tensor.search import nonzero as nonzero
from .tensor.search import searchsorted as searchsorted
from .tensor.search import sort as sort
from .tensor.search import topk as topk
from .tensor.search import where as where
from .tensor.stat import mean as mean
from .tensor.stat import median as median
from .tensor.stat import numel as numel
from .tensor.stat import quantile as quantile
from .tensor.stat import std as std
from .tensor.stat import var as var
from .tensor.to_string import set_printoptions as set_printoptions
