my_dict = {'task1': 1, 'task2': 2, 'task3': 1, 'task4': 3, 'task5': 1}

# Create a new dictionary with the values as keys and the tasks as values
new_dict = {}
for k, v in my_dict.items():
    new_dict.setdefault(v, []).append(k)

# Get the list of tasks for the value we are interested in
value = 1
tasks = new_dict.get(value, [])

print("Tasks with value", value, ":", tasks)