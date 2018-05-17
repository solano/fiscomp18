        program sat_lua
        implicit none

        real*8 x,y,vx,vy,xl,yl
        real*8 rst,rsl,rl,tl, dphi,dr,rgeo
        real*8 dt, tmax, GMt, GMl, pi
        integer i

        pi = 4d0*atan(1d0)
        GMt = 6.6743e-11*5.9736e24
        GMl = GMt*1.23e-2
        rl = 384400e3   
        tl = 27.32*86400
        rgeo = 42244e3

        !read(*,*) tmax, dt, a, e
        !x = (1+e)*a
        !vy = sqrt(GM*(1-e)/(a*(1+e)))
        tmax = 100*86400
        read(*,*) dt  ! leitura em segundos
        x = rgeo
        vy = sqrt(GMt/x)
        y=0; vx=0; dphi=0; dr=0
        i=0
        do while (i*dt <= tmax)
            xl = rl*cos(2*pi*i*dt/tl)
            yl = rl*sin(2*pi*i*dt/tl)
            rst = dsqrt(x*x+y*y)
            rsl = dsqrt((x-xl)**2 + (y-yl)**2)

            dphi = atan2(y,x) - 2*pi*i*dt/86400
            do while (dphi<0)
                dphi = dphi+2*pi
            end do
            dr = rst-rgeo

            write(*,*) i*dt/86400, x, y, vx, vy, dphi, dr
            
            vx = vx - GMt*x*dt/(rst**3) - GMl*(x-xl)*dt/(rl**3)
            x = x + vx*dt
            vy = vy - GMt*y*dt/(rst**3) - GMl*(y-yl)*dt/(rl**3)
            y = y + vy*dt

            i = i+1
        end do

        end program sat_lua
