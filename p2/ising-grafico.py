import matplotlib.pyplot as plt
import numpy as np

dados = np.loadtxt('p2/ising.dat')

x, y8, y12 = tuple(dados.T)

plt.figure(dpi=500)
plt.plot(x,y8,x,y12,x,0*x,'--k')
plt.axis([-1,1,-0.6,0.6])
plt.legend(['$\\tanh (x/0.8) - x$','$\\tanh(x/1.8) - x$'])
plt.savefig('p2/ising.png',bbox_inches='tight')
