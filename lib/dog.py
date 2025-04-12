#!/usr/bin/env python3
# lib/dog.py
class Dog:
    approved_breeds = [
        "Mastiff", "Chihuahua", "Corgi", "Shar Pei",
        "Beagle", "French Bulldog", "Pug", "Pointer"
    ]

    def __init__(self, name="Fido", breed="Mastiff"):
        self.name = name
        self.breed = breed

    #getter
    def get_name(self):
        return self._name

    #name.setter
    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")
    name = property (get_name, set_name)

    #property
    def get_breed(self):
        return self._breed

    #breed.setter
    def set_breed(self, value):
        if value in Dog.approved_breeds:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
    breed = property (get_breed, set_breed)
