import ctypes as ct
import numpy as np
import dataclasses

import libFMS
import pyFMS_mpp
from pyFMS_utils import *


def diag_axis_init(
    name: str,
    array_data: np.ndarray,
    units: str,
    cart_name: str,
    out_var: int,
    lib: ct.CDLL,    
):
    
    name, name_t = set_Cchar(name)
    dim, dim_t = set_sizevars(array_data)
    units, units_t = set_Cchar(units)
    cart_name, cart_name_t = set_Cchar(cart_name)
    out_var, out_var_t = setscalar_Cint32(out_var)

    if (np.all(array_data.dtype) == ct.c_float):
        array_data, array_data_t = setarray_Cfloat(array_data)
        _pyFMS_diag_axis_init = lib.cfms_diag_axis_init_c_float
        _pyFMS_diag_axis_init.argtypes = [ name_t, *dim_t, array_data_t, units_t, cart_name_t, out_var_t ]
        _pyFMS_diag_axis_init.restype = None
        _pyFMS_diag_axis_init(name, dim, array_data, units, cart_name, out_var)
    elif (np.all(array_data.dtype) == ct.c_double):
        array_data, array_data_t = setarray_Cdouble(array_data)
        _pyFMS_diag_axis_init = lib.cfms_diag_axis_init_c_double
        _pyFMS_diag_axis_init.argtypes = [ name_t, *dim_t, array_data_t, units_t, cart_name_t, out_var_t ]
        _pyFMS_diag_axis_init.restype = None
        _pyFMS_diag_axis_init(name, dim, array_data, units, cart_name, out_var)
    else:
        print("cFMS_diag_manager::diag_axis_init array_data type unknown")



def send_data(
        diag_field_id: int,
        field,
        out_var: bool
        lib: ct.CDLL,
):
    
    diag_field_id, diag_field_id_t = setscalar_Cint32(diag_field_id)
    out_var, out_var_t = setscalar_Cbool(out_var)

    if not hasattr(field, "__len__"):
        if (np.all(field.dtype) == ct.c_float):
            field, field_t = setscalar_Cfloat(field[0])
            _pyFMS_send_data = lib.cfms_send_data_0d_c_float
            _pyFMS_send_data.argtypes = [ diag_field_id_t, field_t, out_var_t ]
            _pyFMS_send_data.restype = None
            _pyFMS_send_data(diag_field_id, field, out_var)
        elif (np.all(field.dtype) == ct.c_double):
            field, field_t = setscalar_Cdouble(field[0])
            _pyFMS_send_data = lib.cfms_send_data_0d_c_double
            _pyFMS_send_data.argtypes = [ diag_field_id_t, field_t, out_var_t ]
            _pyFMS_send_data.restype = None
            _pyFMS_send_data(diag_field_id, field)
        else:
            print("cFMS_diag_manager::send_data_0d field data type unknown")
    elif len(field.shape) == 1:
        n, n_t = set_sizevars(field, 1)
        if (np.all(field.dtype) == ct.c_float):
            field, field_t = setarray_Cfloat(field)
            _pyFMS_send_data = lib.cfms_send_data_1d_c_float
            _pyFMS_send_data.argtypes = [ diag_field_id_t, *n_t, field_t, out_var_t ]
            _pyFMS_send_data.restype = None
            _pyFMS_send_data(diag_field_id, *n, field, out_var)
        elif (np.all(field.dtype) == ct.c_double):
            field, field_t = setarray_Cdouble(field)
            _pyFMS_send_data = lib.cfms_send_data_1d_c_double
            _pyFMS_send_data.argtypes = [ diag_field_id_t, *n_t, field_t, out_var_t ]
            _pyFMS_send_data.restype = None
            _pyFMS_send_data(diag_field_id, *n, field, out_var)
        else:
            print("cFMS_diag_manager::send_data_1d field data type unknown")
    elif len(field.shape) == 2:
        n, n_t = set_sizevars(field, 2)
        if (np.all(field.dtype) == ct.c_float):
            field, field_t = setarray_Cfloat(field)
            _pyFMS_send_data = lib.cfms_send_data_2d_c_float
            _pyFMS_send_data.argtypes = [ diag_field_id_t, *n_t, field_t, out_var_t ]
            _pyFMS_send_data.restype = None
            _pyFMS_send_data(diag_field_id, *n, field, out_var)
        elif (np.all(field.dtype) == ct.c_double):
            field, field_t = setarray_Cdouble(field)
            _pyFMS_send_data = lib.cfms_send_data_2d_c_double
            _pyFMS_send_data.argtypes = [ diag_field_id_t, *n_t, field_t, out_var_t ]
            _pyFMS_send_data.restype = None
            _pyFMS_send_data(diag_field_id, *n, field, out_var)
        else:
            print("cFMS_diag_manager::send_data_2d field data type unknown")
    elif len(field.shape) == 3:
        n, n_t = set_sizevars(field, 3)
        if (np.all(field.dtype) == ct.c_float):
            field, field_t = setarray_Cfloat(field)
            _pyFMS_send_data = lib.cfms_send_data_3d_c_float
            _pyFMS_send_data.argtypes = [ diag_field_id_t, *n_t, field_t, out_var_t ]
            _pyFMS_send_data.restype = None
            _pyFMS_send_data(diag_field_id, *n, field, out_var)
        elif (np.all(field.dtype) == ct.c_double):
            field, field_t = setarray_Cdouble(field)
            _pyFMS_send_data = lib.cfms_send_data_3d_c_double
            _pyFMS_send_data.argtypes = [ diag_field_id_t, *n_t, field_t, out_var_t ]
            _pyFMS_send_data.restype = None
            _pyFMS_send_data(diag_field_id, *n, field, out_var)
        else:
            print("cFMS_diag_manager::send_data_3d field data type unknown")
    elif len(field.shape) == 4:
        n, n_t = set_sizevars(field, 4)
        if (np.all(field.dtype) == ct.c_float):
            field, field_t = setarray_Cfloat(field)
            _pyFMS_send_data = lib.cfms_send_data_4d_c_float
            _pyFMS_send_data.argtypes = [ diag_field_id_t, *n_t, field_t, out_var_t ]
            _pyFMS_send_data.restype = None
            _pyFMS_send_data(diag_field_id, *n, field, out_var)
        elif (np.all(field.dtype) == ct.c_double):
            field, field_t = setarray_Cdouble(field)
            _pyFMS_send_data = lib.cfms_send_data_4d_c_double
            _pyFMS_send_data.argtypes = [ diag_field_id_t, *n_t, field_t, out_var_t ]
            _pyFMS_send_data.restype = None
            _pyFMS_send_data(diag_field_id, *n, field, out_var)
        else:
            print("cFMS_diag_manager::send_data_4d field data type unknown")
    else:
        print("cFMS_diag_manager::send_data rank of field unknown")



def diag_field_add_attribute(
        diag_field_id: int,
        att_name: str,
        att_value,
        lib: ct.CDLL,
):
    diag_field_id, diag_field_id_t = setscalar_Cint32(diag_field_id)
    att_name, att_name_t = set_Cchar(att_name)

    if not hasattr(att_value, "__len__"):
        if (type(att_value) == ct.c_double):
            att_value, att_value_t = setscalar_Cdouble(att_value)
            _pyFMS_diag_field_add_attribute = lib.cfms_diag_field_add_attribute_scalar
            _pyFMS_diag_field_add_attribute.argtypes = [ diag_field_id_t, att_name_t, att_value_t]
            _pyFMS_diag_field_add_attribute(diag_field_id, att_name, att_value)
        else:
            print("cFMS_diag_manager::diag_field_add_attribute_scalar att_value type unknown")
    elif hasattr(att_value, "__len__"):
        n, n_t = set_sizevars(att_value, 1)
        if np.all(att_value.dtype == ct.c_double):
            att_value, att_value_t = setarray_Cdouble(att_value)
            _pyFMS_diag_field_add_attribute = lib.cfms_diag_field_add_attribute_array
            _pyFMS_diag_field_add_attribute.argtypes = [ diag_field_id_t, att_name_t, *n_t, att_value_t]
            _pyFMS_diag_field_add_attribute(diag_field_id, att_name, *n, att_value)
        else:
            print("cFMS_diag_manager::diag_field_add_attribute_array att_value type unknown")
    else:
        print("cFMS_diag_manager::diag_field_add_attribute_array att_value type unknown")



def register_diag_field(
        module_name: str,
        field_name: str,
        axes: np.ndarray = None,
        out_var: int,
        lib: ct.CDLL,
):
    
    module_name, module_name_t = set_Cchar(module_name)
    field_name, field_name_t = set_Cchar(field_name)
    out_var, out_var_t = setscalar_Cint32(out_var)

    if axes:
        n, n_t = set_sizevars(axes, 1)
        axes, axes_t = setarray_Cint32(axes)
        _pyFMS_register_diag_field = lib.cfms_register_diag_field_array
        _pyFMS_register_diag_field.argtypes = [ module_name_t, field_name_t, *n_t, axes_t, out_var_t ]
        _pyFMS_register_diag_field.restype = None
        _pyFMS_register_diag_field(module_name, field_name, *n, axes, out_var)
    else:
        _pyFMS_register_diag_field = lib.cfms_register_diag_field_scalar
        _pyFMS_register_diag_field.argtypes = [ module_name_t, field_name_t, out_var_t ]
        _pyFMS_register_diag_field.restype = None
        _pyFMS_register_diag_field(module_name, field_name, out_var)




def register_static_field(
        module_name: str,
        field_name: str,
        axes: np.ndarray,
        out_var: int,
        lib: ct.CDLL,
):
    
    module_name, module_name_t = set_Cchar(module_name)
    field_name, field_name_t = set_Cchar(field_name)
    n, n_t = set_sizevars(axes)
    axes, axes_t = setarray_Cint32(axes)
    out_var, out_var_t = setscalar_Cint32(out_var)
    _pyFMS_register_diag_field = lib.cfms_register_diag_static_field
    _pyFMS_register_diag_field.argtypes = [ module_name_t, field_name_t, *n_t, axes_t, out_var_t ]
    _pyFMS_register_diag_field.restype = None
    _pyFMS_register_diag_field(module_name, field_name, *n, axes, out_var)
    


        



    
