
class Person:
    def __init__(self, first_name, email):
        self.first_name = first_name
        self._email = email
        
    def update_email(self, new_email):
        self._email = new_email

    def email(self):
        return self._email


tk = Person('TK', 'tk@mail.com')
print(tk._email) # tk@mail.com


tk = Person('TK', 'tk@mail.com')
print(tk.email()) # => tk@mail.com
# tk._email = 'new_tk@mail.com' -- treat as a non-public part of the class API
print(tk.email()) # => tk@mail.com
tk.update_email('new_tk@mail.com')
print(tk.email()) # => new_tk@mail.com

