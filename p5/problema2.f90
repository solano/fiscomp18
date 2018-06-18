! Kind of ainda é o primeiro problema, mas agora no regime caótico
! O código eu simplesmente copiei do problema1.f90

subroutine mapa(imax,r,x,resp)
    !f2py intent(out) resp
    real*8 :: x,r
    integer :: i,imax
    real*8 :: resp(imax)

    do i=1,imax
        resp(i) =  x
        x = r*x*(1-x)
    end do
end
