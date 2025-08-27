#Python Custom JSON Encoder and Decoder

#Write a Python program to create a custom JSON encoder and decoder for complex Python objects.
import json

# Define the Address and Person classes
class Address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

# Custom JSON Encoder
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Address):
            return {
                '__type__': 'Address',
                'street': obj.street,
                'city': obj.city,
                'state': obj.state,
                'zip_code': obj.zip_code
            }
        elif isinstance(obj, Person):
            return {
                '__type__': 'Person',
                'name': obj.name,
                'age': obj.age,
                'address': obj.address
            }
        return json.JSONEncoder.default(self, obj)

# Custom JSON Decoder
def complex_decoder(dct):
    if '__type__' in dct:
        if dct['__type__'] == 'Address':
            return Address(dct['street'], dct['city'], dct['state'], dct['zip_code'])
        elif dct['__type__'] == 'Person':
            address = dct['address']
            if isinstance(address, dict):
                address = complex_decoder(address)
            return Person(dct['name'], dct['age'], address)
    return dct

# Example usage
address = Address("123 ABCD St.", "Gurgoan", "CP", "12345")
person = Person("Sneha", 30, address)

# Serialize to JSON
person_json = json.dumps(person, cls=ComplexEncoder)
print("Serialized JSON:", person_json)

# Deserialize from JSON
decoded_person = json.loads(person_json, object_hook=complex_decoder)
print("\nDecoded Object:", decoded_person.name, decoded_person.age, decoded_person.address.street)

