import json
with open('sample-data.json') as f:
    data = json.load(f)

print("Interface Status")
print("=" * 79)
print("{:<60} {:<10} {:<10}".format("DN", "Description", "Speed MTU"))
print("-" * 79)

for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']
    dn = attributes['dn']
    description = attributes['descr']
    speed = attributes['speed']
    mtu = attributes['mtu']

    print("{:<60} {:<10} {:<10}".format(dn, description, f"{speed} {mtu}"))