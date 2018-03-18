program stirling

implicit none

integer i
real*8 lf,st,pi

pi = 4*atan(1.0d0)
lf = 0.0d0

open(10,file='stirling-c.dat')

do i=2,30
	lf = lf + log(dfloat(i))
	st = i*log(dfloat(i)) - i + log(2*pi*i)/2
	write(10,*) i, lf, st, (lf-st)/lf
enddo

close(10)

end program stirling
