import json

# Open and read the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Print the data
for emp in data['emp_details']:
    print(emp["emp_name"])

# Closing file
