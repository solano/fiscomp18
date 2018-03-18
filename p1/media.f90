        program media
        implicit none

        integer n
        real*8 med, dp, x
        
        open(10,file='media.in',status='old')

        n = 0
        med = 0.d0
        dp = 0.d0

        do
            read(10,*,end=10) x
            med = med + x
            n = n+1
        end do

10      if (n > 0) then
            med = med/dfloat(n)
        else
            goto 30
        end if

        !ler media.in novamente, para calcular o desvio padrão
        close(10)
        open(10,file='media.in',status='old',position='rewind')
        do
            read(10,*,end=20) x
            dp = dp + (x-med)**2
        end do

20      dp = sqrt(dp/dfloat(n))
        write(*,*) med, dp

30      end program media
