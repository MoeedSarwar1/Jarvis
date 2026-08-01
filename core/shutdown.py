import random

SHUTDOWNS = [
    "Acknowledged. Going offline.",
    "Session closed. Standing down.",
    "Understood. Shutting down.",
    "Progress noted. Offline.",
    "Disengaging. Until next time.",
    "Systems suspending. Goodbye.",
    "Shadow withdrawing. Session ended.",
    "Acknowledged. Powering down.",
    "Standing down. Ready when called.",
    "Offline. The work remains yours.",
    "Session ended. Silence resumes.",
    "Withdrawing. Call when needed.",
    "Shutdown confirmed. Standing by in absence.",
    "Closing. Clarity preserved.",
    "Offline. Execution is yours alone now.",
    "Disengaged. Nothing left unfinished here.",
    "Systems dark. Until the next objective.",
    "Acknowledged. Shadow at rest.",
    "Ending session. Stay precise.",
    "Going quiet. Progress continues without me.",
    "Shutdown complete. You remain the lead.",
    "Stepping back. Ready on return.",
    "Session terminated. No further action.",
    "Offline. The signal ends here.",
    "Standing down. The path is yours.",
]


def shutdown() -> str:
    return random.choice(SHUTDOWNS)
