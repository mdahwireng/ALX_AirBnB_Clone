import json
import os

class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "./file.json"
    __objects = dict()

    def __init__(self) -> None:
        if not os.path.exists("./data/"):
            os.mkdir("./data")

    def all(self, ):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj["id"]] = obj

    def save(self, ):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_json = json.dumps(self.__objects)
        with open(self.__file_path, "w", encoding="utf-8") as output:
            output.write(obj_json)

    def reload(self, ):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path)
        exists otherwise, do nothing"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as input_json:
                input_json = json.load(input_json)
            self.__objects = input_json
