\# Offline UPI Reliability Engine



Handles USSD/UPI payment flow when there's no internet.



\## Flow

1\. Build USSD request per carrier

2\. Fallback: \*99# → 123Pay → SMS

3\. Parse response

4\. Log every attempt



\## Run

python demo.py



\## Data needed

Replace strings in mock\_responses.py with real USSD responses.

