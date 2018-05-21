import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10,10),dpi=300)
for fnome in ['terra_jupiter1.dat','terra_jupiter1000.dat',
            'terra_jupiter1000alt.dat']:
    dados = np.loadtxt('p4/dados/'+fnome).T
    t,x,y,r = dados[0],dados[1],dados[2],dados[-1]

    plt.plot(x,y)

    # plt.figure(figsize=(10,5))
    # plt.plot(t,r-1)
    # plt.xlabel('Tempo (anos)')
    # plt.xlim(0,25)
    # plt.ylabel(r'$\Delta r$ (UA)')
plt.axes().set_aspect('equal','datalim')
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.xlabel('x (UA)')
plt.ylabel('y (UA)')
plt.title('Órbita da Terra perturbada por Júpiter')
plt.savefig('p4/fig/terra_jupiter.png',bbox_inches='tight')
