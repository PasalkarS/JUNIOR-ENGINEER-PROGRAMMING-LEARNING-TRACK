# Topic 03: Inheritance vs Composition
# Demonstrates both inheritance and composition in notification systems.

# --- APPROACH A: Polymorphic Inheritance ---
class BaseNotifier:
    def __init__(self, sender_name: str):
        self.sender_name = sender_name

    def send(self, recipient: str, message: str) -> None:
        raise NotImplementedError("Subclasses must implement send().")

class EmailNotifier(BaseNotifier):
    def send(self, recipient: str, message: str) -> None:
        print(f"[EMAIL] From: {self.sender_name} To: <{recipient}> | {message}")

class SMSNotifier(BaseNotifier):
    def send(self, recipient: str, message: str) -> None:
        print(f"[SMS] From: {self.sender_name} To: [{recipient}] | {message}")

# --- APPROACH B: Composition (Preferred) ---
# AlertManager HAS-A list of notification channels (loose coupling!)
class AlertManager:
    def __init__(self, channels: list[BaseNotifier]):
        self.channels = channels

    def broadcast_alert(self, recipient: str, message: str):
        print(f"\n--- Broadcasting Alert to {recipient} ---")
        for channel in self.channels:
            channel.send(recipient, message)

if __name__ == "__main__":
    email_channel = EmailNotifier("Company Alerts")
    sms_channel = SMSNotifier("9900")

    # Composite manager assembled with interchangeable channels
    alert_mgr = AlertManager([email_channel, sms_channel])
    alert_mgr.broadcast_alert("admin@company.com", "Database failover initiated.")
