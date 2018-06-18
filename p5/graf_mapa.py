import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from problema1 import mapa

# %%
# matplotlib.style.use('fast')
matplotlib.style.use('default')
# lr = [1,2,3,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4]
# lr = np.linspace(3,4,100)
lr = [1,2,2.5]
lx0 = [.2,.5,.9]

N = 1000
eps = 1e-3
previsto = lambda r: 1-1/r
conv = [mapa(N,r,0.9)-previsto(r) for r in lr]
for r,c in zip(lr,conv):
    first = N
    for i in range(N-1,-1,-1):
        if abs(c[i]) > eps: break
        first = i
    print(f'r = {r}, first = {first}')

#%%

for r in lr:
    # N = int((r-0.5)*300)
    N = 30
    xi = np.arange(1,N+1)
    plt.figure(dpi=300,figsize=(4.5,3))
    for x0 in lx0:
        yi = mapa(N,r,x0)
        plt.plot(xi, yi,'.',markersize=4.9,label=f'$x_0$ = {x0}')
    plt.title(f'r = {r}, ponto fixo = {previsto(r)}')
    plt.ylim(0,1)
    plt.xlabel('i')
    # plt.legend()
    plt.ylabel('$x_i$')
    # plt.annotate(f'Previsto: {previsto(r)}',(80,yi[-1]+0.05))
    plt.savefig(f'p5/fig/mapa-iter-r={r}.png', bbox_inches='tight')
