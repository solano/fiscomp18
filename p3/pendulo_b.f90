        program pendulo_b
        implicit none

        real*8 omega_i, theta_i
        real*8 omega_n, theta_n
        real*8 E, g, L, m, theta_0, dt, tmax
        integer i

        parameter (g=10)
        parameter (L=1)
        parameter (m=1)
        parameter (theta_0=atan(1d0/sqrt(3d0)))
        parameter (tmax=20)
        parameter (dt=5d-3)

        omega_i = 0
        theta_i = theta_0
        i=0
        do while (i*dt <= tmax)
            E = m*(L**2)*(omega_i**2)/2d0 + &
                m*g*L*(1-cos(theta_i))
            write(*,*) i*dt, theta_i, omega_i, E
            omega_n = omega_i - g*sin(theta_i)*dt/L
            theta_n = theta_i + omega_n*dt
            omega_i = omega_n
            theta_i = theta_n
            i = i+1
        end do

        end program pendulo_b
