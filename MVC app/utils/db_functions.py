import json

# read the data from the json file
def load_db(path):
    try:
        with open(path, "r") as f:
            content = f.read()
            content = json.loads(content)
            return content
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return

def save_to_db(updated_db, path):
    try:
        with open(path,'w') as f:
            f.write(json.dumps(updated_db, indent=2))
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return