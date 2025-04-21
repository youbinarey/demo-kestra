import sys
from importer import import_flows

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("❗ Uso: python main.py <archivo_o_directorio>")
    else:
        import_flows(sys.argv[1])