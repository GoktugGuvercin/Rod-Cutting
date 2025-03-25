import time
from recursion import cut_rod
from memoization import (
    memoized_cut_rod,
    bottom_up_cut_rod,
)

lengths = [i for i in range(1, 19)]
prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 32, 36, 37, 37, 41, 45, 47, 50]
price_dict = {le: p for le, p in zip(lengths, prices)}

# Recursive Top-Down Approach
start = time.time()
for i in range(1, 19):
    print(f"Length {i}, max revenue: ", cut_rod(i, price_dict))
end = time.time()
print("Total duration: ", end - start)
print()

# Memoized Recursive Top-Down Approach
start = time.time()
for i in range(1, 19):
    print(f"Length {i}, max revenue: ", memoized_cut_rod(i, price_dict))
end = time.time()
print("\nTotal duration: ", end - start)
print()

# Memoized Bottom-Up Approach
start = time.time()
for i in range(1, 19):
    print(f"Length {i}, max revenue: ", bottom_up_cut_rod(i, price_dict))
end = time.time()
print("\nTotal duration: ", end - start)
print()
