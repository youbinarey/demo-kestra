# Investigación sobre enviroment secrets
`Kestra` ofrece distintas alternativas dependiendo de la versión en uso `Open-Source` o `Enterprise`.
A continuación se detalla el procedimiento para que dentro de los flujos sean accesibles este tipo de variables de entorno siguiendo la versión `Open-Source`.

## Docker Compose
A través de la configuración de kestra se define `env_file:` que referenciará a los ficheros a seguir.
```yaml
kestra:
    env_file:
      - .env_postgres
      - .env_idinet
      - .env_minio
```

## .Env
Para que las variables de cualquier fichero sean accesibles dentro de un `Flow`, debencomenzar por **`KESTRA_`** seguido del nombre y su valor. Ejemplo:
```dotenv
  KESTRA_IDINET_ADMIN_USER=adminuser
  KESTRA_IDINET_ADMIN_PASSWORD=adminuser
```
## Flow

Para poder hacer uso de ella hay que concatenar {{envs. + clave_sin_estar_precedido_por_KESTRA y en minúsculas}}. Ejemplo de un `Flow` cuyo objetivo es devolver el valor de `KESTRA_IDINET_ADMIN_USER`:
```yml
  id: prueba-env
namespace: ejemplo

tasks:
  - id: log
    type: io.kestra.plugin.core.debug.Return
    format: " El usuario de idinet es: {{envs.idinet_admin_user}}"
```

---
## Resumen
 - Permite usar varios `.env` para modularizar tanto como se quiera las configuraciones.
 - Para que una variable sea accesible desde un flow debe comenzar por **`KESTRA_`**.
 - Acceso a variables con *`{{ envs._nombre_variable}}`*


