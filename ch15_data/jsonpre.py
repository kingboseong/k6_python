import json

data = {"name":"KIm", "age":23}

print(data['name'], type(data), json.dumps(data), type(json.dumps(data)))

res_data = json.dumps(data)
print(type(json.loads(res_data)))
