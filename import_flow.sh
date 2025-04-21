#!/bin/bash

NAMESPACE=dev
FLOW_PATH=$1

curl -XPOST "http://localhost:8080/api/v1/namespaces/$NAMESPACE/flows" \
  -H "Content-Type: application/yaml" \
  --data-binary @"$FLOW_PATH"
