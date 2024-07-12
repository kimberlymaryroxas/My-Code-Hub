tupleA = (((5, 6, 4), (17, 29, 72, ((34, 876, 32), (21, 546, 56))), 27), (44, 34), (194, 532, 567))

def print_nested_tuple(t):
    if isinstance(t, tuple):
        for item in t:
            print_nested_tuple(item)
    else:
        print(t)

print_nested_tuple(tupleA)