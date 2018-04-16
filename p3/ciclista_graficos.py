import numpy as np
import matplotlib.pyplot as plt

v0 = 4
P = 400
m = 70
dt = 0.1
tmax = 300
rho = 1.3
A = 0.333

# caso sem resistência
sol_exata_A = lambda t: np.sqrt(v0*v0 + 2*P*t/m)

# caso com resistência
vel_terminal = lambda rho,A: (2*P/(rho*A))**(1/3)

# Lembrar de deixar os gráficos em preto e branco

## GRÁFICO DA PARTE (A) ##
dados_a = np.loadtxt('p3/ciclista_a.dat')
t, v, x = dados_a.T
print("Parte (a), distância atingida =",x[-1])

plt.figure(dpi=500)
plt.plot(t,v,label='solução numérica')
plt.plot(t,sol_exata_A(t),label='solução exata')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.legend()
plt.savefig('p3/ciclista_a.png',bbox_inches='tight')

## GRÁFICO DA PARTE (B) ##
dados_b = np.loadtxt('p3/ciclista_b.dat')
t,v,x = dados_b.T
print("Parte (b), distância atingida =",x[-1])
print("Parte (b), velocidade terminal (numérica) =",v[-1])
print("Parte (b), velocidade terminal (analítica) =",vel_terminal(rho,A))

# quando a velocidade terminal foi atingida, dentro de 1e-3
i_vel_term = np.argmax(abs(vel_terminal(rho,A)-v)<1e-3)

plt.figure(dpi=500)
plt.plot(t,v)
plt.plot([t[i_vel_term],t[i_vel_term]],[0,v[i_vel_term]])
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.savefig('p3/ciclista_b.png',bbox_inches='tight')


## GRÁFICO DA PARTE (C) ##
## TRÊS VALORES DIFERENTES DE A ##
dados_c1 = np.loadtxt('p3/ciclista_c1.dat')
v1 = dados_c1.T[1]
dados_c2 = np.loadtxt('p3/ciclista_c2.dat')
v2 = dados_c2.T[1]
dados_c3 = np.loadtxt('p3/ciclista_c3.dat')
v3 = dados_c3.T[1]
t = dados_c1.T[0] # é o mesmo p/ todos

plt.plot(t,v1,label='Área 123123')
plt.plot(t,v2,label='Área 123140')
plt.plot(t,v3,label='Área 123179')

plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.legend()

plt.savefig('p3/ciclista_c.png',bbox_inches='tight')
