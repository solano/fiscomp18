program expserie

implicit none

integer i,n
real*8 x,esum,ei,ef

	open(10,file='expserie.in')
	read(10,*)x,n
	close(10)

	open(20,file='expserie.dat')
	esum = 1.0d0
	ef = 1.0d0
! laço
	do i=1,n
		ef = ef*i
		ei = (x**i)/ef
		esum = esum + ei
		write(20,*)i,esum,ei
	enddo

	write(20,*)n+1,exp(x)

	close(20)

end program
