! último problema, será que dá tempo de terminar? São 8h59 da segunda-feira

subroutine pp (N,dt,a,b,c,d,x1,y1, x,y)
    integer :: N
    real*8 :: dt, a,b,c,d, x1,y1
    real*8 :: x(N),y(N), ux,uy
    !f2py intent(out) x,y

    x(1)=x1; y(1)=y1
    do i=1,N-1
        ux = dt*(a*x(i)-b*x(i)*y(i))
        uy = dt*(-c*y(i)+d*x(i)*y(i))
        x(i+1) = x(i) + ux*dt
        y(i+1) = y(i) + uy*dt
    end do
end
