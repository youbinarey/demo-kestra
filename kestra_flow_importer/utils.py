import yaml
from pathlib import Path

def check_data_validity(data):
    """
    Verifica que los datos contienen los campos 'id' y 'namespace', 
    y que estos campos no están vacíos.

    :param data: Datos cargados desde un archivo YAML.
    :type data: dict
    :return: Tupla con un valor booleano indicando si los datos son válidos y el mensaje de error (si existe).
    :rtype: tuple(bool, str)
    """
    if 'id' not in data or not data['id']:
        return False, "'id' no encontrado o vacío."
    if 'namespace' not in data or not data['namespace']:
        return False, "'namespace' no encontrado o vacío."
    return True, ""

def extract_id_namespace(flow_path):
    """
    Obtiene el ID, NAMESPACE y el contenido del YAML.

    :param flow_path: Ruta al archivo YAML a procesar.
    :type flow_path: str o Path
    :return: Tupla con el ID, el namespace y el contenido del archivo YAML si son válidos, o None si no lo son.
    :rtype: tuple(str, str, dict)
    
    :raises yaml.YAMLError: Si ocurre un error al parsear el archivo YAML.
    """
    with open(flow_path, 'r') as f:
        try:
            data = yaml.safe_load(f)
            is_valid, error_message = check_data_validity(data)
            if not is_valid:
                print(f"⚠️  Error en {flow_path}: {error_message}")
                return None, None, None
    
            return data['id'], data['namespace'], data
        except yaml.YAMLError as e:
            print(f"❌ Error al parsear {flow_path}: {e}")
            return None, None, None


def get_flow_files(path):
    """
    Obtiene una lista de archivos .yml en la ruta especificada.

    :param path: Ruta al archivo o directorio donde buscar archivos .yml.
    :type path: str o Path
    :return: Lista de rutas de archivos .yml encontrados.
    :rtype: list[Path]
    
    :raises FileNotFoundError: Si no se encuentra el archivo o directorio especificado.
    """
    path = Path(path)
    if not path.exists():
        print(f"❌ No se encontró: {path}")
        return []

    if path.is_file() and path.suffix == '.yml':
        return [path]
    elif path.is_dir():
        return list(path.rglob("*.yml"))

    print("❌ Debes proporcionar un archivo .yml o una carpeta.")
    return []