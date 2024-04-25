# Models/TestingTask.py
from States.TestingStates import ProposedState

# Models/TestingTask.py

class TestingTask:
    def __init__(self, description, duration, project):
        self.description = description
        self.duration = duration
        self.project = project
        self.current_state = None  # Atributo para el estado actual

    def change_state(self, new_state):
        self.current_state = new_state

    def get_state(self):
        return self.current_state.__class__.__name__ if self.current_state else "Desconocido"  # Devuelve el estado actual como nombre

