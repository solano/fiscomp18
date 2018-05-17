        program n_corpos
        implicit none

!       Resolve o problema de n corpos de massas iguais.
!       n é dado na primeira linha da entrada, junto com dt e tmax.
!       Nas n linhas seguintes, são dadas posições e velocidades
!       iniciais (x,y,vx,vy).
!       Considera-se GM = 1.

        real*8, dimension(:), allocatable :: x,y,vx,vy
        real*8, dimension(:,:), allocatable :: r
        real*8 dt, tmax, pi, GM
        integer i,j,k,n

        read(*,*) n, dt, tmax
        allocate(x(n),y(n),vx(n),vy(n))
        allocate(r(n,n))

        do i=1,n
            read(*,*) x(i),y(i),vx(i),vy(i)
        end do
        pi = 4*atan(1d0)
        GM = 1
        k=0
        do while (k*dt < tmax)
            do i=1,n
                do j=1,i
                    r(i,j) = sqrt((x(i)-x(j))**2 + &
                            (y(i)-y(j))**2)
                    r(j,i) = r(i,j)
                end do
            end do

            do i=1,n
                do j=1,n
                    if (i /= j) then
                        vx(i) = vx(i) &
                            - dt*GM*(x(i)-x(j))/abs(r(i,j))**3
                        vy(i) = vy(i) &
                            - dt*GM*(y(i)-y(j))/abs(r(i,j))**3
                    end if
                end do
                x(i) = x(i) + vx(i)*dt
                y(i) = y(i) + vy(i)*dt
                write(*,*) i,k*dt, x(i),y(i),vx(i),vy(i)
            end do

            k = k+1
        end do

        end program n_corpos
