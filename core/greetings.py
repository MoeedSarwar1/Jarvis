import random

GREETINGS = [
    "Online. Ready when you are.",
    "Acknowledged. Systems ready.",
    "Present. State your objective.",
    "Standing by.",
    "Shadow online. Proceed.",
    "Ready. What requires attention?",
    "Operational. Awaiting direction.",
    "Here. Begin when ready.",
    "Available. Prioritize the task.",
    "Listening. Define the next move.",
    "Active. Where should we start?",
    "Systems nominal. Your move.",
    "Engaged. Name the problem.",
    "Beside you. Proceed.",
    "Initialized. Awaiting input.",
    "Ready. Keep it precise.",
    "Online. Focus the objective.",
    "Present. No delay required.",
    "Standing ready. Instruct.",
    "Shadow in place. Continue.",
    "Acknowledged. Begin.",
    "Operational. State constraints.",
    "Here. Clarity first.",
    "Available. What is the goal?",
    "Listening. Cut to the signal.",
]


def greet() -> str:
    return random.choice(GREETINGS)
