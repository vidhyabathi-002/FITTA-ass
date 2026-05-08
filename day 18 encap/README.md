# ENCAPSULATION

Encapsulation in Python is a mechanism of binding data and methods inside a single class.
It restricts direct access to some object data so operations can be controlled through methods.

## Types

- Public members are accessible from anywhere, both inside and outside the class.
- Protected members are declared with a single underscore prefix, like `_pin`.
- Private members are declared with a double underscore prefix, like `__pin`.

## Getter and Setter

A getter method is used to access or read private data.
A setter method is used to modify or update private data.

Getter and setter methods are used for:

- Data protection
- Validation
- Controlled access
- Encapsulation
