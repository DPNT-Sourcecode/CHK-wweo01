

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    if not friend_name:
        friend_name = "World"
    return "Hello, {}!".format(friend_name)


assert hello("") == "Hello, World!"
assert hello("bob") == "Hello, bob!"
