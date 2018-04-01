import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

dados = np.loadtxt('p2/derivadas.dat')

h, eff1, eft1, ef3s1, ef3s2 = tuple(dados.T)

# imprimir tabela pro latex
#tab = open('p2/tab-derivadas','w')
#for i in dados: tab.write("{:e} & {:e} & {:e} & {:e} & {:e} \\\\\n".format(*i))
#tab.close()

# regressão linear
print("para frente:", stats.linregress(np.log10(h),np.log10(eff1)))
print("para trás:", stats.linregress(np.log10(h),np.log10(eft1)))
simlim = np.argmin(ef3s1)
print("simétrica:", stats.linregress(np.log10(h[:simlim]),np.log10(ef3s1[:simlim])))
sim2lim = np.argmin(ef3s2)
print("segunda simétrica:", stats.linregress(np.log10(h[:sim2lim]),np.log10(ef3s2[:sim2lim])))

#plt.figure(figsize=(8,5),dpi=500)
#plt.loglog(h,eff1,h,eft1,h,ef3s1,h,ef3s2)
#plt.legend(['Derivada para frente','Derivada para trás', 'Derivada simétrica', 'Derivada segunda simétrica'])
#plt.xlabel('Precisão $h$')
#plt.ylabel('Erro cometido na aproximação')
#plt.savefig('p2/derivadas.png',bbox_inches='tight')
