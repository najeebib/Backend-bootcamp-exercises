import json

def count_workers(dict):
    if "subordinates" not in dict:
        return 1
    return 1 + sum(count_workers(subordinate) for subordinate in dict["subordinates"])

def count_workers_under_cto(dict):
    if "subordinates" not in dict:
        return 0
    cto_node = next(subordinate for subordinate in dict["subordinates"] if subordinate.get("name") == "CTO")
    return count_workers(cto_node)

def count_developers(dict):
    if "subordinates" not in dict:
        return 1 if "developer" in dict.get("name").lower() else 0
    return sum(count_developers(subordinate) for subordinate in dict["subordinates"])

def get_departments(dict):
    if "subordinates" not in dict:
        return []
    return [dict.get("name")] + [department for subordinate in dict["subordinates"] for department in get_departments(subordinate)]

with open('companies.json', 'r') as f:
    data = json.load(f)

for company in data:
    print(count_workers(company))
    print(count_workers_under_cto(company))
    print(count_developers(company))
    print(get_departments(company))
