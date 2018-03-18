program stirling

implicit none

integer i
real*8 lf

lf=0.0d0

open(10,file='stirling-b.dat')

do i=2,30
	lf = lf + log(dfloat(i))
	write(10,*) i,lf
enddo

close(10)

end program stirling
