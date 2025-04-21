
##  Estructura del proyecto

Este repositorio está organizado para gestionar y automatizar la importación de flujos en Kestra usando scripts personalizados en Bash y Python.



```bash
├── flows/                         # Flujos YAML organizados por entorno
│   └── dev/                       # Flujos del entorno de desarrollo
│       ├── from_postgres_to_s3.yml           # Flujo principal de exportación
│       ├── hello_dev.yml                     # Ejemplo básico de flujo
│       └── ENTERPRISE_from_postgres_to_s3.yml# Variante enterprise del flujo principal
│
├── kestra_flow_importer/         # Módulo Python con toda la lógica de importación
│   ├── api.py                    # Funciones para interactuar con la API de Kestra
│   ├── importer.py               # Lógica principal de importación de flujos
│   ├── utils.py                  # Funciones auxiliares (parseo YAML, validaciones...)
│   ├── main.py                   # Script principal a ejecutar desde consola
│   ├── requirements.txt          # Dependencias necesarias (requests, PyYAML...)
│   ├── Flow_importer_works.md    # Apuntes y documentación interna
│   └── __init__.py               # Marca el directorio como módulo Python
│
├── sql/                          # Scripts SQL auxiliares
│   └── create_tables.sql         # Script para crear tablas en PostgreSQL  
├── .env                    # Variables de entorno (credenciales, URLs, configuraciones)
├── .env_encoded            # Mismo contenido codificado en base64 (simulación de secrets)
├── docker-compose-kestra.yml # Stack de Kestra + Postgres + MinIO en contenedores
├── encode_vars.sh          # Script para generar `.env_encoded` desde `.env`
├── import_flow.sh          # Bash script para importar un solo flujo
├── import_flows.py         # Script alternativo de importación (versión sin modularizar)
```

