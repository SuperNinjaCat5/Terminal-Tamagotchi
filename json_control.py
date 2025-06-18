import json

def load_json(pet_type, pet_name):
    pet_type = pet_type.upper()
    pet_name = pet_name.upper()
    with open(f"{pet_type}-{pet_name}.json", "r") as f:
        loaded_data = json.load(f)
        return loaded_data

def upload_to_json(pet, pet_name, pet_type):
    pet_type = pet_type.upper()
    pet_name = pet_name.upper()
    with open(f"{pet_type}-{pet_name}.json", "w") as f:
        json.dump(pet.to_dict(), f, indent=4)