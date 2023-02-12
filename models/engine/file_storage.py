import json
import os


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to
    instances"""
    __file_path = "./file.json"
    __objects = dict()

    def __init__(self) -> None:
        """Initializes FileStorage intances"""
        if not os.path.exists("./data/"):
            os.mkdir("./data")

    def all(self, ) -> dict:
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj) -> None:
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj['__class__']}.{obj['id']}"
        FileStorage.__objects[key] = obj

    def save(self, ) -> None:
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_json = json.dumps(FileStorage.__objects)
        with open(FileStorage.__file_path, "w", encoding="utf-8") as output:
            output.write(obj_json)

    def reload(self, ) -> None:
        """deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as input_json:
                input_json = json.load(input_json)
            FileStorage.__objects = input_json
        else:
            pass
