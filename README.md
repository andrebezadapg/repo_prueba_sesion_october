# Demo GitHub & VS Code — Reporte de ventas

Repo de práctica de la sesión **AI x A&I**. Mini-proyecto que lee un archivo de ventas y genera un gráfico.

## Archivos

| Archivo | Qué es |
|---|---|
| `datos/ventas.csv` | Datos de ejemplo: fecha, región, producto, ventas (12 filas) |
| `reporte_ventas.py` | Script que suma ventas por región y guarda `reporte.png` |
| `participantes/` | Una carpeta donde cada persona agrega su archivo |

## Cómo correrlo

```bash
pip install pandas matplotlib
python reporte_ventas.py
```

Salida esperada en la terminal:

```
Ventas totales por region:
region
Peru       5650
Chile      4200
Ecuador    2440
```

Y un archivo nuevo: **`reporte.png`** con el gráfico de barras.

## Tu tarea en la sesión

1. **Clona** este repo (`Ctrl+Shift+P` → `Git: Clone`)
2. **Crea una rama**: `tunombre/mi-primer-cambio` (clic en `main`, abajo a la izquierda)
3. **Crea tu archivo** en `participantes/tunombre.md`
4. **Commit** con un mensaje que empiece con verbo: `Add Maria to participantes`
5. **Push**: clic en `Publish Branch`
6. **Pull request** en github.com → agrégame como reviewer
7. **Pull/Sync** al final para ver los archivos de todos
