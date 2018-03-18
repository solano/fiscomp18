        program stirling

        implicit none

        integer i
        real*8 f

        f = 1.0d0
        do i=1,20
            f = f*dfloat(i)
            write(*,*)i,f
        enddo

        end program stirling
