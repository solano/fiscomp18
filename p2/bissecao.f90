        program bissecao
        implicit none

        real*8 a,b,m,erro,f
        real*8 eps, T
        integer i, imax

        parameter(imax = 200)

        read(*,*) T, eps

        i=0
        a = eps
        b = 1-eps
        erro = 10.d0
        do while (erro >= eps .and. i <= imax)
            m = (a+b)/2.d0
            f = m - tanh(m/T)
            if (f>0.d0) then
                b = m
            else if (f < 0.d0) then
                a = m
            else
                a = m
                b = m
            end if

            erro = (b-a)/2.d0
            i = i+1

            write(*,*) i, m, erro
        end do

        end program bissecao
