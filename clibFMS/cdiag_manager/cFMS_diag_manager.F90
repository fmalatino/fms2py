module pyFMS_diag_manager_mod

    use FMS, only : fms_diag_axis_init, fms_diag_field_add_attribute, fms_diag_grid_init,&
        & fms_register_diag_field, fms_register_static_field, fms_send_data, fms_string_utils_c2f_string
    use iso_c_binding

    implicit none

    public :: pyFMS_diag_axis_init
    public :: pyFMS_diag_field_add_attribute
    public :: pyFMS_diag_grid_init
    public :: pyFMS_register_diag_field
    public :: pyFMS_register_static_field
    public :: pyFMS_send_data

    ! type(domain1D), public :: Domain1
    ! type(domain2D), public :: Domain2
    ! type(domainUG), public :: DomainUG

    interface cFMS_diag_axis_init
      module procedure cFMS_diag_axis_init_c_float
      module procedure cFMS_diag_axis_init_c_double
    end interface cFMS_diag_axis_init

    interface cFMS_diag_field_add_attribute
      module procedure cFMS_diag_field_add_attribute_array
      module procedure cFMS_diag_field_add_attribute_scalar
    end interface cFMS_diag_field_add_attribute
    
    interface cFMS_register_diag_field
      module procedure cFMS_register_diag_field_array
      module procedure cFMS_register_diag_field_scalar
    end interface cFMS_register_diag_field

    interface cFMS_diag_grid_init
      module procedure cFMS_diag_grid_init_c_float
      module procedure cFMS_diag_grid_init_c_double
    end interface cFMS_diag_grid_init

    interface cFMS_send_data
        module procedure cFMS_send_data_0d_c_float
        module procedure cFMS_send_data_0d_c_double
        module procedure cFMS_send_data_1d_c_float
        module procedure cFMS_send_data_1d_c_double
        module procedure cFMS_send_data_2d_c_float
        module procedure cFMS_send_data_2d_c_double
        module procedure cFMS_send_data_3d_c_float
        module procedure cFMS_send_data_3d_c_double
        module procedure cFMS_send_data_4d_c_float
        module procedure cFMS_send_data_4d_c_double
    end interface cFMS_send_data

    contains

    subroutine cFMS_diag_field_add_attribute_array(diag_field_id, att_name_ptr, n, att_value) bind(c)

      integer, intent(in)        :: diag_field_id
      type(c_ptr)                :: att_name_ptr
      integer, intent(in)        :: n
      real(c_double), intent(in) :: att_value(n)
    
      character(len=20)          :: att_name

      att_name = fms_string_utils_c2f_string(att_name_ptr)
    
      call fms_diag_field_add_attribute(diag_field_id, att_name, att_value)
    
    end subroutine cFMS_diag_field_add_attribute_array

    subroutine cFMS_diag_field_add_attribute_scalar(diag_field_id, att_name_ptr, att_value) bind(c)

      integer, intent(in)        :: diag_field_id
      type(c_ptr)                :: att_name_ptr
      real(c_double), intent(in) :: att_value
    
      character(len=20)          :: att_name

      att_name = fms_string_utils_c2f_string(att_name_ptr)
    
      call fms_diag_field_add_attribute(diag_field_id, att_name, att_value)
    
    end subroutine cFMS_diag_field_add_attribute_scalar

    subroutine cFMS_register_diag_field_array(module_name_ptr, field_name_ptr, n, axes, out_var) bind(c)

      type(c_ptr), intent(in) :: module_name_ptr
      type(c_ptr), intent(in) :: field_name_ptr
      integer, intent(in)     :: n
      integer, intent(in)     :: axes(n)
      integer, intent(out)    :: out_var
    
      character(len=20)       :: module_name
      character(len=20)       :: field_name
    
      module_name = fms_string_utils_c2f_string(module_name_ptr)
      field_name = fms_string_utils_c2f_string(field_name_ptr)
    
      out_var = fms_register_diag_field(module_name, field_name, axes)
    
    end subroutine cFMS_register_diag_field_array

    subroutine cFMS_register_diag_field_scalar(module_name_ptr, field_name_ptr, out_var) bind(c)
    
      type(c_ptr), intent(in) :: module_name_ptr
      type(c_ptr), intent(in) :: field_name_ptr
      integer, intent(out)    :: out_var
    
      character(len=20)       :: module_name
      character(len=20)       :: field_name
    
      module_name = fms_string_utils_c2f_string(module_name_ptr)
      field_name = fms_string_utils_c2f_string(field_name_ptr)
    
      out_var = fms_register_diag_field(module_name, field_name)
    
    end subroutine cFMS_register_diag_field_scalar

    subroutine cFMS_register_static_field(module_name_ptr, field_name_ptr, n, axes, out_var) bind(c)

      type(c_ptr), intent(in) :: module_name_ptr
      type(c_ptr), intent(in) :: field_name_ptr
      integer, intent(in)     :: n
      integer, intent(in)     :: axes(n)
      integer, intent(out)    :: out_var

      character(len=20)       :: module_name
      character(len=20)       :: field_name

      module_name = fms_string_utils_c2f_string(module_name_ptr)
      field_name = fms_string_utils_c2f_string(field_name_ptr)

      out_var = fms_register_static_field(module_name, field_name, axes)

    end subroutine cFMS_register_static_field

#include "include/cFMS_diag_manager.fh"

end module pyFMS_diag_manager_mod