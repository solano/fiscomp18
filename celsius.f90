program celsius2fahrenheit

implicit none ! nenhuma variável declarada ?implicitamente?

real*8 tc,tf

write(*,*)"Temperatura em Celsius: "
read(*,*)tc

if (tc >= -273.15d0) then
	tf = 9.0d0*tc/5.0d0 + 32.0d0

	write(*,*)"Em Fahrenheit:"
	write(*,*) tf

else
	write(*,*)"Inválido, menor que o zero absoluto!"
endif

end program celsius2fahrenheit
