import numpy as np
import matplotlib.pyplot as plt
from problema1 import dif
from numpy import sqrt
from scipy.stats import linregress

# lx0 = [0.75]
lx0 = np.linspace(0.01,0.99,10000)
eps = 1e-9
imax = 15
imin = 5
r = 3.8

lyap = []
ulyap = []
for x0 in lx0:
    # plt.figure(figsize=(4.5,3),dpi=300)
    x = np.arange(1,imax+1)
    y = dif(imax,r,x0,eps)

    # plt.semilogy(x,y,'ok',markersize=2)
    # plt.ylabel(r'$|x_i - \tilde{x}_i|$')
    # plt.xlabel('i')
    # plt.title(r'$r=3.8$, $x_1=0.75$, $\varepsilon=10^{-9}$')
    # plt.savefig(f'p5/fig/dif-caos.png',
    #     bbox_inches='tight')

    x = x[imin:]
    y = np.log(y[imin:])
    slope, intercept, rrrrr, prob2, see = linregress(x, y)
    mx = x.mean()
    sx2 = ((x-mx)**2).sum()
    sd_intercept = see * sqrt(1./len(x) + mx*mx/sx2)
    sd_slope = see * sqrt(1./sx2)
    # print(f'x0 = {x0}, slope = {slope} +- {sd_slope}')
    lyap.append(slope)
    ulyap.append(sd_slope)


# # %%
#
# lyap = np.array(lyap)
# llll = lyap.mean()
# sdll = lyap.std()
# print(llll)
# print(sdll)
# plt.figure(dpi=300,figsize=(9,3))
# plt.plot(lx0,lyap,'.k',markersize=.8)
# # plt.ylim(-.71,-.68)
# plt.xlim(0,1)
# plt.xlabel('Valor inicial $x_1$')
# plt.ylabel(r'Coeficiente $\lambda$ (regressão)')
# plt.title('Expoente de Lyapunov estimado, $r=3.8$')
# plt.savefig('p5/fig/lyapunov-caos.png',bbox_inches='tight')
#
# %%

plt.figure(dpi=300,figsize=(9,3))
plt.hist(lyap,100,color='grey')
plt.xlim(-1,1)
plt.title('Expoente de Lyapunov estimado, $r=3.8$')
plt.xlabel('$\\lambda$ (regressão)')
plt.ylabel('Frequência absoluta')
plt.savefig('p5/fig/lyapunov-caos-histograma.png',bbox_inches='tight')
