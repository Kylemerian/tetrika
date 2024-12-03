def strict(func):
    def wrapper(*arg, **karg):
        annotations = func.__annotations__

        if len(annotations) != len(arg) + len(karg) + 1:
            raise TypeError(f"Expected number of args - {len(annotations) - 1}, got - {len(arg) + len(karg)}")
        
        for i, (arg_name, expected_type) in enumerate(annotations.items()):
            if arg_name == 'return':
                continue

            if i < len(arg):
                if not isinstance(arg[i], expected_type):
                    raise TypeError(f"Expected type of arg \"{arg_name}\" - {expected_type}, got - {type(arg[i])}")

            elif arg_name in karg:
                if not isinstance(karg[arg_name], expected_type):
                    raise TypeError(f"Expected type of arg \"{arg_name}\" - {expected_type}, got - {type(karg[arg_name])}")

        return func(*arg, **karg)
    return wrapper
    


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError
# print(sum_two(1.2, 2.4))  # >>> TypeError
# print(sum_two("123", 2))  # >>> TypeError