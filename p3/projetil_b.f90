        program projetil_b
        implicit none

        real*8 xi,yi,vxi,vyi,vi
        real*8 xn,yn,vxn,vyn
        real*8 g, theta, lambda, dt
        integer i,imax
        logical traj     ! escrever trajetoria?

        parameter (g=9.8)
        parameter (lambda = 4.d-5)
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
                
                vi = dsqrt(vxi*vxi + vyi*vyi)
                xn = xi + vxi*dt
                yn = yi + vyi*dt
                vxn = vxi - lambda*vi*vxi*dt
                vyn = vyi - g*dt - lambda*vi*vyi*dt

                i = i+1

                vxi = vxn
                vyi = vyn
                xi = xn
                yi = yn
            end do

            if (.not. traj) then
                write(*,*) theta, xi  ! angulo, alcance
            end if
        end do
                
10      end program projetil_b
