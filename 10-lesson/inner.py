def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b), print("I")

result = outer_function(5, 10)
print(result)
