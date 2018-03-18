        program taylor

        implicit none

        ! Calcular o cosseno de x real pela série de Taylor
        ! cos x = 1 - x^2/2! + x^4/4! - x^6/6! + ...

        integer i, imax
        real*8 x,inc,res,fac, eps

        parameter (imax = 50)
        parameter (eps = 1e-6)

        do
            read(*,*,end=20) x

            i = 1
            fac = 1.d0
            res = 0.d0
            inc = 1.d0
            do while (abs(inc) >= eps .and. i <= imax)
                res = res + inc
                fac = fac*dfloat(2*i)*dfloat(2*i-1)
                inc = (-1)**i * x**(2*i)/(fac)
                !write(*,*) i, fac, inc, res
                i = i+1
            enddo

            write(*,*) x, res, abs(inc), i-1
        end do

20      end program taylor
