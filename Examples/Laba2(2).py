def example(color):
    if color == "green":
        return "This is tree"
    elif color == "blue":
        return "This is sky"
    else:
        return "I don't know"
what_is_it = example('blue')
print(what_is_it)

example = None
if example is None:
    print("It's nothing")
else:
    print("It's something")

    
def cat(name, color, age):
    return {'name': name, 'color': color, 'age': age}

my_cat = cat(color = 'white', age = 15, name = 'Nusha')
print(my_cat)