# Base para todas las estrategias de estado
class TaskState:
    def get_state(self):
        raise NotImplementedError("Este método debe ser implementado por subclases.")

    def set_state(self, task):
        raise NotImplementedError("Este método debe ser implementado por subclases.")
