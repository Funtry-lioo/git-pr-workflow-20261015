def greet(name):
    name = name.strip()
    if not name:
        name = "friend"
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("GitHub"))
    print(greet(""))
    print(greet("   "))
