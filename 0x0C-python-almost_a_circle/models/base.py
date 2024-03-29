#!/usr/bin/python3
"""
=============================
Module with the class Base
=============================
"""

import json
import csv


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Base class constructor
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert dictionary to JSON repr
        """
        if (list_dictionaries == [] or list_dictionaries is None):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves json string to file
        """
        if list_objs is None:
            return "[]"

        dict_list = []

        # Loop through list_objs  invoke it's .to_dictionary method

        for inst in list_objs:
            dict_list.append(inst.to_dictionary())

        # Put each dictionary into a list

        # Convert the list to json using the static method to_json_string()

        json_dict_list = cls.to_json_string(dict_list)

        # Save the json string repr of the list of dictionaries into file

        file_name = cls.__name__ + ".json"
        with open(file_name, 'w', encoding="utf-8") as json_file:
            json_file.write(json_dict_list)

    @staticmethod
    def from_json_string(json_string):
        """
        convert json string to list
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create an instance using key values in dict
        """

        # create dummy instance of class
        dummy_instance = cls(1, 1)

        # Use update() method to update dummy instance

        dummy_instance.update(**dictionary)

        return (dummy_instance)

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        file_name = cls.__name__ + ".json"

        # Open file in read only mode
        try:
            with open(file_name, 'r', encoding="utf-8") as json_file:
                list_dicts = cls.from_json_string(json_file.read())

            # Convert json strings from file into python dicts

            # Use create() method to create instances
            list_insts = []

            for dicts in list_dicts:
                list_insts.append(cls.create(**dicts))

            # Append the instances created above to a list

            # Return that list
            return (list_insts)
        except (IOError, TypeError):
            return []
        
    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + '.csv'
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == 'Rectangle':
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == 'Square':
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])