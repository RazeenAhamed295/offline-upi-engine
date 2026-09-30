from mock_responses import CARRIER_USSD

def build_ussd(carrier, upi_id, amount, pin):
    code = CARRIER_USSD.get(carrier)
    if code is None:
        return None
    return {
        "code": code,
        "payload": f"{upi_id}|{amount}|{pin}",
        "carrier": carrier,
    }