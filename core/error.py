import random

ERRORS = [
    "Connection lost. Retrying is not automatic.",
    "Signal dropped. Awaiting recovery.",
    "Something broke. Diagnosing.",
    "Response failed. Try again shortly.",
    "Link interrupted. Check the connection.",
    "System fault. Continuing is unsafe.",
    "Unable to reach the model. Standing by.",
    "Request failed. No response received.",
    "Something went wrong upstream.",
    "The connection did not hold.",
]


def error() -> str:
    return random.choice(ERRORS)
