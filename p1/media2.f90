        program media
        implicit none

        integer n
        real*8 med, med2, dp, x
        
        open(10,file='media.in',status='old')

        n = 0
        med = 0.d0
        med2 = 0.d0

        do
            read(10,*,end=10) x
            med = med + x
            med2 = med2 + x**2
            n = n+1
        end do

10      if (n > 0) then
            med = med/dfloat(n)
            med2 = med2/dfloat(n)
            dp = sqrt(med2-med**2)
        else
            goto 30
        end if

        write(*,*) med, dp

30      end program media
