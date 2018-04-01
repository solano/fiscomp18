import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

dados = np.loadtxt('p2/integrais.dat')
h, trap, simp = tuple(dados.T)

# imprimir pro latex
#tab = open('p2/tab-integrais','w')
#for i in dados: tab.write("{:e} & {:e} & {:e} \\\\\n".format(*i))

# regressão linear
print("trapézio:", stats.linregress(np.log(h),np.log(trap)))
simplim = np.argmin(simp)
print("simpson:", stats.linregress(np.log(h[:simplim]),np.log(simp[:simplim])))

# gráfico
#plt.figure(figsize=(8,5),dpi=500)
#plt.loglog(h,trap,h,simp)
#plt.legend(['Método do trapézio','Método de Simpson'])
#plt.xlabel('Precisão $h$')
#plt.ylabel('Erro cometido na aproximação')
#plt.savefig('p2/integrais.png',bbox_inches='tight')
