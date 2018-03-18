        program autovalor
        implicit none

        real*8, dimension(:,:), allocatable :: A
        real*8, dimension(:), allocatable :: x,y ! xk, xk+1
        real*8 sigma, eps, lambda, lambda2, soma, norma, prod, normay, prec_x
        integer i,j,k,n,kmax

        parameter (eps = 1e-8) ! tolerância do erro do autovalor
        parameter (kmax = 50)  ! número máximo de iterações

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
            ! Normalizar xk+1
            normay = norma(y,n)
            do i=1,n
                y(i) = y(i)/normay
            end do
            prec_x = norma(x-y,n)

            k = k+1
            x = y
            
            call multmv(y,A,x,n)
            lambda2 = prod(x,y,n)
            sigma = abs(lambda2 - lambda)
            lambda = lambda2
        end do
        
        write(*,*) 'autovalor,sigma,prec_x=', lambda,sigma,prec_x

        end program autovalor

        ! Norma l2
        function norma(x,n)
            real*8 x(n)
            integer i
            real*8 norma
            norma = 0
            do i=1,n
                norma = norma + x(i)**2
            end do
            norma = sqrt(norma)
            return
        end function
        
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
