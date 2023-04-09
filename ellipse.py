import numpy as np
import matplotlib.pyplot as plt

# Définir les paramètres de l'ellipse
a = 2 # grand axe
b = 1 # petit axe
xc = 0 # coordonnée x du centre
yc = 0 # coordonnée y du centre

# Créer une grille de points
x = np.linspace(-a, a, 100)
y = np.linspace(-b, b, 100)
X, Y = np.meshgrid(x, y)

# Calculer les valeurs de la fonction ellipse
F = ((X-xc)**2/a**2) + ((Y-yc)**2/b**2) - 1

# Tracer la fonction ellipse
plt.contour(X, Y, F, levels=[0])
plt.axis('equal')
plt.show()
