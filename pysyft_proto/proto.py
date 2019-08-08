from os import path
import json

filename = path.dirname(path.dirname(__file__)) + "/proto.json"
proto_info = {}

try:
    with open(filename) as f:
        proto_info = json.load(f)
except Exception:
    pass

