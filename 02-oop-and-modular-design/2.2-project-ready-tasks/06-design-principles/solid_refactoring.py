# Topic 06: SOLID Design Principles Refactoring
# Demonstrates refactoring code that violates Single Responsibility & Dependency Inversion.

# --- BAD DESIGN (Violates SRP & DIP) ---
# A single class handles calculation, persistence, and output formatting.
class BadOrderManager:
    def process_order(self, customer: str, amount: float):
        total = amount * 1.08  # calculation
        with open("orders_log.txt", "a") as f:  # hardcoded I/O
            f.write(f"{customer},{total}\n")
        print(f"Sent email receipt to {customer} for ${total:.2f}")  # output

# --- IMPROVED CLEAN DESIGN (Honors SOLID) ---
class OrderCalculator:
    """SRP: Only calculates pricing and tax."""
    @staticmethod
    def calculate_total(amount: float, tax_rate: float = 0.08) -> float:
        return round(amount * (1 + tax_rate), 2)

class OrderLogger:
    """SRP: Only handles persistence logging."""
    def __init__(self):
        self.logs = []

    def log_order(self, customer: str, total: float):
        self.logs.append(f"{customer}: ${total:.2f}")

class OrderNotification:
    """SRP: Only handles notifications."""
    @staticmethod
    def send_confirmation(customer: str, total: float):
        print(f"[CONFIRMATION] Customer '{customer}' charged ${total:.2f}")

class OrderProcessor:
    """DIP: Glues together injected dependencies."""
    def __init__(self, calculator: OrderCalculator, logger: OrderLogger, notifier: OrderNotification):
        self.calc = calculator
        self.logger = logger
        self.notifier = notifier

    def process(self, customer: str, amount: float) -> float:
        total = self.calc.calculate_total(amount)
        self.logger.log_order(customer, total)
        self.notifier.send_confirmation(customer, total)
        return total

if __name__ == "__main__":
    processor = OrderProcessor(OrderCalculator(), OrderLogger(), OrderNotification())
    processor.process("Bob", 150.0)
    print("Recorded logs:", processor.logger.logs)
