# import json

# # JSON string (text)
# json_text = '{"name": "Aisha", "age": 28}'

# # JSON string → Python dict
# person = json.loads(json_text)

# print(person["name"])   # Aisha
# print(person["age"])    # 28

# # Python dict → JSON string
# back = json.dumps(person)
# print(back)  # '{"name": "Aisha", "age": 28}'

import json

json_text = '''[
  {"name":"Ali",  "age":22, "active":true},
  {"name":"Noor", "age":17, "active":true},
  {"name":"Zaid", "age":30, "active":false}
]'''

users = json.loads(json_text)

# Filter: active users aged 18+
adults = [
    u for u in users
    if u["active"] and u["age"] >= 18
]

print(json.dumps(adults, indent=2))
# [{"name":"Ali","age":22,"active":true}]