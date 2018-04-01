import numpy as np
import matplotlib.pyplot as plt

dados = np.loadtxt('p2/raiz-t.dat')
T, m = dados.T

plt.figure(dpi=500)
plt.plot(T,m)
plt.axis([0,1,0,1.1])
plt.xlabel('Temperatura $T$')
plt.ylabel('Raiz $m$ da equação')
plt.savefig('p2/raiz-t.png',bbox_inches='tight')
