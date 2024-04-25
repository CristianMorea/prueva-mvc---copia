class Task:
    def __init__(self, description, duration, project, developer):
        self.description = description
        self.duration = duration
        self.project = project
        self.developer = developer
        self.finished = False

    def getDetails(self):
        return {
            "description": self.description,
            "duration": self.duration,
            "project": self.project,
            "developer": self.developer,
            "finished": self.finished,
        }
