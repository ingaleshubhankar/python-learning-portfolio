import sys

num_list=[1,2,3,4,5,6,7,8,9]
num_tuple=(1,2,3,4,5,6,7,8,9)

print(f"Value of the Number List :{num_list}")
print(f"Value of the Number Tuple :{num_tuple}")
print(f"Length of the Number List : {len(num_list)}")
print(f"Length of the Number Tuple : {len(num_tuple)}")
print(f"Size of the Number List : {sys.getsizeof(num_list)}")
print(f"Size of the Number List Excluding Overhead: {num_list.__sizeof__()}")
print(f"Size of the Number Tuple : {sys.getsizeof(num_tuple)}")
print(f"Size of the Number Tuple Excluding Overhead: {num_tuple.__sizeof__()}")
print("")
