from States.TaskState import TaskState


class ProposedState(TaskState):
    def change_state(self, task):
        task.is_proposed = True
        task.is_in_tests = False
        task.is_certified = False

class InTestsState(TaskState):
    def change_state(self, task):
        task.is_proposed = True
        task.is_in_tests = True
        task.is_certified = False

class CertifiedState(TaskState):
    def change_state(self, task):
        task.is_proposed = True
        task.is_in_tests = True
        task.is_certified = True