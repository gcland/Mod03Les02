catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog3 = (("Food", 300), ("Ice Cream", 100))
catalog2 = (("Smartphone", 800), ("Tablet", 450))


def tuple_join(x, y, z):
    join_tuple = x + y + z
    print(join_tuple)

tuple_join(catalog1, catalog3, catalog2)