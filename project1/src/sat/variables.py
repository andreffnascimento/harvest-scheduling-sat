class VariableGenerator:
    current_id = 1
    id_size = 1

    def __init__(self) -> None:
        pass

    @staticmethod
    def generate_var() -> int:
        id = VariableGenerator.current_id
        VariableGenerator.current_id += 1
        VariableGenerator.id_size = len(str(VariableGenerator.current_id - 1))
        return id


class Variable:
    def __init__(self, description:str) -> None:
        self.id = VariableGenerator.generate_var()
        self.description = description
        self.value = None

    def __str__(self) -> str:
        return str(self.id).zfill(VariableGenerator.id_size) + ' ' + self.description + \
            ' ' * (20 - len(self.description))  + ' = ' + str(self.value)

    def __repr__(self) -> str:
        return self.description
