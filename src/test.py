import os

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(os.path.abspath(current_dir))
print(root_dir)
output_dir = os.path.join(root_dir, "output")
print(output_dir)
filename = "expenses.json"
output_file_path = os.path.join(output_dir , filename)
print(output_file_path)