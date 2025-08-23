#Python Data Validation Library using Dataclasses and type hints

#Write a Python program to create a data validation library using Python's dataclasses and type hints.
# Import necessary modules
from dataclasses import dataclass, field, fields, Field
from typing import Any, Callable, List, get_type_hints

# Custom exception for validation errors
class ValidationError(Exception):
    pass

# Function to validate dataclass fields
def validate(instance):
    cls = instance.__class__
    hints = get_type_hints(cls)
    # Iterate through fields and type hints
    for name, type_hint in hints.items():
        value = getattr(instance, name)
        # Check if value matches type hint
        if not isinstance(value, type_hint):
            raise ValidationError(f"Field '{name}' expects {type_hint}, got {type(value)}")
        # Check for custom validators
        field: Field = next(f for f in fields(cls) if f.name == name)
        if 'validators' in field.metadata:
            for validator in field.metadata['validators']:
                validator(instance, value)

# Decorator to define a validator function
def validator(func: Callable[[Any, Any], None]):
    if not callable(func):
        raise ValueError("Validator must be callable")
    func._is_validator = True
    return func

# Function to define a field with validation
def field_with_validation(*, default: Any = None, default_factory: Callable[[], Any] = None, validators: List[Callable[[Any, Any], None]] = None) -> Field:
    # Ensure only one of default or default_factory is provided
    if default is not None and default_factory is not None:
        raise ValueError('cannot specify both default and default_factory')
    
    metadata = {}
    # Attach validators to metadata
    if validators:
        metadata['validators'] = validators
    
    # Define field with appropriate parameters
    if default is not None:
        return field(default=default, metadata=metadata)
    elif default_factory is not None:
        return field(default_factory=default_factory, metadata=metadata)
    else:
        return field(metadata=metadata)

# Dataclass representing a User with validation
@dataclass
class User:
    # Define fields with validation
    name: str
    age: int = field_with_validation(default=0, validators=[
        validator(lambda instance, value: value >= 0 or ValidationError("Age must be non-negative")),
        validator(lambda instance, value: value <= 150 or ValidationError("Age must be 150 or less"))
    ])
    email: str = field_with_validation(default="", validators=[
        validator(lambda instance, value: "@" in value or ValidationError("Invalid email address"))
    ])

# Example usage
try:
    user = User(name="Arsen", age=30, email="arsen@example.com")
    validate(user)
    print("User is valid")
except ValidationError as e:
    print(f"Validation error: {e}")

