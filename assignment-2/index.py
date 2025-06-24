lst = [10, 20, 30, 40, 50]
element = 30
if element in lst:
    index = lst.index(element)
    print(f"Index of {element} is {index}")
else:
    print(f"{element} not found in the list")
