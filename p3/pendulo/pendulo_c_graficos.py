import numpy as np
import matplotlib.pyplot as plt

theta,per1,per2 = np.loadtxt('p3/pendulo/pendulo_c.dat').T

plt.figure(dpi=500)
plt.plot(theta,per2,'k')
plt.xlim(0,90)
plt.xlabel('Ângulo inicial (graus)')
plt.ylabel('Período de oscilação (s)')
plt.title('Período em função do ângulo inicial')
plt.savefig('p3/pendulo/pendulo_c_periodo.png',bbox_inches='tight')
