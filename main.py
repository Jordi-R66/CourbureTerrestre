from math import cos, sin, acos, atan2, sqrt, pi

RAYON_EQUA: float = 6_378_137.0
RAYON_POLE: float = 6_356_752.314245179497563967

DEGS: float = 180.0 / pi
RADS: float = pi / 180.0

R: float = (2 * RAYON_EQUA + RAYON_POLE) / 3

distance: float = 56.25 #float(input("Distance au sol entre l'objet observé et le point d'observation (en km) : "))
hauteur_objet: float = 87 #float(input("Hauteur de l'objet observé (en mètres) : "))
hauteur_regard: float = 4 #float(input("Hauteur du regard (en mètres) : "))

d_regard: float = (R+hauteur_regard)
d_objet: float = (R+hauteur_objet)

alpha: float = distance * 1000 / R
beta: float = acos(R/d_regard)

if alpha > 1:
	alpha = 1.0 / alpha

if beta > 1:
	beta = 1.0 / beta

CoordsObs: tuple[float, float] = (cos(pi/2 - beta) * d_regard, sin(pi/2 - beta) * d_regard)
CoordsObj: tuple[float, float] = (cos(pi/2 - beta + alpha) * d_objet, sin(pi/2 - beta + alpha) * d_objet)

DeltaX: float = CoordsObs[0] - CoordsObj[0]
DeltaY: float = CoordsObj[1] - CoordsObs[1]

VISIBILITE: str = "Objet visible en théorie" if (DeltaY > 0) else "Objet invisible en théorie"

print(f"Hauteur visible théorique : {DeltaY:.2f}\n{VISIBILITE} mètres")


#CoordsHor: tuple[float, float] = (cos(pi/2) * R, sin(pi/2) * R)

#DistanceHor: float = beta * R

# ---------------------- ÉQUATION DE LA TANGENTE PAR RAPPORT À L'HORIZON ----------------------

"""m, p = 0.0, 0.0
Delta_x: float = CoordsObs[0] - CoordsHor[0]

if (Delta_x != 0):

	Delta_y: float = CoordsObs[1] - CoordsHor[1]

	d_hor: float = sqrt(Delta_x**2 + Delta_y**2)

	m: float = Delta_y/Delta_x
	p: float = CoordsHor[1] - (CoordsHor[0] * m)
"""
# --------------- FINAL ----------------