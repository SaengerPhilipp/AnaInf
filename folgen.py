import numpy as np
import matplotlib.pyplot as plt

limit_value = 0
epsilon = 0.15

#hier einfach Folgend definieren und damit rum spielen +in zeile 20 den plot anpassen
n = np.arange(1, 50)
b_n = 1 + ((-1)**n) / n
a_n = 1/n
c_n = (-1)**n
d_n = 1
e_n = 2**n
f_n = np.where(n % 2 == 0, 1.0, 1.0 / n)

N = int(np.ceil(1 / epsilon))

plt.figure(figsize=(10, 6))

plt.scatter(n, b_n, color='blue', label='Folge $a_n$', zorder=3)

plt.axhline(y=limit_value, color='green', linestyle='-', label=f'Grenzwert $a = {limit_value}$')

plt.axhspan(limit_value - epsilon, limit_value + epsilon, color='lightgreen', alpha=0.3, label=f'Epsilon-Schlauch ($\pm${epsilon})')

plt.axvline(x=N, color='red', linestyle='--', label=f'Index $N = {N}$')

plt.title('Visualisierung der Konvergenz einer Folge')
plt.xlabel('Index $n$')
plt.ylabel('Wert $a_n$')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()