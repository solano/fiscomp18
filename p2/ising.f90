        program ising
        implicit none

        real*8 x
        integer i

        x = -1
        do i=1,51
            write(*,*) x, x, tanh(x/0.8), tanh(x/1.2)
            x = x+0.04
        end do

        end program ising
