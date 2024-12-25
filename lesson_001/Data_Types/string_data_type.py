import sys

# String data by single quoted format
dataStringSample1='Shubhankar Ingale'
print("This is single quoted example")
print(f"Type of the {dataStringSample1} is : {type(dataStringSample1)}")
print(f"Length of the {dataStringSample1} is : {len(dataStringSample1)}")
print(f"Size of the {dataStringSample1} is : {sys.getsizeof(dataStringSample1)}")
print("")

# String data by double quoted format
dataStringSample2="Shubhankar Ingale"
print("This is double quoted example")
print(f"Type of the {dataStringSample2} is : {type(dataStringSample2)}")
print(f"Length of the {dataStringSample2} is : {len(dataStringSample2)}")
print(f"Size of the {dataStringSample2} is : {sys.getsizeof(dataStringSample2)}")
print("")
