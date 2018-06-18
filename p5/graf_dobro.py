import numpy as np
import matplotlib.pyplot as plt
from problema2 import mapa

r = -1.55
x0 = 0.05
N = 145

# N = int((r-0.5)*300)
xi = np.arange(1,N+1)
plt.figure(dpi=300,figsize=(4.5,3))
# for x0 in lx0:
yi = mapa(N,r,x0)
plt.plot(xi, yi,'.-k',
markersize=4.9,linewidth=1,
label=f'$x_0$ = {x0}')
# plt.ylim(0,1)
plt.xlabel('i')
# plt.legend()
plt.title(r'Mapa logístico com $r=3.2$, $x_1 = 0.05$')
plt.ylabel('$x_i$')
plt.show()
# plt.savefig('p5/fig/mapa-dobro.png',bbox_inches='tight')

#%%
N = 37
# print(f'\n N = {N}')
xi = np.arange(1,N+1)
yi = mapa(N,r,x0)
print(*yi[-2:],sep='\n')
a = 1+r
b = np.sqrt(-3-2*r+r*r)
print((a-b)/(2*r), (a+b)/(2*r), sep='\n')
