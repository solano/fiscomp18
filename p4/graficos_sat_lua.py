import numpy as np
import matplotlib.pyplot as plt

fdados = [('864',100),('432',200),('288',300),('216',400),
          ('144',600),('48',1800),('36',2400),('18',4800)]
dados = [np.loadtxt('p4/dados/sat_lua%s-.dat'%f[0]).T for f in fdados]

# plt.figure(figsize=(10,5),dpi=300)
# for f,dat in list(zip(fdados,dados))[:2:-1]:
#     t,x,y,dphi,dr = dat[0],dat[1],dat[2],dat[5],dat[6]
#     plt.plot(t,dphi,label=str(f[1])+' passos/dia')
#     # plt.plot(t,dr,label=str(f[1])+' passos/dia')
# plt.xlim(175,200)
# plt.ylim(0.2,0.7)
# plt.xlabel(r'Tempo (dias)')
# plt.ylabel(r'$\Delta \phi$ (radianos)')
# plt.title('Perturbação lunar na órbita do satélite geoestacionário')
# plt.legend()

plt.figure(figsize=(10,5),dpi=300)
t,dr = dados[-1][0],dados[-1][6]
plt.plot(t,dr/1000)
plt.xlim(0,50)
plt.xlabel(r'Tempo (dias)')
plt.ylabel(r'$\Delta r$ (km)')
plt.title('Perturbação lunar na órbita do satélite geoestacionário')
plt.savefig('p4/fig/sat_lua_dr.png',bbox_inches='tight')

# plt.figure(figsize=(10,10),dpi=300)
# plt.plot(x/1000,y/1000)
# plt.axes().set_aspect('equal','datalim')
# plt.xlabel('x (km)')
# plt.ylabel('y (km)')
# plt.title('Órbita geostacionária perturbada pela Lua')
# plt.savefig('p4/fig/sat_lua_orbita.png',bbox_inches='tight')
