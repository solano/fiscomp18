        program planetas
        implicit none

        real*8 x,y,vx,vy
        real*8 r, a, e
        real*8 dt, tmax, GM, pi
        integer i

        pi = 4d0*atan(1d0)
        GM = 4d0*pi*pi

        read(*,*) tmax, dt, a, e
        x = (1+e)*a
        vy = sqrt(GM*(1-e)/(a*(1+e)))
        y = 0
        vx = 0

        do while (i*dt <= tmax)
            write(*,*) i*dt, x, y, vx, vy

            r = dsqrt(x*x+y*y)
            
            vx = vx - GM*x*dt/(r**3)
            x = x + vx*dt
            vy = vy - GM*y*dt/(r**3)
            y = y + vy*dt

            i = i+1
        end do

        end program planetas
