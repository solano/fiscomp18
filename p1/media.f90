        program media
        implicit none

        integer i, n
        real*8 med, medquad, dp1, dp2
        real*8, dimension(:), allocatable :: x

        read(*,*) n    ! ler tamanho da lista
        allocate(x(n)) ! alocar memória

        med = 0.d0
        medquad = 0.d0
        dp1 = 0.d0
        dp2 = 0.d0

        do i=1,n
            read(*,*) x(i)
            med = med + x(i)
            medquad = medquad + x(i)**2
        end do
        med = med/dfloat(n)
        medquad = medquad/dfloat(n)

        do i=1,n
            dp1 = dp1 + (x(i)-med)**2
        end do
        dp1 = sqrt(dp1/n)
        dp2 = sqrt(medquad - med**2)

        write(*,*) n, med, dp1, dp2

        end program media
