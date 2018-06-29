class Dog:
    def say_something(self):
        print('woof')

    def set_age(self, age):
        # R
        # Coerce
        # ACt
        # return

        if not isinstance(age, int):
            raise 'must be an integer'
        self._age = age

    def get_age(self):
        return print("the age is " +  self._age)

    def print_instance(self):
        print(self)

class Person:
    def say_something(self):
        print('hello')
