import sys, requests, yaml
from pathlib import Path


API_BASE = "http://localhost:8080/api/v1"

# Comprueba si el namespace existe, si no existe lo crea
def ensure_namespace_exists(namespace):
    check = requests.get(f"{API_BASE}/namespaces/{namespace}")
    if check.status_code == 404:
        print(f"➕ Creando namespace: {namespace}")
        create = requests.post(f"{API_BASE}/namespaces/{namespace}")
        if create.ok:
            print(f"✅ Namespace '{namespace}' creado")
        else:
            print(f"❌ Error creando namespace: {create.status_code} - {create.text}")
            return False
    elif check.ok:
        print(f"✅ Namespace '{namespace}' ya existe")
    else:
        print(f"❌ Error comprobando namespace: {check.status_code} - {check.text}")
        return False
    return True


def extract_id_namespace(flow_path):
    with open(flow_path, 'r') as f:
        try:
            data = yaml.safe_load(f) # Flow a diccionario python
            return data.get('id', '<sin-id>'), data.get('namespace', 'dev'), data
        except yaml.YAMLError as e:
            print(f"❌ Error al parsear {flow_path}: {e}")
            return None, None, None


def import_flow(flow_path):
    flow_path = Path(flow_path)
    if not flow_path.exists():
        print(f"❌ No se encontró el archivo o carpeta: {flow_path}")
        return

    if flow_path.is_file() and flow_path.suffix == '.yml':
        flow_files = [flow_path]
    elif flow_path.is_dir():
        flow_files = list(flow_path.rglob("*.yml"))
    else:
        print("❌ Debes proporcionar un archivo .yml o un directorio que los contenga.")
        return

    for file in flow_files:
        flow_id, namespace, flow_yaml = extract_id_namespace(file)
        if not flow_id or not namespace:
            print(f"⚠️  Saltando {file} por falta de id o namespace.")
            continue

        print(f"📤 Importando: {file} (ID: {flow_id}, Namespace: {namespace})")

        if not ensure_namespace_exists(namespace):
            print(f"🚫 No se pudo crear o validar el namespace '{namespace}'. Saltando...")
            continue

        response = requests.post(
            f"{API_BASE}/flows/{namespace}",
            headers={"Content-Type": "application/json"},
            json=flow_yaml
        )

        if response.ok:
            print(f"✅ Importado correctamente: {flow_id}")
        else:
            print(f"❌ Error al importar {flow_id} ({response.status_code}): {response.text}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("❗ Uso: python import_flows.py <archivo_o_directorio>")
    else:
        import_flow(sys.argv[1])
