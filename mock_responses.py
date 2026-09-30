# Mock USSD responses based on public NPCI *99# flow
# Replace strings here when teammates capture real responses

MOCK_RESPONSES = {
    "success": "Transaction Successful. Txn ID: {txn_id}. Amount: Rs.{amount}. Balance: Rs.{balance}",
    "wrong_pin": "Transaction Failed. Reason: Invalid MPIN. Please try again.",
    "invalid_vpa": "Transaction Failed. Reason: Invalid UPI ID.",
    "timeout": "Transaction Failed. Reason: No response from bank. Try again.",
    "insufficient": "Transaction Failed. Reason: Insufficient balance.",
}

CARRIER_USSD = {
    "airtel": "*99#",
    "vi": "*99#",
    "bsnl": "*99#",
    "jio": None,  # unsupported — triggers fallback
}