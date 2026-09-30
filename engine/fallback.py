from engine.build_ussd import build_ussd

def fallback_chain(carrier, upi_id, amount, pin):
    attempts = []

    # Step 1: *99#
    req = build_ussd(carrier, upi_id, amount, pin)
    if req:
        attempts.append(("ussd_99", req))

    # Step 2: 123Pay IVR
    attempts.append(("123pay_ivr", {"carrier": carrier, "upi_id": upi_id}))

    # Step 3: SMS fallback
    attempts.append(("sms", {"carrier": carrier, "upi_id": upi_id}))

    return attempts