from .operations import Operations

class Calculator:
    def __init__(self):
        self.operations = Operations()
        self.history = []

    def calculate(self, operation: str, x: float, y: float) -> float:
        operations_map = {
            '+': self.operations.add,
            '-': self.operations.subtract,
            '*': self.operations.multiply,
            '/': self.operations.divide
        }

        if operation not in operations_map:
            raise ValueError(f"Unsupported operation: {operation}")

        result = operations_map[operation](x, y)
        self.history.append(f"{x} {operation} {y} = {result}")
        return result

    def get_history(self) -> list:
        return self.history.copy()