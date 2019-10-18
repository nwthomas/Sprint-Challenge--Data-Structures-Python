import time
from binary_search_tree import BinarySearchTree
from binary_search import binary_search

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# NORMAL CODE FOR THIS ASSIGNMENT
# duplicates = []
# bst = BinarySearchTree(names_1[0])
# for i in range(1, len(names_1)):
#     bst.insert(names_1[i])

# for name in names_2:
#     if bst.contains(name):
#         duplicates.append(name)

# STRETCH CODE FOR THIS ASSIGNMENT
duplicates = []
names_1.sort()

for name2 in names_2:
    if binary_search(names_1, name2) == 1:
        duplicates.append(name2)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
