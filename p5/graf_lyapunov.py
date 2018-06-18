from problema1 import lyapunov
import numpy as np
import matplotlib.pyplot as plt

lx0 = [0.05, 0.15, 0.5, 0.75, 0.95]
eps = 1e-3
n = 1
r = 2.5

# np.log(abs(2-r))
#
#
# # for x0 in lx0:
# #     print(f'x0 = {x0}, lambda = {lyapunov(n,r,x0)}')
#
# r,x0 = 2.5,0.8
# for n in range(1,6):
#     print(f'{lyapunov(n,r,x0)}  {pylyapunov(n,r,x0)}')

#%%

plt.figure(dpi=300,figsize=(9,3))
x = np.linspace(0.01,.99,10000)
# for n in range(90000,100000,5000):
    # plt.plot(x, lyapunov(n,2.5,x))
plt.plot(x, lyapunov(1e3,2.5,x), '--k', linewidth=0.8,
    label='n = $1\\times10^3$')
plt.plot(x, lyapunov(100e3,2.5,x), '-k', linewidth=0.8,
    label='n = $100\\times10^3$')
plt.ylim(-.71,-.68)
plt.xlim(0,1)
plt.xlabel('Valor inicial $x_1$')
plt.ylabel('Coeficiente $\\lambda^*_n$')
plt.title('Expoente de Lyapunov analítico, $r=2.5$')
plt.legend(loc='lower right')
plt.savefig('p5/fig/lyapunov-analitico.png',
    bbox_inches='tight')

#%%
x = np.linspace(0.01,.99,10000)
for n in [100e3]:
    aaa = lyapunov(n,2.5,x)
    aaa = np.extract(np.isfinite(aaa),aaa)
    print('n = %d, lambda = %.10f +- %.50f' \
           %(n,aaa.mean(),aaa.std()))
