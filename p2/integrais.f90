        program integrais
        implicit none

        real*8 a,b,h,x,f,primitiva
        real*8 intt,errot, ints,erros, intexato
        integer i,n

        parameter(a=0.d0)
        parameter(b=1.d0)

        intexato = primitiva(b)-primitiva(a)

        do
            read(*,*,end=10) n
            h = (b-a)/n

            ! Método do trapézio
            intt = (f(a)+f(b))/2.d0
            do i=1,n-1
                intt = intt+f(a+real(i,8)*h)
            end do
            intt = intt*h
            errot = abs(intt-intexato)

            ! Método de Simpson
            ints = f(a)+f(b)
            do i=1,n-1
                if (mod(i,2)==1) then
                    ints = ints + f(a+real(i,8)*h)*4.d0
                else
                    ints = ints + f(a+real(i,8)*h)*2.d0
                end if
            end do
            ints = ints*h/3.d0
            erros = abs(ints-intexato)

            !write(*,*) intt, ints
            write(*,*) h, errot, erros
            !write(*,*) log10(h),log10(errot),log10(erros)

        end do

10      end program integrais

        real*8 function f(x)
            real*8 x
            f = exp(2.d0*x)*sin(x)
            return
        end

        real*8 function primitiva(x)
            real*8 x
            primitiva = -exp(2.d0*x)*(cos(x)-2.d0*sin(x))/5.d0
            return
        end
