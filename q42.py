import os

path = "test_folder"

if os.path.exists(path):
    print("Directory exists")
else:
    print("Directory does not exist")
