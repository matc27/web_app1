FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):                                       # Custom function definition
    """ Read a text file and return the list of todo item. """          # Doc string to describe what the function does - it is shown when use help(function)
    with open(filepath, "r") as file_local:                             # with block which serve to manages file and automatically closes the file when exiting the block
        todos_local = file_local.readlines()                            # create a starting list from the existing lines in the file
    return todos_local                                                  # output of the function

def write_todos(todos_arg, filepath=FILEPATH):                          # Custom function to simplify the script - write the user input in the txt file
    """ Write the todo item list in the text file. """
    with open(filepath,"w") as file:                                    # with block which serve to manages file and automatically closes the file when exiting the block
            file.writelines(todos_arg)                                  # overwrite the file with the new list including the old items and the new user input

if __name__ == "__main__":                                              # useful to make diference when program run directly or via other file (imported there)
     print("Hello")

