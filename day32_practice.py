def gen():
    yield 1
    yield 2
    yield 3

# To use the generator:
for value in gen():
    print(value)
