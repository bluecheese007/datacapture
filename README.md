# DataCapture

## Descripción

DataCapture es un sistema eficiente para capturar y analizar datos estadísticos. Utiliza estructuras de datos optimizadas y algoritmos para proporcionar análisis en tiempo constante.

## Características

- **Captura Eficiente**: Utiliza `defaultdict` para un almacenamiento eficiente y sin errores de datos numéricos.
- **Análisis en Tiempo Constante**: A través de `StatsBuilder`, realiza cálculos estadísticos en O(1).

## Instalación

El código esta contruido usando python 3.10. Se puede crear un ambiente ejecutando

```bash
conda create --name myenv python=3.10
```

y luego activandolo 
```bash
conda activate myenv
```


Instale las dependencias de desarrollo con:

```bash
pip install -r requirements-dev.txt
```

## Uso

```python
from DataCapture import DataCapture

capture = DataCapture()
capture.add(3)
capture.add(9)
...
stats = capture.build_stats()
print(stats.less(4))  # Números menores que 4
print(stats.between(3, 8))  # Números entre 3 y 8
...
```
