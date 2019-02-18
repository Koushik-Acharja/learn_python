
class Person:
    def __init__(self, first_name):
        self.first_name = first_name
"""   
    first_name = 'TK'
"""

tk = Person('TK')
print(tk.first_name) # => TK

"""
tk = Person()
print(tk.first_name) # => TK
"""

tk = Person('TK')
tk.first_name = 'Kaio'
print(tk.first_name) # => Kaio
