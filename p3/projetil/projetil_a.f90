        program projetil_a
        implicit none

        real*8 xi,yi,vxi,vyi
        real*8 g, theta, dt
        integer i,imax
        logical traj     ! escrever trajetoria?

        parameter (g=9.8)
        parameter (dt=0.01)
        parameter (imax = 10000000)
        
        traj = iargc()>0

        do
            read(*,*,end=10) theta

            xi = 0
            yi = 0
            vxi = 700*cos(theta*(2.d0*atan(1.d0)/90.d0))
            vyi = 700*sin(theta*(2.d0*atan(1.d0)/90.d0))

            i=0
            do while(yi>=0 .and. i<=imax)
                if (traj) then
                    write(*,*) i*dt, vxi, vyi, xi, yi
                end if
                
                xi = xi + vxi*dt
                yi = yi + vyi*dt
                vyi = vyi - g*dt

                i = i+1
            end do

            if (.not. traj) then
                write(*,*) theta, xi  ! angulo, alcance
            end if
        end do
                
10      end program projetil_a
