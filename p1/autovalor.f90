        program autovalor
        implicit none

        real*8, dimension(:,:), allocatable :: A
        real*8, dimension(:), allocatable :: x,y ! xk, xk+1
        real*8 sigma, eps, lambda, lambda2, prec_x, prod
        integer i,j,k,n,kmax

        parameter (eps = 1.d-8) ! tolerância do erro do autovalor
        parameter (kmax = 60)  ! número máximo de iterações

        read(*,*) n
        allocate(A(n,n))
        allocate(x(n))
        allocate(y(n))

        ! Ler matriz
        do i=1,n
            read(*,*) ( A(i,j), j=1,n )
        end do

        ! Chutar vetor x0 = (1,1,...,1)/sqrt(n)
        do i=1,n
            x(i) = 1/sqrt(float(n))
        end do

        ! x1 = A x0
        call multmv(y,A,x,n)

        lambda = prod(x,y,n)
        k = 0

        !!!!!! LOOP !!!!!!
        sigma = 10 ! qualquer coisa maior que eps para começar
        do while(k <= kmax .and. sigma >= eps)
            ! Norma induzida pelo produto interno
            y = y/sqrt(prod(y,y,n))
            if (lambda < 0) then
                prec_x = sqrt(prod(x+y,x+y,n))
            else
                prec_x = sqrt(prod(x-y,x-y,n))
            end if

            k = k+1
            x = y

            call multmv(y,A,x,n)
            lambda2 = prod(x,y,n)
            sigma = abs(lambda2 - lambda)
            lambda = lambda2
        end do

        write(*,*) lambda, sigma, prec_x

        end program autovalor

        ! Produto interno
        function prod(x,y,n)
            real*8 prod
            real*8 x(n), y(n)
            integer i
            prod=0
            do i=1,n
                prod = prod + x(i)*y(i)
            end do
            return
        end function

        ! Multiplica matriz A por vetor x e põe o resultado em y
        subroutine multmv(y,A,x,n)
            real*8 A(n,n), y(n), x(n), soma
            do i=1,n
                soma = 0
                do j=1,n
                    soma = soma + A(i,j)*x(j)
                end do
                y(i) = soma
            end do
            return
        end subroutine
