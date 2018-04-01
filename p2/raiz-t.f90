        program raizt
        implicit none

        real*8 a,b,m,erro,f
        real*8 eps, T
        integer i,n

        parameter (eps=1.d-12)
        parameter (n=100)

        do i=1,n
            T = dfloat(i)/dfloat(n)
            a = 1.d-5
            b = 1-a
            erro = 10
            do while (erro >= eps)
                m = (a+b)/2.d0
                f = m - tanh(m/T)
                if (f>0) then
                    b = m
                else if (f < 0) then
                    a = m
                else
                    a = m
                    b = m
                end if

                erro = (b-a)/2.d0
            end do
            write(*,*) T, m
        end do

        end program raizt
