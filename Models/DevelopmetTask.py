# Models/DevelopmentTask.py
from States.DevelopmentStates import StartedState
from States.DevelopmentStates import StartedState

# Models/DevelopmentTask.py

class DevelopmentTask:
    def __init__(self, description, duration, project, developer):
        self.description = description
        self.duration = duration
        self.project = project
        self.developer = developer
        self.current_state = None  # Atributo para el estado actual

    def change_state(self, new_state):
        self.current_state = new_state

    def get_state(self):
        return self.current_state.__class__.__name__ if self.current_state else "Desconocido"  # Devuelve el estado actual como nombre

