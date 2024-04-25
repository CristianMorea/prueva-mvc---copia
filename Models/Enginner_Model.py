class Engineer:
    def __init__(self, name, engineer_type):
        self.name = name
        self.type = "Development" if engineer_type == "1" else "Testing"  # Configuración correcta del tipo de ingeniero
