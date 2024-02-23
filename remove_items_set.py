small_ints = set(range(21))
print(small_ints)

# small_ints.clear()
# print(small_ints)

small_ints.discard(10)
small_ints.remove(11)
print(small_ints)

# wont crash
small_ints.discard(99)
print(small_ints)

# Removing item from set that does not exits will crash
# small_ints.remove(99)
# print(small_ints)
