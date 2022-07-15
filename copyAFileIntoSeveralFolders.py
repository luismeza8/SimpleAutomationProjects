import os
import shutil
from pathlib import Path

while True:
    file = Path(input("Archivo: "))

    if os.path.isfile(file) == False:
        print("Archivo no valido")
    else:
        break

while True:
    destiny = Path(input("Carpeta con carpetas: "))

    if os.path.isdir(destiny) == False:
        print("Carpeta no valida")
    else:
        break

for carpeta in os.listdir(destiny):
    if os.path.isdir(destiny/carpeta) == True:
        shutil.copy(file, destiny/carpeta)

print("Listo!")
