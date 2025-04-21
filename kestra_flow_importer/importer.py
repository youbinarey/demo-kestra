from kestra_flow_importer.api import namespace_exists, create_namespace, post_flow
from utils import extract_id_namespace, get_flow_files


# Comprueba si el namespace existe, si no existe lo crea.
def ensure_namespace(namespace):
    res = namespace_exists(namespace)
    if res.status_code == 404:
        print(f"➕ Creando namespace: {namespace}")
        res = create_namespace(namespace)
        if res.ok:
            print(f"✅ Namespace '{namespace}' creado")
            return True
        else:
            print(f"❌ Error creando namespace: {res.status_code}")
            return False
    elif res.ok:
        print(f"✅ Namespace '{namespace}' ya existe")
        return True
    else:
        print(f"❌ Error comprobando namespace: {res.status_code}")
        return False


# Obtiene lista .yml, asignaa flow_id y namespace y POST con el flujo.

def import_flows(path):
    for file in get_flow_files(path):
        flow_id, namespace, flow_yaml = extract_id_namespace(file)
        if not flow_id or not namespace:
            print(f"⚠️ Saltando {file}")
            continue

        print(f"📤 Importando {file} (ID: {flow_id}, NS: {namespace})")
        if not ensure_namespace(namespace):
            continue

        res = post_flow(namespace, flow_yaml)
        if res.ok:
            print(f"✅ Importado correctamente: {flow_id}")
        else:
            print(f"❌ Error al importar {flow_id}: {res.status_code} - {res.text}")