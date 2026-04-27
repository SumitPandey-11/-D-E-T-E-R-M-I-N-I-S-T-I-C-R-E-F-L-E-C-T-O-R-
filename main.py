import time
import json
import os
from datetime import datetime

# --- UI CONSTANTS (ANSI COLORS) ---
BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

BANNER = f"""
{CYAN}{BOLD}
╔══════════════════════════════════════════════════════════╗
║        D E T E R M I N I S T I C   R E F L E C T O R     ║
║            Professional Decision Support System          ║
╚══════════════════════════════════════════════════════════╝
{RESET}"""

def log_reflection(data, result):
    """Saves the reflection session to a local JSON file."""
    log_file = "reflection_history.json"
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "inputs": data,
        "suggestion": result
    }
    
    history = []
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            try: history = json.load(f)
            except: history = []
            
    history.append(entry)
    with open(log_file, "w") as f:
        json.dump(history, f, indent=4)

def get_reflection_logic(mood, energy, time_avail, prod):
    """
    Core Deterministic Engine with 'Decision Trace'.
    Returns (Suggestion, Trace_Steps)
    """
    trace = [f"Checking Mood: {mood.upper()}"]
    
    if mood == "stressed":
        trace.append(f"Evaluating Time Constraint: {time_avail}")
        if time_avail == "free":
            return "Conduct a 20-min Guided Meditation & Stress Journaling.", trace
        return "Practice 5-min Box Breathing & Identify 1 'Must-Do' Task.", trace

    elif mood == "sad":
        trace.append(f"Evaluating Energy Levels: {energy}")
        if energy == "high":
            return "Engage in 15-min Brisk Exercise or Call a Trusted Friend.", trace
        return "Write 3 Gratitude Points & Take a 30-min Power Nap.", trace

    elif mood == "happy":
        trace.append(f"Evaluating Productivity State: {prod}")
        if prod == "high":
            return "Capitalize on flow: Tackle your 'Deep Work' or most challenging project task.", trace
        return "Energy boost: Plan a Social Celebration or Treat Yourself to a Creative Hobby.", trace

    elif mood == "neutral":
        trace.append(f"Evaluating Energy Reserves: {energy}")
        if energy == "high":
            return "Optimization Mode: Focus on Skill Building or Learning a New Concept.", trace
        return "Maintenance Mode: Perform 'Admin' tasks like Inbox Zero or Calendar planning.", trace

    return "Unknown configuration.", trace

def validate(prompt, options, field_name):
    while True:
        val = input(f"{BOLD}{prompt}{RESET} ({'/'.join(options)}): ").strip().lower()
        if not val:
            print(f"{RED}⚠ Error: {field_name} cannot be empty.{RESET}")
            continue
        if val in options:
            return val
        print(f"{RED}⚠ '{val}' is invalid. Please choose from {options}.{RESET}")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BANNER)
    
    # 1. Structured Input Collection
    print(f"{YELLOW}--- [STEP 1: DATA COLLECTION] ---{RESET}")
    mood = validate("Current Mood  ", ["happy", "sad", "stressed", "neutral"], "Mood")
    energy = validate("Energy Level  ", ["high", "medium", "low"], "Energy")
    time_avail = validate("Time Available", ["free", "limited"], "Time")
    prod = validate("Productivity  ", ["high", "low"], "Productivity")

    # 2. Simulated Processing (For UX "Weight")
    print(f"\n{CYAN}⚙ Analyzing inputs against Deterministic Rule-Set...{RESET}")
    time.sleep(1.2)

    # 3. Decision Execution
    result, trace = get_reflection_logic(mood, energy, time_avail, prod)

    # 4. Professional Output Display
    print(f"\n{YELLOW}--- [STEP 2: DECISION TRACE] ---{RESET}")
    for i, step in enumerate(trace):
        print(f" {i+1}. {GREEN}✓{RESET} {step}")

    print(f"\n{YELLOW}--- [STEP 3: FINAL SUGGESTION] ---{RESET}")
    print(f"{BLUE}╔" + "═"*60 + "╗")
    print(f"║ {BOLD}{result.center(58)}{RESET} ║")
    print(f"╚" + "═"*60 + "╝{RESET}")

    # 5. Data Persistence
    log_reflection({"mood": mood, "energy": energy, "time": time_avail, "prod": prod}, result)
    print(f"\n{GREEN}💾 Session logged to 'reflection_history.json'.{RESET}")
    print(f"{CYAN}Ready for next entry.{RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}Process terminated by user.{RESET}")
