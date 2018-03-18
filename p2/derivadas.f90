        program derivadas
        implicit none

        real*8 x,h,f,f1,f2,ff1,ft1,f3s1,f3s2
        real*8 fx, fx1, fx2
        real*8 eff1, eft1, ef3s1, ef3s2

        x = 1.d0

        do
            read(*,*,end=10) h
            
            ! função e derivadas exatas
            fx = f(x)
            fx1 = f1(x)
            fx2 = f2(x)
            
            ! calcular derivada para frente de 2 pontos
            ff1 = (f(x+h)-fx)/h
            eff1 = abs(ff1-fx1)
    
            ! derivada para trás de 2 pontos
            ft1 = (fx-f(x-h))/h
            eft1 = abs(ft1-fx1)

            ! derivada simétrica de 3 pontos
            f3s1 = (f(x+h)-f(x-h))/(2.d0*h)
            ef3s1 = abs(f3s1-fx1)

            ! derivada segunda simétrica de 3 pontos
            f3s2 = (f(x+h) - 2.d0*fx + f(x-h))/(h**2)
            ef3s2 = abs(f3s2 - fx2)

            write(*,*) log10(h),log10(eff1), &
                log10(eft1), log10(ef3s1),log10(ef3s2)

        end do

10      end program derivadas

        real*8 function f(x)
            real*8 x
            f = exp(2.d0*x)*cos(x/4.d0)
            return
        end

        real*8 function f1(x)
            real*8 x
            f1 = 2.d0*exp(2.d0*x)*cos(x/4.d0) &
             - (exp(2.d0*x)*sin(x/4.0d0))/4.d0
            return
        end

        real*8 function f2(x)
            real*8 x
            f2 = 4.d0*exp(2.d0*x)*cos(x/4.d0) &
             - exp(2.d0*x)*sin(x/4.d0)/2.d0   &
             - exp(2.d0*x)*sin(x/4.0d0)/2.d0 &
             - exp(2.d0*x)*cos(x/4.d0)/16.d0
            return
            end
