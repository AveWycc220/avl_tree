""" Module for using set """
from modules.set.set import Set

def about_operation():
    print("Allowed operation : 1 -> Add(value) 2-> Contains(value) 3-> Remove(value)\
4 -> Clear() 5 -> Count() 6 -> IsEmpty\n\
q -> Exit h -> Help")
    if set_type == "list":
        print("Example : [value, value] | Nesting allowed")
    if set_type == "dict":
        print("Example : {key : value} | Nesting allowed")
    if set_type == "set":
        print("Example : (value, value) | Nesting allowed")

print("Allowed types: int -> Integer, str -> String, float -> Float, bool -> Boolean, list -> List, dict -> Dictionary, set -> Set")
set_type = input()
new_set = Set(set_type)
about_operation()
while True:
    choose = input()
    if choose == '1':
        print("Enter value")
        value = input()
        new_set.add(value)
    elif choose == '2':
        print("Enter value")
        value = input()
        print(new_set.contains(value))
    elif choose == '3':
        print("Enter value")
        value = input()
        new_set.remove(value)
    elif choose == '4':
        new_set.clear()
    elif choose == '5':
        print(F"Count = {new_set.count()}")
    elif choose == '6':
        print(new_set.is_empty())
    elif choose == 'q':
        break
    elif choose == 'h':
        print("___HELP___\n")
        about_operation()
        print(F"Set : {new_set.__doc__}")
        print(F"Add : {new_set.add.__doc__}")
        print(F"Contains : {new_set.contains.__doc__}")
        print(F"Remove : {new_set.remove.__doc__}")
        print(F"Clear : {new_set.clear.__doc__}")
        print(F"Count : {new_set.count.__doc__}")
        print(F"IsEmpty : {new_set.is_empty.__doc__}")
