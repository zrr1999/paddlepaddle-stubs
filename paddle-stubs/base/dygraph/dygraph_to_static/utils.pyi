from __future__ import annotations

from typing import Any, NamedTuple, Optional

from paddle.utils import gast

PADDLE_MODULE_PREFIX: str
DYGRAPH_MODULE_PREFIX: str
DYGRAPH_TO_STATIC_MODULE_PREFIX: str

class BaseNodeVisitor(gast.NodeVisitor):
    ancestor_nodes: Any = ...
    def __init__(self) -> None: ...
    def visit(self, node: Any): ...

dygraph_class_to_static_api: Any
FOR_ITER_INDEX_PREFIX: str
FOR_ITER_TUPLE_PREFIX: str
FOR_ITER_TUPLE_INDEX_PREFIX: str
FOR_ITER_VAR_LEN_PREFIX: str
FOR_ITER_VAR_NAME_PREFIX: str
FOR_ITER_ZIP_TO_LIST_PREFIX: str

class FullArgSpec:
    args: Any = ...
    varargs: Any = ...
    varkw: Any = ...
    defaults: Any = ...
    kwonlyargs: Any = ...
    kwonlydefaults: Any = ...
    annotations: Any = ...

def getfullargspec(target: Any): ...
def parse_arg_and_kwargs(function: Any): ...
def parse_varargs_name(function: Any): ...
def type_name(v: Any): ...
def make_hashable(x: Any, error_msg: Any | None = ...): ...
def is_api_in_module(node: Any, module_prefix: Any): ...
def is_dygraph_api(node: Any): ...
def is_paddle_api(node: Any): ...
def is_paddle_func(func: Any): ...
def is_numpy_api(node: Any): ...
def is_control_flow_to_transform(
    node: Any, static_analysis_visitor: Any | None = ..., var_name_to_type: Any | None = ...
): ...
def to_static_api(dygraph_class: Any): ...
def to_static_ast(node: Any, class_node: Any): ...
def update_args_of_func(node: Any, dygraph_node: Any, method_name: Any) -> None: ...
def create_api_shape_node(tensor_shape_node: Any): ...
def get_constant_variable_node(name: Any, value: Any, shape: Any = ..., dtype: str = ...): ...
def get_attribute_full_name(node: Any): ...
def generate_name_node(name_ids: Any, ctx: Any = ..., gen_tuple_if_single: bool = ...): ...
def create_funcDef_node(nodes: Any, name: Any, input_args: Any, return_name_ids: Any): ...
def index_in_list(array_list: Any, item: Any): ...
def create_assign_node(name: Any, node: Any): ...

class RenameTransformer(gast.NodeTransformer):
    root: Any = ...
    old_name: str = ...
    new_name: str = ...
    def __init__(self, node: Any) -> None: ...
    def rename(self, old_name: Any, new_name: Any) -> None: ...
    def visit_Name(self, node: Any): ...
    def visit_Attribute(self, node: Any): ...

def ast_to_func(ast_root: Any, dyfunc: Any, delete_on_exit: bool = ...): ...
def recover_globals_attribute(src_obj: Any, dst_obj: Any) -> None: ...
def func_to_source_code(function: Any, dedent: bool = ...): ...
def ast_to_source_code(ast_node: Any): ...
def is_candidate_node(node: Any): ...
def compare_with_none(node: Any): ...

class IsControlFlowVisitor(gast.NodeVisitor):
    ast_root: Any = ...
    static_analysis_visitor: Any = ...
    node_to_wrapper_map: Any = ...
    node_var_type_map: Any = ...
    is_control_flow_num: int = ...
    def __init__(
        self, ast_node: Any, static_analysis_visitor: Any | None = ..., node_var_type_map: Any | None = ...
    ) -> None: ...
    def transform(self): ...
    def visit_BoolOp(self, node: Any): ...
    def visit_Compare(self, node: Any): ...
    def visit_Call(self, node: Any): ...
    def visit_Name(self, node: Any): ...
    def visit_Constant(self, node: Any): ...
    def get_compare_nodes_with_tensor(self): ...

class NameNodeReplaceTransformer(gast.NodeTransformer):
    target_name: Any = ...
    replace_node: Any = ...
    def __init__(self, root_node: Any, target_name: Any, replace_node: Any) -> None: ...
    def visit_Name(self, node: Any): ...

class ForLoopTuplePreTransformer(gast.NodeTransformer):
    wrapper_root: Any = ...
    root: Any = ...
    def __init__(self, wrapper_root: Any) -> None: ...
    def transform(self) -> None: ...
    def visit_For(self, node: Any): ...
    def tuple_to_stmts(self, node: Any, tuple_name: Any, idx: Any = ...): ...
    def is_for_iter(self, for_node: Any): ...
    def is_for_enumerate_iter(self, for_node: Any): ...

class ForNodeVisitor:
    node: Any = ...
    target: Any = ...
    iter_args: Any = ...
    body: Any = ...
    iter_var_name: Any = ...
    iter_idx_name: Any = ...
    iter_var_len_name: Any = ...
    iter_zip_to_list_name: Any = ...
    iter_node: Any = ...
    enum_idx_name: Any = ...
    args_length: Any = ...
    def __init__(self, for_node: Any) -> None: ...
    def parse(self): ...
    def is_for_range_iter(self): ...
    def is_for_iter(self): ...
    def is_for_enumerate_iter(self): ...

class SplitAssignTransformer(gast.NodeTransformer):
    ast_root: Any = ...
    def __init__(self, ast_node: Any) -> None: ...
    def transform(self) -> None: ...
    def visit_Assign(self, node: Any): ...

def unwrap(func: Any): ...
def input_specs_compatible(src_input_specs: Any, desired_input_specs: Any): ...
def slice_is_num(slice_node: Any): ...
