import streamlit as st
import get_todos

todos = get_todos.getTodos()


def add_todos():
    todo1 = st.session_state["new_todo"] + "\n"
    todos.append(todo1)
    get_todos.writeTodos(todos)
    st.session_state["new_todo"] = ""


st.title("TO-DO App")
st.subheader("This is my TO-DO APP")
st.write("This App is to increase your productivity")
st.write("Add your TO-DOs below :")

for index, item in enumerate(todos):
    checkBox = st.checkbox(item, key=item)
    if checkBox:
        todos.pop(index)
        get_todos.writeTodos(todos)
        del st.session_state[item]
        st.session_state["new_todo"] = ""
        st.experimental_rerun()

st.text_input(label="",
              placeholder="Enter text here",
              on_change=add_todos,
              key="new_todo",
              )

