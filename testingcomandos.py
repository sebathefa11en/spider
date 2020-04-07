import os

if os.path.exists("stack.json"):
    os.remove("stack.json")
    print("Exito")
else:
    print("Can not delete the file as it doesn't exists")