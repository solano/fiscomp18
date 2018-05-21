        program kepler
        implicit none

        real*8 x,y,vx,vy,r
        real*8 y_temp, t_per
        real*8 periodo, a
        real*8 dt, GM, pi
        integer i,p,n_orbitas

        pi = 4d0*atan(1d0)
        GM = 4d0*pi*pi
        n_orbitas = 20

        do
            read(*,*,end=10) dt,a
            vx = 0
            y = 0
            x = a
            vy = 2*pi/dsqrt(a) ! em unidades astronômicas

            p = -1
            i=0
            do while (p < 2*n_orbitas)
                r = dsqrt(x*x+y*y)
                vx = vx - GM*x*dt/(r**3)
                x = x + vx*dt
                vy = vy - GM*y*dt/(r**3)
                y_temp = y + vy*dt

                if (y==0 .or. y_temp/y<0) then
                    t_per = i*dt
                    p = p+1
                end if

                y = y_temp
                i = i+1
            end do

            periodo = t_per*2/dfloat(p)
            write(*,*) a, periodo, periodo**2/a**3
        end do

10      end program kepler
