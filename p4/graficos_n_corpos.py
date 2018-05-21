import numpy as np
import matplotlib.pyplot as plt

dados_a = np.loadtxt('p4/dados/3_corpos_a.dat')
dados_b = np.loadtxt('p4/dados/3_corpos_b.dat')
dados_c = np.loadtxt('p4/dados/3_corpos_c.dat')

llll = [([5000,5400],1e-3,dados_a,'Solução de Lagrange (3 corpos)','lagrange'),
        ([5000,6000],1e-4,dados_b,'Solução de Moore (3 corpos)','moore'),
        ([],1e-4,dados_c,'Solução de Moore perturbada (3 corpos)','moore_perturb')]

for pontos,dt,dados,titulo,fn in llll:
    corpo1 = np.array([dados[3*i] for i in range(len(dados)//3)]).T
    corpo2 = np.array([dados[3*i+1] for i in range(len(dados)//3)]).T
    corpo3 = np.array([dados[3*i+2] for i in range(len(dados)//3)]).T

    plt.figure(figsize=(5,5),dpi=300)
    plt.plot(corpo1[2],corpo1[3])
    plt.plot(corpo2[2],corpo2[3])
    plt.plot(corpo3[2],corpo3[3])
    for i in pontos:
        lx = [corpo1[2,i],corpo2[2,i],corpo3[2,i],corpo1[2,i]]
        ly = [corpo1[3,i],corpo2[3,i],corpo3[3,i],corpo1[3,i]]
        style = '--o' if fn=='lagrange' else 'o'
        plt.plot(lx,ly,style,label='t = %.1f'%(i*dt))
    plt.axes().set_aspect('equal','datalim')
    plt.title(titulo)
    plt.legend()
    plt.savefig('p4/fig/3_corpos_%s.png'%fn, bbox_inches='tight')
