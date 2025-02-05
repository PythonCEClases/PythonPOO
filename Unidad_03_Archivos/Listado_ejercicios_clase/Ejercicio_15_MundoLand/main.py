from mamiferos.mamiferos_clases import Mamiferos
from plantas.plantas_clases import Plantas

mams = Mamiferos()
plas = Plantas()


for elemento in mams.mamiferos:
    for k, v in elemento.items():
        print(f"{k}: {v}")

for elemento in plas.plantas:
    for k, v in elemento.items():
        print(f"{k}: {v}")