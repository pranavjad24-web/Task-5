import os

folder = "experiment_results"

if not os.path.exists(folder):
    os.mkdir(folder)
    print("Directory created")
else:
    print("Directory already exists")
