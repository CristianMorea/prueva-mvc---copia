
# Controllers/Task_Controller.py
from Models.DevelopmetTask import DevelopmentTask 
from Models.TestingTask import TestingTask 

from Models.TestingTask import TestingTask
from States.DevelopmentStates import StartedState, InProcessState, FinishedState
from States.TestingStates import ProposedState, InTestsState, CertifiedState
from Views.Task_View import TaskView
# Controllers/Task_Controller.py

from Models.DevelopmetTask import DevelopmentTask 
from Models.TestingTask import TestingTask 
from States.DevelopmentStates import StartedState, InProcessState, FinishedState
from States.TestingStates import ProposedState, InTestsState, CertifiedState
from Views.Task_View import TaskView


class TaskController:
    def __init__(self, tasks, engineers, view):
        self.tasks = tasks
        self.engineers = engineers
        self.view = view

    def add_and_assign_task(self):
        try:
            task_type = int(input("Elija el tipo de tarea (1: Desarrollo, 2: Pruebas): "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            return

        description = input("Ingrese la descripción de la tarea: ")
        duration = input("Ingrese la duración de la tarea (en horas): ")
        project = input("Ingrese el proyecto al que pertenece la tarea: ")

        if task_type == 1:
            developer_name = input("Ingrese el nombre del desarrollador: ")
            new_task = DevelopmentTask(description, duration, project, developer_name)
            new_task.change_state(StartedState())  # Cambiar estado inicial
        elif task_type == 2:
            new_task = TestingTask(description, duration, project)
            tester_name = input("Ingrese el nombre del ingeniero de pruebas: ")
            new_task.tester = tester_name
            new_task.change_state(ProposedState())  # Cambiar estado inicial
        else:
            self.view.show_error_message("Tipo de tarea no válido.")
            return

        self.tasks.append(new_task)
        print(f"Tarea '{description}' asignada correctamente.")

    def change_task_status(self):
        self.view.showAllTasks(self.tasks)

        index = int(input("Ingrese el índice de la tarea para cambiar su estado: "))

        task = self.tasks[index]

        if isinstance(task, DevelopmentTask):
            print("Elija el nuevo estado:")
            print("1: Iniciada")
            print("2: En proceso")
            print("3: Terminada")

            new_status = int(input("Ingrese el número correspondiente al nuevo estado: "))

            if new_status == 1:
                task.change_state(StartedState())
            elif new_status == 2:
                task.change_state(InProcessState())
            elif new_status == 3:
                task.change_state(FinishedState())
        elif isinstance(task, TestingTask):
            print("Elija el nuevo estado:")
            print("1: Propuesta")
            print("2: En pruebas")
            print("3: Certificada")

            new_status = int(input("Ingrese el número correspondiente al nuevo estado: "))

            if new_status == 1:
                task.change_state(ProposedState())
            elif new_status == 2:
                task.change_state(InTestsState())
            elif new_status == 3:
                task.change_state(CertifiedState())

        print(f"El estado de la tarea con índice {index} ha cambiado con éxito.")

    def runController(self):
        while True:
            try:
                action = int(input("Elija una acción (1: Crear y asignar tarea, 2: Cambiar estado de tarea, 0: Salir): "))
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue

            if action == 1:
                self.add_and_assign_task()
            elif action == 2:
                self.change_task_status()
            elif action == 0:
                print("Saliendo del programa...")
                break
            else:
                print("Acción no válida. Inténtelo de nuevo.")
