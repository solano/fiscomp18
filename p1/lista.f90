        program lista
        implicit none

        real*8, dimension(:), allocatable :: nums
        real*8 xmin, xmax
        integer n, m, i, j, k

        read(*,*) n,m
        allocate(nums(n))

        do i=1,n
            read(*,*) nums(i)
        end do

        ! Encontrar mínimo e máximo valores da lista
        xmin = nums(1)
        xmax = nums(1)
        do i=1,n
            if (nums(i) <= xmin) then
                xmin = nums(i)
                k = i
            end if
            if (nums(i) >= xmax) then
                xmax = nums(i)
            end if
        end do

        ! Percorrer a lista m vezes. Em cada iteração, fazer k = índice do
        ! menor valor encontrado. Imprimir tal valor, e alterá-lo para xmax.
        do j=1,m
            do i=1,n
                if(nums(i) < xmin) then
                    xmin = nums(i)
                    k = i
                end if
            end do
            write(*,*) nums(k)
            nums(k) = xmax
            xmin = xmax
        end do

        end program lista
