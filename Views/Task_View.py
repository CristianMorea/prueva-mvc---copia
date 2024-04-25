from Models.DevelopmetTask import DevelopmentTask
from Models.TestingTask import TestingTask
# Views/Task_View.py

from Models.DevelopmetTask import DevelopmentTask
from Models.TestingTask import TestingTask

class TaskView:
    def __init__(self):
        pass

    def showAllTasks(self, tasks):
        if not tasks:
            print("No hay tareas para mostrar.")
            return

        print("Lista de tareas:")
        for index, task in enumerate(tasks):
            status = task.get_state()  # Obtener el estado usando el patrón Strategy
            if isinstance(task, DevelopmentTask):
                developer_name = task.developer
                print(
                    f"Índice: {index}, Descripción: {task.description}, Duración: {task.duration} horas, Proyecto: {task.project}, "
                    f"Desarrollador: {developer_name}, Estado: {status}"
                )
            elif isinstance(task, TestingTask):
                tester_name = getattr(task, 'tester', 'No asignado')
                print(
                    f"Índice: {index}, Descripción: {task.description}, Duración: {task.duration} horas, Proyecto: {task.project}, "
                    f"Ingeniero de pruebas: {tester_name}, Estado: {status}"
                )

    def show_error_message(self, message):
        print(f"Error: {message}")

    def showFinishedTasks(self, tasks):
        print("Lista de tareas completadas:")
        for idx, task in enumerate(tasks):
            if task.get_state() == "FinishedState":  # Comparar con el estado "terminada"
                print(f"{idx}. {task.description}")

    def showUnfinishedTasks(self, tasks):
        print("Lista de tareas no completadas:")
        for idx, task in enumerate(tasks):
            if task.get_state() != "FinishedState":  # Comparar con el estado "terminada"
                print(f"{idx}. {task.description}")

    def getUserInput(self, prompt="Ingrese un valor:"):
        return input(prompt)

    def promptTaskDetails(self):
        description = self.getUserInput("Ingrese la descripción de la tarea:")
        duration = self.getUserInput("Ingrese la duración de la tarea:")
        project = self.getUserInput("Ingrese el nombre del proyecto:")
        developer = self.getUserInput("Ingrese el nombre del desarrollador:")
        return {"description": description, "duration": duration, "project": project, "developer": developer}

    def addTask(self, newTask):
        print(f"Tarea agregada: {newTask.getDescription()}")
