        program ciclista_a
        implicit none

        real*8 v0, vi, x       ! inicial, v_i
        real*8 m, P, dt
        integer i, imax

        parameter (v0 = 4.d0)
        parameter (m = 70.d0)
        parameter (P = 400.d0)
        parameter (dt = 0.1d0)
        parameter (imax = 3000) ! 300 segundos / dt

        vi = v0
        x = 0
        do i=0,imax
            write(*,*) i*dt, vi, x

            if (i==0 .or. i==imax) then
                x = x+0.5d0*vi*dt
            else
                x = x + vi*dt
            end if

            vi = vi + (P/(m*vi))*dt
        end do

        end program ciclista_a
