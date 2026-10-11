# Test Log — Aegis Breach: Operation Nightfall

## Full playthrough test (all 6 stages)
- Date: 2026-10-10
- Tester: Hettiarachchi T.J.
- Result: PASS — all 6 flags recovered in sequence via intended solution path

## Isolation tests
- Stage 3 -> Stage 6 container: PASS (unreachable)
- Stage 6 -> Stage 3 container: PASS (unreachable)
- Stage 3 -> Internet: FAIL (reachable) — known limitation, documented in README

## Reset tests
- reset_stage3.sh: PASS — rebuilt cleanly, SQLi exploit confirmed working after reset
- reset_stage6.sh: PASS — rebuilt cleanly, privilege escalation confirmed working after reset

## Exploit/solver script validation
- solve_sqli.py: PASS — flag AEGIS{auth_bypass_1nj3ct3d} recovered automatically
- exploit_stage6.py: PASS — flag AEGIS{root_access_granted} recovered automatically
- isolation_scan.py: PASS (2/3) — one known limitation documented above
