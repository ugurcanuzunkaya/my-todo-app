import streamlit as st
import functions
import os
import pathlib


def change_dir_to_this_file():
    # getting the current working directory
    cwd = os.getcwd()
    path_of_this_file = pathlib.Path(__file__).parent
    if cwd != path_of_this_file:
        os.chdir(path_of_this_file)

    if not os.path.exists('todos'):
        with open('todos', 'w') as f:
            f.write("")


def add_todo():
    if st.session_state.add_todo == "":
        st.write("Please type something in the input box.")
        return

    if st.session_state.add_todo in todos:
        st.write("To-Do item already exists.")
        return
    
    todos.append(st.session_state.add_todo)
    functions.file_operations(filename='todos', listname=todos, operation="w")
    st.write("New To-Do item added successfully!")


def clear_all_todos():
    todos.clear()
    functions.file_operations(filename='todos', listname=todos, operation="w")
    st.write("All To-Do items cleared successfully!")

change_dir_to_this_file()
todos = functions.file_operations(filename='todos', listname=[], operation="r")

st.title("To-Do List")
st.subheader("This is a simple To-Do List App created using Streamlit.")
st.write("Welcome to the To-Do List App!")

for todo in todos:
    if checkbox := st.checkbox(todo, key=str(todo)):
        todos.remove(todo)
        functions.file_operations(filename='todos', listname=todos, operation="w")
        del st.session_state.add_todo
        st.experimental_rerun()

st.text_input(label=(""), placeholder="Type here...", key="add_todo")
st.button("Add", on_click=add_todo)

st.button("Clear All", on_click=clear_all_todos)

st.write("Thank you for using the To-Do List App!")

