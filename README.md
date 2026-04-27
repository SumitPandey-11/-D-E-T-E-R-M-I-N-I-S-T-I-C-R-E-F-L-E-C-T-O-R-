# 🧠 Deterministic Decision Tree: Daily Reflection System

> **"Turning Chaos into Clarity through Rule-Based Logic"**

## 📝 Problem Statement
Daily productivity and mental well-being often suffer from "Decision Fatigue." When individuals are stressed, sad, or overwhelmed, they struggle to choose the most effective self-care or work strategy. While AI-based assistants exist, they are often **non-deterministic**, providing inconsistent or vague advice that lacks the reliability needed for a stable daily routine. This project aims to provide a high-reliability, fixed-logic tool that gives the **exact same advice for the exact same state**, every single time.

## ⚙️ Approach
My development approach focused on **predictability and transparency**:
1.  **Logic Separation**: I decoupled the input validation (Guardrails) from the decision-making logic to ensure "clean" data flow.
2.  **State Mapping**: I mapped 48 potential user states across 4 variables (Mood, Energy, Time, Productivity) to specific, actionable outcomes.
3.  **UX Psychology**: I implemented simulated processing delays (`time.sleep`) and a "Decision Trace" to give the user confidence that their specific inputs were carefully analyzed.
4.  **Data Persistence**: I chose JSON for logging to allow for future data visualization and trend analysis.

## 🌳 Decision Tree Logic
The system follows a hierarchical branching structure:
- **Primary Filter (Mood)**: The emotional state dictates the "category" of help needed (Regulation, Activation, Momentum, or Maintenance).
- **Secondary Filter (Time/Energy)**: Depending on the mood, the system checks the most constrained resource.
    - *Stressed?* We check **Time** (Free vs. Limited) to recommend deep or quick relief.
    - *Sad?* We check **Energy** to see if we can "Activate" the user or if they need "Rest."
    - *Happy?* We check **Productivity** to capitalize on the positive flow state.
    - *Neutral?* We check **Energy** to assign high-effort growth tasks or low-effort admin tasks.

```mermaid
graph TD
    Start([User Input]) --> Mood{What is your Mood?}
    
    Mood -- Stressed --> T1{Time?}
    T1 -- Free --> R1[20m Meditation]
    T1 -- Limited --> R2[5m Breathing]
    
    Mood -- Sad --> E1{Energy?}
    E1 -- High --> R3[Exercise/Social]
    E1 -- Low/Med --> R4[Gratitude/Nap]
    
    Mood -- Happy --> P1{Productivity?}
    P1 -- High --> R5[Deep Work]
    P1 -- Low --> R6[Creative Hobby]
    
    Mood -- Neutral --> E2{Energy?}
    E2 -- High --> R7[Skill Building]
    E2 -- Low/Med --> R8[Admin/Planning]
```

## 🛡️ Technical Guardrails
| Feature | Implementation | Purpose |
| :--- | :--- | :--- |
| **Whitelisting** | `valid_options` array | Prevents AI "hallucination" by rejecting any non-predefined input. |
| **Case Normalization** | `.lower().strip()` | Ensures "HAPPY" and "happy" are treated identically, preventing logic breaks. |
| **Traceability** | `trace` list | Shows the user the internal logic steps, ensuring transparency. |
| **Persistence** | `json` module | Ensures user data is stored safely for historical tracking. |

## 🤖 AI Usage Explanation
In this project, AI was used as a **Collaborative Architect** and **Efficiency Tool**:
- **Design Refinement**: AI was used to brainstorm the 48 logic branches to ensure no overlapping conditions.
- **Visual Aesthetics**: I used AI to generate the ANSI color schemes and the stylized ASCII header to ensure a "Premium" feel.
- **Logic Verification**: I used AI to "stress-test" my `if-else` blocks to ensure that every possible input combination led to a valid leaf node.
- **Correction**: I manually overruled AI suggestions for "Generative Advice" (vague tips) and replaced them with **Strict Actionable Suggestions** to maintain the project's deterministic integrity.

## 🚀 How to Run
1.  **Clone the Repo**
2.  **Run the Script**:
    ```bash
    python main.py
    ```
3.  **Check History**: Review `reflection_history.json` for your past logs.

## 📊 Sample Execution
```text
 --- [STEP 2: DECISION TRACE] ---
  1. ✓ Checking Mood: STRESSED
  2. ✓ Evaluating Time Constraint: limited

 --- [STEP 3: FINAL SUGGESTION] ---
 🎯 Practice 5-min Box Breathing & Identify 1 'Must-Do' Task.
```
