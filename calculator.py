# calculator.py
class Calculator:
    def __init__(self, a: float, b: float, op: str):
        self.a = float(a)
        self.b = float(b)
        self.op = op

    def compute(self) -> float:
        if self.op == '+':
            return self.a + self.b
        if self.op == '-':
            return self.a - self.b
        if self.op == '*':
            return self.a * self.b
        if self.op == '/':
            if self.b == 0:
                raise ZeroDivisionError("division by zero")
            return self.a / self.b
        raise ValueError(f"Unsupported op: {self.op}")
