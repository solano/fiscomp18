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
plt.style.use('grayscale')

## GRÁFICO DA PARTE (A) ##
dados_a = np.loadtxt('p3/ciclista_a.dat')
t, v, x = dados_a.T
print("Parte (a), distância atingida =",x[-1])

erros = np.abs(v-sol_exata_A(t))/v
i_erro_max = np.argmax(erros)
erro_max = erros[i_erro_max]
print('Curvas coincidem dentro de',erro_max*100,'%%')

plt.figure(dpi=500)
plt.title('Movimento sem resistência do ar')
plt.plot(t,v,label='solução numérica')
plt.plot(t,sol_exata_A(t),'--',label='solução exata')
plt.xlim(0,300)
plt.ylim(0,60)
#plt.grid(linestyle='--',linewidth=0.7)
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
t_term,v_term = t[i_vel_term],v[i_vel_term]

print(vel_terminal(rho,A)-v[-1])

plt.figure(dpi=500)
plt.title('Movimento com resistência do ar ($A$ = 0,333 m$^2$)')
plt.plot(t,v)
plt.plot([0,300],[v[-1],v[-1]],'--',color='gray')
plt.plot([t_term],[v_term],'ko')
plt.annotate('Velocidade terminal\natingida',
             xy=(t_term,v_term),
             xytext=(90,8),
             arrowprops=dict(arrowstyle='->')
             )
plt.plot([t[i_vel_term],t[i_vel_term]],[0,v[i_vel_term]],'--k',linewidth=0.5)
plt.annotate('%.3f s'%t_term, xy=(t_term+5,2))
plt.annotate('%.3f m/s'%v_term, xy=(10,v_term+0.5))
plt.xlim(0,160)
plt.ylim(0,16)
#plt.grid(linestyle='--',linewidth=0.7)
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
dados_c4 = np.loadtxt('p3/ciclista_c4.dat')
v4 = dados_c4.T[1]
dados_c5 = np.loadtxt('p3/ciclista_c5.dat')
v5 = dados_c5.T[1]
t = dados_c1.T[0] # é o mesmo p/ todos
print(vel_terminal(rho,0.1)-v1[-1])
print(vel_terminal(rho,0.2)-v2[-1])
print(vel_terminal(rho,0.3)-v3[-1])
print(vel_terminal(rho,0.4)-v4[-1])
print(vel_terminal(rho,0.5)-v5[-1])

plt.figure(dpi=500)
plt.title('Movimento com resistência do ar ($A$ variável)')
plt.plot(t,v1,'-k',  label='A = 0.1 m$^2$, $v_{term}$ = %.2f m/s'%v1[-1])
plt.plot(t,v2,'--k', label='A = 0.2 m$^2$, $v_{term}$ = %.2f m/s'%v2[-1])
plt.plot(t,v3,':k',  label='A = 0.3 m$^2$, $v_{term}$ = %.2f m/s'%v3[-1])
plt.plot(t,v4,'-.k', label='A = 0.4 m$^2$, $v_{term}$ = %.2f m/s'%v4[-1])
plt.plot(t,v5,'gray',label='A = 0.5 m$^2$, $v_{term}$ = %.2f m/s'%v5[-1])

plt.xlim(0,160)
plt.ylim(0,20)
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.legend(loc='lower right')

plt.savefig('p3/ciclista_c.png',bbox_inches='tight')
