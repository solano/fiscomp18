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

        xmin = nums(1)
        xmax = nums(1)
        do i=1,n
            if (nums(i) < xmin) then
                xmin = nums(i)
                k = i
            end if
            if (nums(i) > xmax) then
                xmax = nums(i)
            end if
        end do
        write(*,*) xmin, xmax

        !o algoritmo é percorrer a lista m vezes e pegar os valores mínimos
        !a cada rodada o k-ésimo é selecionado, printado e eliminado (fazendo
        !nums(k) = xmax)
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
