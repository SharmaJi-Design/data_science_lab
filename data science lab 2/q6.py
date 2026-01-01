#6. Simple Path Validator 
#Represent a small map as a dictionary like {"A": {"B", "C"}, "B": {"A", "D"}, "C": {"A", "D"}, "D": 
#{"B", "C"}}. Ask the user to input a path, e.g., ["A", "C", "D"]. Check if each consecutive step is 
#connected and print "Valid path" or "Invalid path". 

map_graph = {
    "A": {"B", "C"},            
    "B": {"A", "D"},
    "C": {"A", "D"},
    "D": {"B", "C"}
}
def is_valid_path(path):
    for i in range(len(path) - 1):
        current = path[i]
        next_node = path[i + 1]
        if next_node not in map_graph.get(current, set()):
            return False
    return True
user_input = input("Enter a path as a list of nodes (e.g., ['A', 'C', 'D']): ")
try:
    path = eval(user_input)
    if not isinstance(path, list) or not all(isinstance(node, str) for node in path):
        raise ValueError
    if is_valid_path(path):
        print("Valid path")
    else:

        print("Invalid path")
except:
    print("Invalid input format. Please enter a list of nodes.")


        