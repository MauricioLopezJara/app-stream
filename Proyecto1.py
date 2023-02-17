import streamlit as st

def main():
    st.title("Lista de Tareas")
    tasks = ["Comprar leche", "Ir al gimnasio", "Estudiar para el examen"]
    task = st.text_input("Añade una tarea")
    if st.button("Añadir"):
        tasks.append(task)

    st.write("Tareas:")
    for i, task in enumerate(tasks):
        st.write(f"{i+1}. {task}")

if __name__ == "__main__":
    main()
