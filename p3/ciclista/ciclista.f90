        program ciclista
        implicit none

        real*8 v0, vi, vn, xi, xn
        real*8 m, P, dt, rho, A
        integer i, imax

        parameter (v0 = 4.d0)
        parameter (m = 70.d0)
        parameter (P = 400.d0)
        parameter (dt = 0.1d0)
        parameter (imax = 3000) ! 300 segundos / dt

        read(*,*) rho, A

        vi = v0
        xi = 0
        do i=0,imax
            write(*,*) i*dt, vi, xi

            vn = vi + (P/(m*vi) - rho*A*vi*vi/(2.d0*m))*dt
            xi = xi + 0.5d0*(vi+vn)*dt

            vi = vn
        end do

        end program ciclista
