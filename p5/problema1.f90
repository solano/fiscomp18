! Primeiro problema do projeto 5 de intro à fiscomp

subroutine pontofixo(r,x,a,n)
    real*8 :: r
    real*8 :: x(n), a(n)
    !f2py depends(n) x
    !f2py intent(out) a
    do i = 1,n
        a(i) = r*x(i)*(1-x(i))
    end do
end

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

subroutine dif (imax,r,x1,eps,resp)
    real*8 :: r,x1,eps,g1,g2
    real*8 :: resp(imax)
    !f2py intent(out) resp

    g1 = x1
    g2 = x1+eps
    do i=1,imax
        resp(i) = abs(g2-g1)
        g1 = g1*r*(1-g1)
        g2 = g2*r*(1-g2)
    end do
end

subroutine lyapunov (n,r,x1, m,lambda)
    real*8 :: x(m),x1(m),lambda(m),r
    !f2py intent(out) lambda
    !f2py depends(m) x1
    lambda=0; x=x1
    do i=1,n
        lambda = lambda + log(abs(r*(1-2*x)))/n
        x = r*x*(1-x)
    end do
end
