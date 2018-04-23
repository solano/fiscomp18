import numpy as np
import matplotlib.pyplot as plt

dados = np.loadtxt('p3/pendulo/pendulo_b.dat').T
t,theta,omega,E = dados

plt.figure(dpi=500,figsize=(10,4))
plt.plot(t,theta,'k',label='Ângulo',zorder=1)
plt.plot(t,0*t,'gray',zorder=0)
plt.plot(t,theta,'--k',label='Velocidade angular') # só pra aparecer na legenda
plt.xlim(0,20)
plt.ylim(-1,1)
plt.title('Movimento do pêndulo (método de Euler-Cromer)')
plt.xlabel('Tempo (s)')
plt.ylabel('Ângulo com a vertical (rad)')
plt.legend()
plt.twinx()
plt.ylim(-3,3)
plt.ylabel('Velocidade angular (rad/s)',zorder=2)
plt.plot(t,omega,'--k')
plt.savefig('p3/pendulo/pendulo_b_movimento.png',bbox_inches='tight')

plt.figure(dpi=500,figsize=(10,3))
plt.plot(t,E,'k')
plt.title('Energia mecânica (método de Euler-Cromer)')
plt.xlim(0,20)
plt.ylim(0,4)
plt.grid()
plt.xlabel('Tempo (s)')
plt.ylabel('Energia (J)')
plt.savefig('p3/pendulo/pendulo_b_energia.png',bbox_inches='tight')
