with open("log.txt") as f:
    content = f.read()
if "python" in content:
    print("yes, python is in the para")
else:
    print("No,python is not in the para")
    