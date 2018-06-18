# plot do diagrama de bifurcação, aka a parte mais legal

import numpy as np
import matplotlib.pyplot as plt
from problema2 import mapa

########## Preparo dos dados
# %%

# # para o plot geral
# nultimos=15
# start=1
# finish=4

# # Para o plot detalhado
# Nultimos=30
# start = 3.5
# finish = 4

# # Para o plot experimental
# Nultimos=30
# start=-2
# finish=-1

# Para o plot no tkinter
Nultimos=30
start = 1
finish = 3.6

lr = np.linspace(start,finish,20000)

xi, lmapa = [], []
for r in lr:
    # N = int((r-0.5)*400)
    N = 1000

    lmapa.extend(mapa(N,r,0.5)[-Nultimos:])
    xi.extend(np.repeat(r,Nultimos))

# ########## Plot geral
# # %%
# plt.figure(dpi=300,figsize=(9,2.25))
# plt.plot(xi,lmapa,',k',markersize=0.03)
# plt.xlim(start,finish)
# plt.ylim(0,1)
# plt.savefig('p5/fig/diagrama-bifurc.png',bbox_inches='tight')
#
# ########## Plot detalhado
# #%%
# plt.figure(dpi=300,figsize=(9,9))
# plt.plot(xi,lmapa,',k',markersize=1)
# plt.xlim(start,finish)
# plt.ylim(0,1)
# plt.savefig('p5/fig/diagrama-birfuc-detal.png',bbox_inches='tight')
#
# ######### Plot experimental
# #%%
# plt.figure(dpi=300,figsize=(9,3))
# plt.plot(xi,lmapa,',k',markersize=1)
# plt.xlim(start,finish)
# plt.savefig('p5/fig/diagrama-birfuc-experimental-ignorar.png',bbox_inches='tight')

# plot no tkinter pra ver os pontos
plt.figure()
plt.plot(xi,lmapa,',k')
plt.show()
