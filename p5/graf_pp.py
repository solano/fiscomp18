import numpy as np
import matplotlib.pyplot as plt
from problema3 import pp

a = 2/3
b = 4/3
c = 1
d = 1

#%%
# plt.figure(dpi=300)
# for x1,y1 in [(1.,.1),(.1,.4),(.2,.3),(.1,.05),(1,1),(1.1,0.5)]:
for x1,y1 in [(1.,.1),(.1,.4),(.2,.3),(.1,.05),(1,1),(1.1,0.5)]:
    t = 2000
    dt = 1e-2
    N = int(t/dt)
    i = int(y1*100)
    x,y = pp(N,dt,a,b,c,d,x1,y1)
    plt.figure(dpi=300)
    plt.plot(np.arange(N)*dt, x,'-k', label='Presas')
    plt.plot(np.arange(N)*dt, y,'--k', label='Predadores')
    plt.title(f'$x_1$ = {x1}, $y_1$ = {y1}')
    plt.legend()
    plt.savefig(f'p5/fig/pp{i}.png',bbox_inches='tight')

#     plt.plot(x,y)
#     plt.xlabel('x')
#     plt.ylabel('y')
# plt.title('Espaço de fase')
# plt.savefig('p5/fig/pp_fase.png',bbox_inches='tight')
