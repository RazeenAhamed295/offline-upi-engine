from engine.fallback import fallback_chain
from engine.parse import parse_response
from engine.log import log_attempt
from mock_responses import MOCK_RESPONSES

def run_demo():
    carrier = "airtel"
    upi_id = "user@upi"
    amount = 500
    pin = "1234"

    chain = fallback_chain(carrier, upi_id, amount, pin)

    for method, req in chain:
        print(f"Trying {method}...")
        if method == "123pay_ivr":
            raw = MOCK_RESPONSES["success"].format(
                txn_id="TXN12345", amount=amount, balance=15000
            )
            result = parse_response(raw)
            log_attempt(carrier, method, result["status"])
            print(f"  -> {result}")
            break
        else:
            log_attempt(carrier, method, "failed", "unsupported")
            print("  -> failed, falling back")

if __name__ == "__main__":
    run_demo()