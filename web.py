import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"                          # get the value of the input box with sessions_state which is a dictionary
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):                                    # iterate over the todos list to read and print its content
    checkbox = st.checkbox(todo, key=todo)                              # provide dynamic key which is unique for each todo
    if checkbox:                                                        # if the checkbox is checked, the following code is executed
        todos.pop(index)                                                # remove the todo from the list based on its index
        functions.write_todos(todos)                                    # update the text file with the new list
        del st.session_state[todo]                                      # delete the checkbox from the session state to avoid it reappearing when the app reruns
        st.rerun()                                                      # rerun the app to reflect changes (needed for checkboxes)

# for todo in todos:
#     checkbox = st.checkbox(todo, key=todo)                                # provide dynamic key which is unique for each todo
#     if checkbox:                                                          # if the checkbox is checked, the following code is executed
#         todos.remove(todo)                                                # remove the todo from the list
#         functions.write_todos(todos)                                      # update the text file with the new list
#         del st.session_state[todo]                                        # delete the checkbox from the session state to avoid it reappearing when the app reruns
#         st.rerun()                                                        # rerun the app to reflect changes


st.text_input(label="Enter a todo:", placeholder="Add new todo...", 
              on_change=add_todo, key="new_todo")                       # input box with on_change parameter which calls the add_todo function when user hits enter


# st.session_state                                                      # to access the dictionary which stores the values of the input boxes and other widgets