# ============================================================
# Assignment No  : 05
# Title          : Elementary Chatbot for Customer Interaction
# Problem        : Rule-based chatbot using regex pattern
#                  matching for PCCOER college helpdesk.
# Subject        : Lab Practice II (310258) - AI | PCCOER
# CO Mapping     : C318.3
# ============================================================

import re, random

# ─── Knowledge Base (pattern → responses) ──────────────────

KB = [
    (r"\bhello\b|\bhi\b|\bhey\b", [
        "Hello! Welcome to PCCOER Helpdesk. How can I help you?",
        "Hi! I'm PCBOT, your PCCOER virtual assistant. What do you need?",
    ]),
    (r"\bbye\b|\bgoodbye\b|\bexit\b|\bquit\b", [
        "Goodbye! Have a great day!",
        "Bye! Feel free to return anytime.",
    ]),
    (r"\bname\b|\bwho are you\b", [
        "I'm PCBOT — the virtual assistant for PCCOER, Ravet, Pune.",
    ]),
    (r"\badmission\b|\bapply\b|\benroll\b", [
        "Admissions are via DTE Maharashtra portal. Visit pccoer.edu.in for eligibility and important dates.",
        "For admission queries, contact: admissions@pccoer.edu.in or call 020-XXXXXXXX.",
    ]),
    (r"\bfee\b|\bfees\b|\btuition\b|\bpayment\b", [
        "Fee structure varies by program. Check pccoer.edu.in → Academics → Fees.",
        "Contact the accounts department for exact fee details.",
    ]),
    (r"\bhostel\b|\baccommodation\b|\broom\b", [
        "PCCOER has separate hostels for boys and girls. Contact the warden for seat availability.",
        "On-campus hostel is available! Reach the admin office for room allocation.",
    ]),
    (r"\bexam\b|\btimetable\b|\bschedule\b|\bhall ticket\b", [
        "Exam schedules and hall tickets are on the ERP portal (erp.pccoer.edu.in).",
        "Check the official notice board or ERP system for your timetable.",
    ]),
    (r"\blibrary\b|\bbooks?\b|\breference\b", [
        "Library is open 8 AM–8 PM (weekdays). Borrow up to 3 books with your student ID.",
        "Digital library (NPTEL, NDLI) is accessible 24×7 via institutional login.",
    ]),
    (r"\bplacement\b|\bjob\b|\bcareer\b|\brecruit\b", [
        "PCCOER has an active Training & Placement cell. Top companies visit for campus drives.",
        "For placement info, contact the T&P officer or visit the placement portal.",
    ]),
    (r"\bwifi\b|\binternet\b|\bnetwork\b", [
        "Campus-wide Wi-Fi is available. Use your ERP login credentials to connect.",
        "For connectivity issues, contact IT Support: itsupport@pccoer.edu.in.",
    ]),
    (r"\bcourse\b|\bbranch\b|\bdepartment\b|\bprogram\b", [
        "PCCOER offers BE, ME, MBA and PhD in CS, IT, Mechanical, Civil, ENTC, and more.",
        "Visit pccoer.edu.in/departments for the full list of programs.",
    ]),
    (r"\btransport\b|\bbus\b|\bconveyance\b", [
        "PCCOER provides transport from multiple routes. Contact the transport office for details.",
        "Bus routes and timings are available at the admin office.",
    ]),
    (r"\bscholarship\b|\bfinancial aid\b|\bwaiver\b", [
        "Government scholarships are available via mahadbt.gov.in. Contact the student welfare desk.",
    ]),
    (r"\bthank\b|\bthanks\b", [
        "You're welcome! Anything else I can help with?",
        "Happy to help! Feel free to ask more.",
    ]),
    (r"\bhelp\b|\bwhat can you\b|\bsupport\b", [
        "I can assist with: Admissions, Fees, Hostel, Exams, Library, Placements, Wi-Fi, Transport, Scholarships.",
    ]),
]

DEFAULT = [
    "I'm sorry, I didn't understand that. Could you rephrase?",
    "That's outside my knowledge. Please contact the admin office.",
    "Try asking about: admissions, fees, hostel, exams, or placements.",
]

# ─── Inference Engine ───────────────────────────────────────

def respond(user_input):
    text = user_input.lower().strip()
    for pattern, replies in KB:
        if re.search(pattern, text):
            return random.choice(replies)
    return random.choice(DEFAULT)

def is_exit(text):
    return bool(re.search(r"\bbye\b|\bgoodbye\b|\bexit\b|\bquit\b", text.lower()))


# ─── Main ───────────────────────────────────────────────────

if __name__ == "__main__":
    print("╔" + "═"*52 + "╗")
    print("║    PCBOT — PCCOER Virtual Helpdesk Chatbot       ║")
    print("║    Lab Practice II (310258) - AI | PCCOER        ║")
    print("╠" + "═"*52 + "╣")
    print("║  Type 'help' to see what I can assist with.      ║")
    print("║  Type 'bye'  to end the conversation.            ║")
    print("╚" + "═"*52 + "╝")
    print()
    print("PCBOT: Hello! I'm PCBOT, your PCCOER virtual assistant.")
    print("       How can I help you today?")
    print()

    while True:
        try:
            user = input("You  : ").strip()
            if not user:
                continue
            reply = respond(user)
            print(f"PCBOT: {reply}")
            print()
            if is_exit(user):
                break
        except (KeyboardInterrupt, EOFError):
            print("\nPCBOT: Session ended. Goodbye!")
            break

    print("─" * 54)
    print("Chatbot types: Rule-Based (pattern matching)")
    print("Approach     : Knowledge Base + Regex Inference Engine")
    print("Conclusion   : Elementary chatbot developed for PCCOER helpdesk.")
