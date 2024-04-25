# Models/States/DevelopmentStates.py
from States.TaskState import TaskState
from States.TaskState import TaskState
# States/DevelopmentStates.py
from States.TaskState import TaskState

class StartedState(TaskState):
    def set_state(self, task):
        task.is_started = True
        task.is_in_process = False
        task.is_finished = False

    def get_state(self):
        return "Iniciada"


class InProcessState(TaskState):
    def set_state(self, task):
        task.is_started = False
        task.is_in_process = True
        task.is_finished = False

    def get_state(self):
        return "En proceso"


class FinishedState(TaskState):
    def set_state(self, task):
        task.is_started = False
        task.is_in_process = False
        task.is_finished = True

    def get_state(self):
        return "Terminada"
