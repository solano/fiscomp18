        program newton
        implicit none

        integer i, nmax
        real*8 a,x0,eps,x,delx,func,dfunc

        read(*,*) a,x0
        read(*,*) eps,nmax

        i=1
        delx = 1000
        do while (delx >= eps)
            x = x0 - (x0**2-a)/(2.d0*x0)
            delx = abs(x-x0)
            i = i+1
            x0 = x
            write(*,*) x, delx, i
        end do


        end program newton
