import numpy as np
import matplotlib.pyplot as plt
from problema1 import pontofixo

x = np.linspace(0,1,100)
# for fn in l:
plt.figure(dpi=300,figsize=(4.5,3))
plt.plot(x,x,'-k',alpha=0.5)
for r,fmt in [(1,'-k'),(2,'--k'),(2.5,'-.k')]:
    # x,y = np.loadtxt('p5/dados/'+fn).T
    y = pontofixo(r,x)
    plt.plot(x,y,fmt,label=f'r = {r}')

for a in [1,2,2.5]:
    a = 1-1/a
    plt.plot([a,a],[0,a],'--k',alpha=0.5)

plt.legend()
plt.xlim(0,1)
plt.ylim(0,1)
# plt.show()
plt.savefig('p5/fig/pontofixo.png',bbox_inches='tight')
