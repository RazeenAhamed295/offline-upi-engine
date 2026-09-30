import re

def parse_response(raw):
    if "Successful" in raw:
        txn = re.search(r"Txn ID:\s*(\w+)", raw)
        amt = re.search(r"Amount:\s*Rs\.?(\d+)", raw)
        bal = re.search(r"Balance:\s*Rs\.?(\d+)", raw)
        return {
            "status": "success",
            "txn_id": txn.group(1) if txn else None,
            "amount": amt.group(1) if amt else None,
            "balance": bal.group(1) if bal else None,
        }
    return {
        "status": "failed",
        "reason": raw.strip(),
    }