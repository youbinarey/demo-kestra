# Kestra Flow Importer

Permite importar flujos `.yml` de Kestra a través de su API REST.

##  Requisitos

- Python 
- Docker + Kestra ejecutándose localmente
- Instalar dependencias:

```bash
pip install -r requirements.txt
```

##  Uso

```bash
python main.py <fcihero-o-directorio>
```

Ejemplos:

```bash
python main.py flows/dev/flow.yml
python main.py flows/
```

El script detectará el `id` y `namespace` del YAML, creará el namespace si no existe, y hará POST a la API de Kestra.


## Ejecución
1. Punto de entrada 'main.py'  
Comprueba que recibe un parametro.

2. 'mian.py' llama a importer.import_flows(path)
3.