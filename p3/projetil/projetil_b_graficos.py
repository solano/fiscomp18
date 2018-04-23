import numpy as np
import matplotlib.pyplot as plt

dados = [np.loadtxt('p3/projetil/projetil_b_%d.dat'%i).T \
                    for i in (30,40,45,50,60)]
# cada dado é: tempo, vx, vy, x, y
# vamos plotar as trajetórias, então só importam x e y
x = [l[3] for l in dados]
y = [l[4] for l in dados]

plt.figure(dpi=500)
plt.plot(x[0],y[0],'-.k',   label='30°')
plt.plot(x[1],y[1],'--k',  label='40°')
plt.plot(x[2],y[2],'-k',  label='45°',zorder=1)
plt.plot(x[3],y[3],':k',   label='50°')
plt.plot(x[4],y[4],'gray',label='60°',zorder=0)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.ylim(0,12000)
plt.xlim(0,25000)
plt.title('Trajetória do projétil (com resistência do ar)')
plt.legend()
plt.savefig('p3/projetil/projetil_b_trajetorias.png',bbox_inches='tight')

# alcance em função do ângulo

alcance = np.loadtxt('p3/projetil/projetil_b_alcance.dat').T
i_max = np.argmax(alcance[1])
ang_max = alcance[0,i_max]
alcance_max = alcance[1,i_max]
print('ângulo de alcance máximo:',ang_max)
print('alcance máximo',alcance_max)

plt.figure(dpi=500)
plt.plot(alcance[0],alcance[1],'k')
plt.grid()
plt.ylim(min(alcance[1]),23000)
plt.xlim(30,60)
plt.xlabel('Ângulo (graus)')
plt.ylabel('Alcance (m)')
plt.title('Alcance do projétil (com resistência do ar)')
plt.savefig('p3/projetil/projetil_b_alcance.png',bbox_inches='tight')
