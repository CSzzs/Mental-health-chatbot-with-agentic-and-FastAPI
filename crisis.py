from typing import List

CRISIS_KEYWORDS: List[str] = [
    "suicidel", "Suicide", "kill my self", "want to die", "hopeless", "worthless",
    "can't go on", "give up", "ending it all", "no reason to live"
]

SAFETY_MESSAGES = (
    "it sounds like you're going thorough a relly tough time."
    "You're not alone, and there are people who want to help you."
    "Plese consider reaching out to a mental health professional or contacting a helpline:\n\n"
    "**Sri Lanka:** 1333 (Courage Commitment Compassion), 0707308308 (Sri Lanka Sumithrayo)\n"
    "**USA:** 988 (Suicide and Crisis Lifeline)\n"
    "**UK:** 116 123 (Samaritans)"
    "You matter. 🩵"
)

def contains_crisis_keyword(text: str) -> bool:
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in CRISIS_KEYWORDS)