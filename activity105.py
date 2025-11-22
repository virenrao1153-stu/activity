def product_of_tuple(tup):
    product = 1
    for num in tup:
        product *= num
    return product

tup1 = (4, 3, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 9)

product1 = product_of_tuple(tup1)
product2 = product_of_tuple(tup2)

print("Tuple 1:", tup1)
print("Product of Tuple 1 =", product1)

print("\nTuple 2:", tup2)
print("Product of Tuple 2 =", product2)