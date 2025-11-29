import time
from collections import defaultdict
from typing import Dict, List, Tuple

# Simple sliding-window rate limiter:
# Allow 5 requests per user every 60 seconds.

MAX_REQUESTS = 5
WINDOW_SECONDS = 60

# Store timestamps of each user's requests
request_history: Dict[str, List[float]] = defaultdict(list)


def check_rate_limit(user_id: str) -> Tuple[bool, int]:
    """
    Returns whether the user is allowed to make a request.
    Uses a sliding window by cleaning out old timestamps.
    """
    now = time.time()
    window_start = now - WINDOW_SECONDS

    # Remove timestamps older than the sliding window
    request_history[user_id] = [
        ts for ts in request_history[user_id] if ts >= window_start
    ]

    used = len(request_history[user_id])

    if used < MAX_REQUESTS:
        # Log this request
        request_history[user_id].append(now)
        remaining = MAX_REQUESTS - (used + 1)
        return True, remaining

    return False, 0


# ------------------------------------------------------------------

print(f"--- Rate Limiter Demo ({MAX_REQUESTS} requests / {WINDOW_SECONDS} seconds) ---")

user = "user_A"

# Test 1: user makes 6 requests back-to-back
for i in range(1, MAX_REQUESTS + 2):
    ok, remaining = check_rate_limit(user)
    status = "ALLOWED" if ok else "BLOCKED"

    print(f"[{i}] {status} (remaining: {remaining})")

# Test 2: wait for the window to clear
print("\nWaiting for the time window to expire...\n")
time.sleep(WINDOW_SECONDS)

ok, remaining = check_rate_limit(user)
print(f"After waiting: {'ALLOWED' if ok else 'BLOCKED'} (remaining: {remaining})")

# Test 3: another user
other_user = "user_B"
ok, remaining = check_rate_limit(other_user)
print(f"\nUser B request: {'ALLOWED' if ok else 'BLOCKED'} (remaining: {remaining})")

# User A should also work again after the wait
ok, remaining = check_rate_limit(user)
print(f"User A request: {'ALLOWED' if ok else 'BLOCKED'} (remaining: {remaining})")
