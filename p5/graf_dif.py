import numpy as np
import matplotlib.pyplot as plt
from problema1 import dif
from numpy import sqrt
from scipy.stats import linregress

lx0 = [0.05, 0.15, 0.5, 0.75, 0.95]
# lx0 = np.linspace(0.01,0.99,10000)
eps = 1e-3
imax = 20
imin = 5
r = 2.5

# lyap = []
for x0 in lx0:
    plt.figure(figsize=(4.5,3),dpi=300)
    x = np.arange(1,imax+1)
    y = dif(imax,r,x0,eps)

    plt.semilogy(x,y,'ok',markersize=2)
    plt.title('Diferença $|x_i - \\tilde{x}_i|$,'+f' com $x_1$ = {x0}')
    plt.savefig(f'p5/fig/dif-r=2,5-x0=0,{int(x0*100)}.png',
        bbox_inches='tight')

        # isso vai produzir um arquivo terminando em x0=0,5 que na
        # verdade corresponde a x0 = 0.05. Não tô com saco pra corrigir

    x = x[imin:]
    y = np.log(y[imin:])
    slope, intercept, rrrrr, prob2, see = linregress(x, y)
    mx = x.mean()
    sx2 = ((x-mx)**2).sum()
    sd_intercept = see * sqrt(1./len(x) + mx*mx/sx2)
    sd_slope = see * sqrt(1./sx2)
    print(f'x0 = {x0}, slope = {slope} +- {sd_slope}')
    # lyap.append(slope)

# # %%
#
# # lyap = np.array(lyap)
# # llll = lyap.mean()
# # sdll = lyap.std()
# # print(llll)
# # print(sdll)
# plt.figure(dpi=300,figsize=(9,3))
# plt.plot(lx0,lyap,'.k',markersize=.8)
# plt.ylim(-.71,-.68)
# plt.xlim(0,1)
# plt.xlabel('Valor inicial $x_1$')
# plt.ylabel(r'Coeficiente $\lambda$ (regressão)')
# plt.title('Expoente de Lyapunov estimado, $r=2.5$')
# plt.savefig('p5/fig/lyapunov.png',bbox_inches='tight')
