! -*-f90-*-
!***********************************************************************
!*                   GNU Lesser General Public License
!*
!* This file is part of the GFDL Flexible Modeling System (FMS).
!*
!* FMS is free software: you can redistribute it and/or modify it under
!* the terms of the GNU Lesser General Public License as published by
!* the Free Software Foundation, either version 3 of the License, or (at
!* your option) any later version.
!*
!* FMS is distributed in the hope that it will be useful, but WITHOUT
!* ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
!* FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
!* for more details.
!*
!* You should have received a copy of the GNU Lesser General Public
!* License along with FMS.  If not, see <http://www.gnu.org/licenses/>.
!***********************************************************************

!> @file
!> @brief Various routines handling domains in @ref mpp_domains_mod

!> @addtogroup pyfms_diag_manager_mod
!> @{
subroutine CFMS_DIAG_AXIS_INIT_(name_ptr, dim, array_data, units_ptr, cart_name_ptr, out_var) bind(c)

  type(c_ptr), intent(in)       :: name_ptr
  integer, intent(in)           :: dim
  real(CFMS_KIND_), intent(in)  :: array_data(dim)
  type(c_ptr), intent(in)       :: units_ptr
  type(c_ptr), intent(in)       :: cart_name_ptr
  integer, intent(out)          :: out_var

  character(len=20) :: name
  character(len=20) :: units
  character(len=20) :: cart_name

  name = fms_string_utils_c2f_string(name_ptr)
  units = fms_string_utils_c2f_string(units_ptr)
  cart_name = fms_string_utils_c2f_string(cart_name_ptr)

  out_var = fms_diag_axis_init(name, array_data, units, cart_name)

end subroutine CFMS_DIAG_AXIS_INIT_

!############################################################################

subroutine CFMS_DIAG_GRID_INIT_(glo_lat, glo_lon, aglo_lat, aglo_lon, &
  & dim_glo1, dim_glo2, dim_aglo1, dim_aglo2) bind(c)

  integer, intent(in)           :: dim_glo1, dim_glo2, dim_aglo1, dim_aglo2
  real(CFMS_KIND_), intent(in)  :: glo_lat(dim_glo1,dim_glo2)
  real(CFMS_KIND_), intent(in)  :: glo_lon(dim_glo1,dim_aglo2)
  real(CFMS_KIND_), intent(in)  :: aglo_lat(dim_aglo1,dim_aglo2)
  real(CFMS_KIND_), intent(in)  :: aglo_lon(dim_aglo1,dim_aglo2)

  type(domain2d) :: Domain
  

  call fms_diag_grid_init(Domain, glo_lat, glo_lon, aglo_lat, aglo_lon)

end subroutine CFMS_DIAG_GRID_INIT_

!############################################################################

subroutine CFMS_SEND_DATA_0D_(diag_field_id, field, out_var) bind(c)

  integer, intent(in)           :: diag_field_id
  real(CFMS_KIND_), intent(in)  :: field
  logical, intent(out)          :: out_var

  out_var = fms_diag_send_data(diag_field_id, field)

end subroutine CFMS_SEND_DATA_0D_

!############################################################################

subroutine CFMS_SEND_DATA_1D_(diag_field_id, n, field, out_var) bind(c)

  integer, intent(in)           :: diag_field_id
  integer, intent(in)           :: n
  real(CFMS_KIND_), intent(in)  :: field(n)
  logical, intent(out)          :: out_var

  out_var = fms_diag_send_data(diag_field_id, field)

end subroutine CFMS_SEND_DATA_1D_

!############################################################################

subroutine CFMS_SEND_DATA_2D_(diag_field_id, n, m, field, out_var) bind(c)

  integer, intent(in)           :: diag_field_id
  integer, intent(in)           :: n
  integer, intent(in)           :: m
  real(CFMS_KIND_), intent(in)  :: field(n,m)
  logical, intent(out)          :: out_var

  out_var = fms_diag_send_data(diag_field_id, field)

end subroutine CFMS_SEND_DATA_2D_

!############################################################################

subroutine CFMS_SEND_DATA_3D_(diag_field_id, n, m, l, field, out_var) bind(c)

  integer, intent(in)           :: diag_field_id
  integer, intent(in)           :: n
  integer, intent(in)           :: m
  integer, intent(in)           :: l
  real(CFMS_KIND_), intent(in)  :: field(n,m,l)
  logical, intent(out)          :: out_var

  out_var = fms_diag_send_data(diag_field_id, field)

end subroutine CFMS_SEND_DATA_3D_

!############################################################################

subroutine CFMS_SEND_DATA_4D_(diag_field_id, n, m, l, k, field, out_var) bind(c)

  integer, intent(in)           :: diag_field_id
  integer, intent(in)           :: n
  integer, intent(in)           :: m
  integer, intent(in)           :: l
  integer, intent(in)           :: k
  real(CFMS_KIND_), intent(in)  :: field(n,m,l,k)
  logical, intent(out)          :: out_var

  out_var = fms_diag_send_data(diag_field_id, field)

end subroutine CFMS_SEND_DATA_4D_

!############################################################################
!> @}