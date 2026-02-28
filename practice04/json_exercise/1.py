import json

# Открываем JSON файл
with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 30)
print("DN")
print("-" * 30)

# Предполагаемая структура (как обычно в этих заданиях Cisco APIC)
for item in data["imdata"]:
    dn = item["l1PhysIf"]["attributes"]["dn"]
    print(dn)