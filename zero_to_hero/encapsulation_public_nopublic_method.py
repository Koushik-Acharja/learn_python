
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age

    #public method
    def show_age(self):
        return self._age
    
    #non public method
    def _show_age(self):
        return self._age
    
    # or
    def view_age(self):
        return self._get_age()
    
    def _get_age(self):
        return self._age



tk = Person('TK', 25)
#for public method
print(tk.show_age()) # => 25

#for non public method
print(tk._show_age()) # => 25

#or
print(tk.view_age()) # => 25