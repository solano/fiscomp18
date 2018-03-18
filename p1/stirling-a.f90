program stirling

implicit none

integer i
real*8 f

f = 1.0d0

open(10,file='stirling-a.dat')
do i=1,20
	f = f*dfloat(i)
	write(10,*)i,f
enddo
close(10)

end program stirling
