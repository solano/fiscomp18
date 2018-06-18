import matplotlib.pyplot as plt

plt.figure(dpi=100)
plt.plot(range(100),[a**2-40*a for a in range(100)])
plt.show()
