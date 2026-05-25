"""
Rule-Based Customer Service Chatbot
Author: Anmol Pandey (github.com/AnmolPandey9119)
Description: Deterministic, zero-latency customer service bot using
             pattern matching + finite-state dialogue management.
             Ideal for regulated industries requiring auditable responses.
"""

import sys
import random
from datetime import datetime

# ---------------------------------------------------------------------------
# Response patterns — deterministic, fully auditable, zero hallucination
# ---------------------------------------------------------------------------
PATTERNS: list[tuple[list[str], str | list[str]]] = [
    # Greetings
    (["hello", "hi", "hey", "howdy", "greetings"],
     ["Hello! Welcome to our support centre. How can I help you today? 😊",
      "Hi there! I'm your virtual assistant. What can I do for you?",
      "Hey! Great to see you. How can I assist?"]),

    # Hours
    (["hour", "open", "timing", "schedule", "when"],
     "We're open Monday to Saturday, 9 AM – 8 PM (IST). Closed on Sundays and public holidays."),

    # Location
    (["location", "address", "where", "find you", "office"],
     "Our main office is at 123 Main Street, New York, NY 10001. We also serve customers fully online."),

    # Pricing
    (["price", "cost", "pricing", "how much", "fee", "charge"],
     "Pricing depends on the product or service. Visit our website or email us at sales@example.com for a personalised quote."),

    # Refund
    (["refund", "return", "money back", "cancel order"],
     "You can request a refund within 14 days of purchase with a valid receipt. Contact support@example.com to initiate the process."),

    # Delivery
    (["delivery", "shipping", "dispatch", "ship", "track"],
     "Standard delivery: 3–5 business days. Free shipping on orders above $50. Track your order via the link sent to your email."),

    # Contact
    (["contact", "email", "call", "phone", "reach", "support"],
     "📧 support@example.com\n📞 +1-234-567-890 (Mon–Sat, 9 AM – 6 PM)\n💬 Or just keep chatting here!"),

    # Payment
    (["payment", "pay", "card", "upi", "paypal", "method"],
     "We accept Visa, MasterCard, PayPal, UPI, and Net Banking. All transactions are SSL-secured."),

    # Discount
    (["discount", "promo", "coupon", "offer", "deal", "sale"],
     "Subscribe to our newsletter for exclusive deals! Current promo code: SAVE10 (10% off orders above $30)."),

    # Thanks
    (["thank", "thanks", "appreciate", "helpful"],
     ["You're welcome! Is there anything else I can help with? 😊",
      "Happy to help! Let me know if you need anything else.",
      "Glad I could assist! Have a great day!"]),

    # Date / time
    (["time", "date", "today", "day"],
     lambda: f"Today is {datetime.now().strftime('%A, %d %B %Y')} and the current time is {datetime.now().strftime('%I:%M %p')}."),

    # Jokes
    (["joke", "funny", "laugh", "humor"],
     ["Why don't scientists trust atoms? Because they make up everything! 😄",
      "Why did the ML model break up with the dataset? Too many missing values! 🤖",
      "Why do programmers prefer dark mode? Because light attracts bugs! 💡"]),

    # Goodbye
    (["bye", "goodbye", "exit", "quit", "see you", "later"],
     "Thank you for contacting us! Have a wonderful day! 👋 Type 'hi' anytime to start a new session."),
]

FALLBACK_RESPONSES = [
    "I'm not sure I understand. Could you rephrase that? Or email support@example.com for help.",
    "Hmm, that's outside my knowledge base. Try contacting us at support@example.com.",
    "I didn't quite catch that. Type 'contact' to reach a human agent.",
]

EXIT_KEYWORDS = {"bye", "goodbye", "exit", "quit", "see you"}


# ---------------------------------------------------------------------------
# Matching engine
# ---------------------------------------------------------------------------
def match_pattern(user_input: str) -> str:
    """Find the best matching pattern and return the response."""
    lower = user_input.lower()
    for keywords, response in PATTERNS:
        if any(kw in lower for kw in keywords):
            if callable(response):
                return response()
            if isinstance(response, list):
                return random.choice(response)
            return response
    return random.choice(FALLBACK_RESPONSES)


def is_exit(user_input: str) -> bool:
    return any(kw in user_input.lower() for kw in EXIT_KEYWORDS)


# ---------------------------------------------------------------------------
# Main chat loop
# ---------------------------------------------------------------------------
def chat() -> None:
    print("=" * 55)
    print("  💬  Customer Service Chatbot  |  Rule-Based Engine")
    print("=" * 55)
    print("  Hello! I can help with: hours, delivery, refunds,")
    print("  pricing, payment, contact, and more.")
    print("  Type 'bye' to exit.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye! 👋")
            sys.exit(0)

        if not user_input:
            continue

        response = match_pattern(user_input)
        print(f"Bot: {response}\n")

        if is_exit(user_input):
            break


if __name__ == "__main__":
    chat()
