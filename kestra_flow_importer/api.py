import requests

API_BASE = "http://localhost:8080/api/v1"

def namespace_exists(namespace):
    return requests.get(f"{API_BASE}/namespaces/{namespace}")

def create_namespace(namespace):
    return requests.post(f"{API_BASE}/namespaces/{namespace}")

def post_flow(namespace, flow_yaml):
    return requests.post(
        f"{API_BASE}/flows/{namespace}",
        headers={"Content-Type": "application/json"},
        json=flow_yaml
    )