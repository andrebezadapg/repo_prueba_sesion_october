import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos/ventas.csv")
total = df.groupby("region")["ventas"].sum().sort_values(ascending=False)

print("Ventas totales por region:")
print(total)

total.plot(kind="bar", title="Ventas por region", color="#2b6cb0")
plt.tight_layout()
plt.savefig("reporte.png")
print("Listo: grafico guardado en reporte.png")
