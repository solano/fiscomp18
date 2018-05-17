import numpy as np
import matplotlib.pyplot as plt

dados_a = np.loadtxt('p4/3_corpos_a.dat')
dados_b = np.loadtxt('p4/3_corpos_b.dat')
dados_c = np.loadtxt('p4/3_corpos_c.dat')

for dados,titulo in [(dados_a,'Solução de Lagrange (3 corpos)'),
                     (dados_b,'Solução de Moore (3 corpos)'),
                     (dados_c,'Solução de Moore perturbada (3 corpos)')]:
    corpo1 = np.array([dados[3*i] for i in range(len(dados)//3)]).T
    corpo2 = np.array([dados[3*i+1] for i in range(len(dados)//3)]).T
    corpo3 = np.array([dados[3*i+2] for i in range(len(dados)//3)]).T

    plt.figure(figsize=(5,5),dpi=100)
    plt.plot(corpo1[2],corpo1[3])
    plt.plot(corpo2[2],corpo2[3])
    plt.plot(corpo3[2],corpo3[3])
    plt.axes().set_aspect('equal','datalim')
    plt.title(titulo)
    plt.show()
