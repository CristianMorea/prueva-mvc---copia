from Controllers.Task_Controller import TaskController

from Views.Task_View import TaskView
def main():
    tasks = []
    engineers = []
    view = TaskView()

    task_controller = TaskController(tasks, engineers, view)  
    task_controller.runController()  # Ejecutar el controlador

if __name__ == "__main__":
    main()
