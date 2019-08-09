from os import path
import json

filename = path.dirname(path.dirname(__file__)) + path.sep +  "proto.json"
proto_info = None

try:
    with open(filename) as f:
        proto_info = json.load(f)
except Exception:
    pass

