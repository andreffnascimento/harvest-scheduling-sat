class VariableGenerator:
    current_id = 1

    def __init__(self) -> None:
        pass

    @staticmethod
    def generate_var():
        id = VariableGenerator.current_id
        VariableGenerator.current_id += 1
        return id


class Variable:
    def __init__(self, description:str) -> None:
        self.id = VariableGenerator.generate_var()
        self.description = description
        self.value = None

    def __str__(self) -> str:
        return str(self.id) + ' ' + self.description + '\t = ' + str(self.value)

    def __repr__(self) -> str:
        return self.description
