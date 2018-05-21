        program terra_jupiter
        implicit none

        real*8 x,y,vx,vy,xj,yj
        real*8 rts,rtj,rj,tj
        real*8 dt, tmax, GMs, GMj, pi
        integer i

        pi = 4d0*atan(1d0)
        GMs = 4d0*pi*pi
        GMj = GMs*1.9e27/2.0e30

        rj = 5.20
        tj = 11.8578244

        !read(*,*) tmax, dt, a, e
        !x = (1+e)*a
        !vy = sqrt(GM*(1-e)/(a*(1+e)))
        tmax = 100
        dt = 0.001
        x = 1
        vy = 2*pi/sqrt(x)
        y = 0
        vx = 0

        do while (i*dt <= tmax)
            xj = rj*cos(2*pi*i*dt/tj)
            yj = rj*sin(2*pi*i*dt/tj)
            rts = dsqrt(x*x+y*y)
            rtj = dsqrt((x-xj)**2 + (y-yj)**2)

            write(*,*) i*dt, x, y, vx, vy, rts

            vx = vx - GMs*x*dt/(rts**3) - GMj*(x-xj)*dt/(rtj**3)
            x = x + vx*dt
            vy = vy - GMs*y*dt/(rts**3) - GMj*(y-yj)*dt/(rtj**3)
            y = y + vy*dt

            i = i+1
        end do

        end program terra_jupiter
