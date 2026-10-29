import numpy as np
import matplotlib.pyplot as plt
# Alexandro Aguilar NC 0007
No_lista = [1, 2, 3, 12, 40]
califa_ml = [20, 30, 80, 100, 90]
califa_va = [70, 50, 60, 90, 80]

plt.plot(No_lista, califa_ml, label="Califa ML")
plt.plot(No_lista, califa_va, label="Califa VA")
plt.title("calificaciones materias 0007")
plt.xlabel("Numero de lista")
plt.ylabel("Calificación")

plt.legend()
plt.show()
print("Alexandro Aguilar NC 0007")