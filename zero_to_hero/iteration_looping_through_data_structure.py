

bookshelf = [
  "The Effective Engineer",
  "The 4 hours work week",
  "Zero to One",
  "Lean Startup",
  "Hooked"
]

for book in bookshelf:
    print(book)
    
""""""""

dictionary = { "some_key": "some_value" }

for key in dictionary:
    print("%s --> %s" %(key, dictionary[key]))
    
# some_key --> some_value
    
""""""""

dictionary = { "some_key": "some_value" }

for key, value in dictionary.items():
    print("%s --> %s" %(key, value))

# some_key --> some_value

""""""""

dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian",
  "age": 24
}

for attribute, value in dictionary_tk.items():
    print("My %s is %s" %(attribute, value))
    
# My name is Leandro
# My nickname is Tk
# My nationality is Brazilian
# My age is 24


