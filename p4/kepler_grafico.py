import numpy as np
import matplotlib.pyplot as plt

fdados = ['kep_mercurio1.dat','kep_venus1.dat','kep_terra1.dat',
    'kep_marte1.dat','kep_jupiter1.dat','kep_saturno1.dat',
    'kep_urano1.dat','kep_netuno1.dat'][::-1]
dados = [np.loadtxt('p4/dados/'+f).T for f in fdados]

plt.figure(figsize=(10,10),dpi=300)
for planeta in dados:
    x,y = planeta[1],planeta[2]
    plt.plot(x,y)
plt.axes().set_aspect('equal','datalim')
plt.xlabel('x (UA)')
plt.ylabel('y (UA)')
plt.title('Órbitas circulares (sistema solar)')
plt.savefig('p4/kepler_grafico.png',bbox_inches='tight')
