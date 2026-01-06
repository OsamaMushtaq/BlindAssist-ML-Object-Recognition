"""
GSM Emergency Alert Module
Uses SIM900A to send emergency messages.
"""

def send_emergency_alert(phone_number, message):
    """
    Sends emergency SMS alert.
    """
    print(f"Sending emergency alert to {phone_number}")
    print(f"Message: {message}")
