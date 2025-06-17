import json

def load_json(pet_type, pet_name):
    with open("pet_type.json", "r") as f:
        loaded_data = json.load(f)
        return loaded_data

def upload_to_json(data, pet_name, pet_type):
    with open(f"{pet_type}-{pet_name}.json", "w") as f:
        json.dump(data, f, indent=4)