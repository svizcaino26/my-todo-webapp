import streamlit as st
import functions

todo_list = functions.get_tasks()


def add_task():
    new_task = st.session_state['new_task'].strip().capitalize() + '\n'
    todo_list.append(new_task)
    functions.write_tasks(todo_list)


st.title("My To-do App")
st.subheader("This is my to-do app")
st.write("This app is to increase your productivity")

for index, task in enumerate(todo_list):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        todo_list.pop(index)
        functions.write_tasks(todo_list)
        del st.session_state[task]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new to-do...",
              on_change=add_task, key='new_task')
