        program pendulo_c
        implicit none

        real*8 omega_i, theta_i, omega_n, theta_n
        real*8 g, L, m, theta_0, dt, tmax, t_u
        real*8 periodo1,a,b,func,du,integral,periodo2
        integer i,p,N

        parameter (g=10)
        parameter (L=1)
        parameter (m=1)
        parameter (tmax=20)
        parameter (dt=5d-3)

        do
        read(*,*,end=10) theta_0
        theta_0 = theta_0*2d0*atan(1d0)/90d0
 
        ! Cálculo do período por Euler-Cromer
        omega_i = 0
        theta_i = theta_0
        i=0
        p = -1
        t_u = 0
        do while (p <= 20 .and. i*dt<=tmax)
            omega_n = omega_i - g*sin(theta_i)*dt/L
            theta_n = theta_i + omega_n*dt
            
            if (omega_i==0 .or. omega_n/omega_i<0) then
                p = p+1
                t_u = i*dt
            end if

            omega_i = omega_n
            theta_i = theta_n
            i = i+1
        end do
        periodo1 = 2*t_u/dfloat(p)

        ! Cálculo do perído pela integral elíptica
        ! usando método de Simpson
        a = 0
        b = 2d0*atan(1d0)
        N = 2**12
        du = (b-a)/dfloat(N)
        integral = (func(a,theta_0)+func(b,theta_0))*du/3d0
        do i=1,N-1
            if (mod(i,2)==0) then
                integral = integral + &
                  2d0*func(a+i*du, theta_0)*du/3d0
            else
                integral = integral + &
                  4d0*func(a+i*du, theta_0)*du/3d0
            end if
        end do
        periodo2 = 4d0*sqrt(L/g)*integral

        write(*,*) theta_0*90d0/(2d0*atan(1d0)),periodo1,periodo2
        end do
10      end program pendulo_c

        function func(u,theta_0)
            real*8 func, u, theta_0
            func = 1d0/sqrt(1d0 - &
                (sin(theta_0/2d0)**2) * (sin(u))**2)
            return
        end function func


