        program stirling
        implicit none

        integer i
        real*8 lf

        lf=0.0d0
        do i=2,30
            lf = lf + log(dfloat(i))
            write(*,*) i,lf,ceiling(lf/log(2.d0))
        enddo

        end program stirling
