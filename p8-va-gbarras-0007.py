import numpy as np
import matplotlib.pyplot as plt
# Alexandro Aguilar NC 0007
diasX = ["Lun","Mar", "Mie", "Jue", "Vie"]
califa_va_y = [5, 6, 3, 8, 10]

plt.bar(diasX,califa_va_y)
plt.title("Califas en VA de Alexandro Aguilar NC 0007")
plt.xlabel("Dias semana habil")
plt.ylabel("Calificaciones en VA")
plt.grid()
plt.show()
print("Alexandro Aguilar NC 0007")