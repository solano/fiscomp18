        program ciclista_b
        implicit none

        real*8 v0, vi, x       ! inicial, v_i
        real*8 m, P, dt, rho, A
        integer i, imax

        parameter (v0 = 4.d0)
        parameter (m = 70.d0)
        parameter (P = 400.d0)
        parameter (rho = 1.3)
        parameter (A = 0.333)
        parameter (dt = 0.1d0)
        parameter (imax = 3000) ! 300 segundos / dt

        vi = v0
        x = 0
        do i=0,imax
            write(*,*) i*dt, vi, x

            if (i==0 .or. i==imax) then
                x = x + 0.5d0*vi*dt
            else
                x = x + vi*dt
            end if

            vi = vi + (P/(m*vi) - rho*A*vi*vi/(2.d0*m))*dt
        end do

        end program ciclista_b
