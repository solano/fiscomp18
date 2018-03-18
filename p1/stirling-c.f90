        program stirling
        implicit none

        integer i
        real*8 lf,st,pi

        parameter(pi = 4*atan(1.0d0))

        lf = 0.0d0
        do i=2,30
            lf = lf + log(dfloat(i))
            st = i*log(dfloat(i)) - i + log(2*pi*i)/2
            write(*,*) i, lf, st, (lf-st)/lf
        end do
        i = 1000000
        st = i*log(dfloat(i)) - i + log(2*pi*i)/2
        write(*,*) i, st

        end program stirling
