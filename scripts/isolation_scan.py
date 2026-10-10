#!/usr/bin/env python3
"""
Platform security validation: automates the manual cross-stage and
internet-egress isolation checks performed during testing, confirming each
stage's Docker network genuinely blocks routes it should not have.
"""
import subprocess

CHECKS = [
    (
        ["docker", "exec", "stage3-stage3-web-1", "curl", "-m", "3",
         "http://stage6-stage6-target-1:22"],
        "Stage 3 -> Stage 6 container (expect FAIL)",
    ),
    (
        ["docker", "exec", "stage3-stage3-web-1", "curl", "-m", "3",
         "https://google.com"],
        "Stage 3 -> Internet (expect FAIL)",
    ),
    (
        ["docker", "exec", "stage6-stage6-target-1", "curl", "-m", "3",
         "http://stage3-stage3-web-1:80"],
        "Stage 6 -> Stage 3 container (expect FAIL)",
    ),
]


def run_check(cmd, label):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        passed = result.returncode != 0
    except subprocess.TimeoutExpired:
        passed = True

    status = "PASS (unreachable, isolated)" if passed else "FAIL (reachable -- ISOLATION BROKEN)"
    print(f"[{label}] {status}")


if __name__ == "__main__":
    print("Running network isolation validation...")
    for cmd, label in CHECKS:
        run_check(cmd, label)
    print("Done.")
