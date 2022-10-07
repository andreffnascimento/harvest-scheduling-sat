class VariableGenerator:

    current_id = 0

    def __init__(self) -> None:
        VariableGenerator.current_id = 0

    @staticmethod
    def generate_var():
        id = VariableGenerator.current_id
        VariableGenerator.current_id += 1
        return id



class Variable:

    def __init__(self, description:str, value:bool = None) -> None:
        self.id = VariableGenerator.generate_var()
        self.description = description
        self.value = value

    def __str__(self) -> str:
        return self.description