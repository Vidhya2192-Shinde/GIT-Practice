"kkjhbvhdbdbkbv"

def e():
    n=3
    yield n
    n=5
    yield n

x=e()
print(next(x))
print(next(x))

