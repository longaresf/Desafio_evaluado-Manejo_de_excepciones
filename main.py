from error import DimensionError
from photo import Foto

foto = Foto(800, 600, "Hermanos")
print(f"Foto creada. Alto: {foto.alto}, Ancho: {foto.ancho}, Nombre: {foto.ruta}")

try:
    foto.ancho = 2501
except DimensionError as e:
    print("\nExcepción capturada al establecer dimensiones de la foto", e)

try:
    foto.alto = 2501
except DimensionError as e:
    print("\nExcepción capturada al establecer altura de la foto", e)
