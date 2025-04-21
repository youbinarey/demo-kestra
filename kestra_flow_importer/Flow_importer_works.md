# Kestra Flow Importer

Permite importar flujos `.yml` de Kestra a través de su API REST.

##  Requisitos

- Python > 3.7
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

- `main.py`        👈**PUNTO DE ENTRADA**  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`↓ ` 
- `mainimporter.py`      👈 **Lógica principal**  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`↓ ` 
- `utils.py`       👈 **Lee archivos YAML y extrae info**
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`↓ `
- `api.py`          👈 **Llama a la API REST de Kestra**
