def pass_as_a_tuples(*args):
    print(args)

def pass_as_a_dictionary(**kwargs):
    print(kwargs)

if __name__ == '__main__':
    pass_as_a_tuples(1, 2, 3, 4, 5)
    pass_as_a_tuples([1, 2, 3])
    pass_as_a_dictionary(a = 1, b = 2)