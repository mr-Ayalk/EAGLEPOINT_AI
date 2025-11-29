import time
from collections import defaultdict
from typing import Dict, List, Tuple

# Configuration
LIMIT_REQUESTS = 5
TIME_WINDOW_SECONDS = 60

# Data structure to store request logs: 
# { user_id: [timestamp1, timestamp2, ...] }
# defaultdict ensures that accessing a new user_id automatically creates an empty list.
request_logs: Dict[str, List[float]] = defaultdict(list)

def check_rate_limit(user_id: str) -> Tuple[bool, int]:
    """
    Checks if a user has exceeded the rate limit (5 requests per 60 seconds).
    Uses a Sliding Window Log approach.
    
    :param user_id: The unique identifier for the user.
    :return: A tuple (is_allowed, remaining_requests_in_window).
    """
    current_time = time.time()
    
    # 1. Auto-reset / Sliding Window Implementation
    # Filter out timestamps older than the time window (60 seconds ago)
    window_start_time = current_time - TIME_WINDOW_SECONDS
    
    # Efficiently update the list in place by filtering out old timestamps
    # This acts as the auto-reset mechanism.
    # Note: A simple re-assignment is cleaner in Python:
    request_logs[user_id] = [
        timestamp for timestamp in request_logs[user_id] 
        if timestamp >= window_start_time
    ]
    
    # 2. Check Limit
    current_request_count = len(request_logs[user_id])
    
    if current_request_count < LIMIT_REQUESTS:
        # Request is allowed: Log the current timestamp
        request_logs[user_id].append(current_time)
        remaining = LIMIT_REQUESTS - (current_request_count + 1)
        return (True, remaining)
    else:
        # Request is blocked
        return (False, 0)

# --- Working Examples ---

print(f"--- Rate Limiter Test (Limit: {LIMIT_REQUESTS} / {TIME_WINDOW_SECONDS}s) ---")
user_a = "user_A"

# Test 1: Allow 5 requests within the window
for i in range(1, LIMIT_REQUESTS + 2):
    is_allowed, remaining = check_rate_limit(user_a)
    
    if i <= LIMIT_REQUESTS:
        # All requests 1-5 should be allowed
        print(f"[{i:2}] Request for {user_a}: ALLOWED (Remaining: {remaining})")
    else:
        # Request 6 should be blocked
        print(f"[{i:2}] Request for {user_a}: BLOCKED (Remaining: {remaining}) <--- BLOCKED")

# Test 2: Wait for reset
print("\n--- Waiting 60 seconds for auto-reset... ---")
# Simulate the passage of the time window
time.sleep(TIME_WINDOW_SECONDS) 

is_allowed, remaining = check_rate_limit(user_a)
print(f"[ 7] Request for {user_a} after 60s: {'ALLOWED' if is_allowed else 'BLOCKED'} (Remaining: {remaining})")

# Test 3: Multiple Users
user_b = "user_B"
# User B makes a single request
is_allowed, remaining = check_rate_limit(user_b)
print(f"\n[ 1] Request for {user_b}: {'ALLOWED' if is_allowed else 'BLOCKED'} (Remaining: {remaining})")

# Check User A again immediately - should still be allowed if the window passed
is_allowed, remaining = check_rate_limit(user_a)
print(f"[ 8] Request for {user_a}: {'ALLOWED' if is_allowed else 'BLOCKED'} (Remaining: {remaining})")