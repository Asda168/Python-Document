from abc import ABC, abstractmethod
import math


# ─────────────────────────────────────────────
#  Abstract Base
# ─────────────────────────────────────────────
class Operation(ABC):
    """Abstract base class for all calculator operations."""

    @abstractmethod
    def execute(self, a: float, b: float = None) -> float:
        pass

    @abstractmethod
    def symbol(self) -> str:
        pass


# ─────────────────────────────────────────────
#  Concrete Operations
# ─────────────────────────────────────────────
class Add(Operation):
    def execute(self, a: float, b: float) -> float:
        return a + b

    def symbol(self) -> str:
        return "+"


class Subtract(Operation):
    def execute(self, a: float, b: float) -> float:
        return a - b

    def symbol(self) -> str:
        return "-"


class Multiply(Operation):
    def execute(self, a: float, b: float) -> float:
        return a * b

    def symbol(self) -> str:
        return "×"


class Divide(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

    def symbol(self) -> str:
        return "÷"


class Power(Operation):
    def execute(self, a: float, b: float) -> float:
        return a ** b

    def symbol(self) -> str:
        return "^"


class SquareRoot(Operation):
    def execute(self, a: float, b: float = None) -> float:
        if a < 0:
            raise ValueError("Cannot take square root of a negative number.")
        return math.sqrt(a)

    def symbol(self) -> str:
        return "√"


class Modulo(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Modulo by zero is undefined.")
        return a % b

    def symbol(self) -> str:
        return "%"


# ─────────────────────────────────────────────
#  History Manager
# ─────────────────────────────────────────────
class HistoryManager:
    """Manages calculation history."""

    def __init__(self):
        self._history: list[str] = []

    def add(self, entry: str):
        self._history.append(entry)

    def get_all(self) -> list[str]:
        return list(self._history)

    def clear(self):
        self._history.clear()

    def __len__(self):
        return len(self._history)


# ─────────────────────────────────────────────
#  Calculator
# ─────────────────────────────────────────────
class Calculator:
    """
    Main calculator class.
    Registers operations, performs calculations, and keeps history.
    """

    def __init__(self):
        self._operations: dict[str, Operation] = {}
        self._history = HistoryManager()
        self._register_defaults()

    def _register_defaults(self):
        for op in [Add(), Subtract(), Multiply(), Divide(),
                   Power(), SquareRoot(), Modulo()]:
            self._operations[op.symbol()] = op

    def register_operation(self, operation: Operation):
        """Plug in a custom operation."""
        self._operations[operation.symbol()] = operation

    def calculate(self, a: float, symbol: str, b: float = None) -> float:
        if symbol not in self._operations:
            raise ValueError(f"Unknown operation '{symbol}'. "
                             f"Available: {list(self._operations.keys())}")
        op = self._operations[symbol]
        result = op.execute(a, b)

        # Build history entry
        if b is None:
            entry = f"{symbol}{a} = {result}"
        else:
            entry = f"{a} {symbol} {b} = {result}"
        self._history.add(entry)
        return result

    def history(self) -> list[str]:
        return self._history.get_all()

    def clear_history(self):
        self._history.clear()

    def available_operations(self) -> list[str]:
        return list(self._operations.keys())


# ─────────────────────────────────────────────
#  Interactive REPL
# ─────────────────────────────────────────────
BANNER = """
╔══════════════════════════════════════╗
║        OOP Python Calculator         ║
╠══════════════════════════════════════╣
║  Operations: +  -  ×  ÷  ^  √  %     ║
║  Commands:   history  clear  closed  ║
╚══════════════════════════════════════╝
"""

UNARY_OPS = {"√"}


def parse_input(user_input: str):
    """Parse a line like '3 + 4' or '√ 9' into tokens."""
    parts = user_input.strip().split()
    if not parts:
        return None, None, None

    # Unary: "√ 9"  or  "√9"
    if parts[0] in UNARY_OPS:
        symbol = parts[0]
        a = float(parts[1]) if len(parts) > 1 else float(parts[0][1:])
        return a, symbol, None

    # Binary: "3 + 4"
    if len(parts) == 3:
        a, symbol, b = parts
        return float(a), symbol, float(b)

    raise ValueError(f"Could not parse: '{user_input}'")


def run_repl():
    calc = Calculator()
    print(BANNER)

    while True:
        try:
            raw = input("  calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  Goodbye!")
            break

        if not raw:
            continue

        cmd = raw.lower()

        if cmd == "closed":
            print("  Goodbye!")
            break

        if cmd == "history":
            h = calc.history()
            if not h:
                print("  (no history yet)")
            else:
                print("  ── History ──────────────────")
                for i, entry in enumerate(h, 1):
                    print(f"  {i:>3}. {entry}")
                print("  ─────────────────────────────")
            continue

        if cmd == "clear":
            calc.clear_history()
            print("  History cleared.")
            continue

        try:
            a, symbol, b = parse_input(raw)
            result = calc.calculate(a, symbol, b)
            # Pretty-print
            if isinstance(result, float) and result.is_integer():
                print(f"      = {int(result)}")
            else:
                print(f"      = {result:.10g}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"  ⚠  Error: {e}")
        except Exception as e:
            print(f"  ⚠  Unexpected error: {e}")


# ─────────────────────────────────────────────
#  Demo (runs when executed directly)
# ─────────────────────────────────────────────
def display():
    print(BANNER)
    calc = Calculator()

    cases = [
        (10,  "+",  5),
        (10,  "-",  3),
        (6,   "×",  7),
        (22,  "÷",  4),
        (2,   "^",  10),
        (144, "√",  None),
        (17,  "%",  5),
    ]

    print("  ── Demo calculations ────────────────")
    for a, sym, b in cases:
        result = calc.calculate(a, sym, b)
        entry = calc.history()[-1]
        print(f"  {entry}")

    print("\n  ── History ──────────────────────────")
    for i, h in enumerate(calc.history(), 1):
        print(f"  {i:>2}. {h}")

    print("\n  ─────────────────────────────────────")
    print("  Run  python calculator.py  for interactive mode.\n")


if __name__ == "__main__":
    import sys
    if "--demo" in sys.argv:
        display()
    else:
        run_repl()