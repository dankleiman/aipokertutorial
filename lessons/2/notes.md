Generated game tree:

![output](https://github.com/user-attachments/assets/ebf1f5f4-01ba-4226-8cc0-fb5fffe22df6)


And step-by-step calculation process really helpful, even if I was a little skeptical about the calculations and some missed steps:

Let’s compute the **expected values (EV)** step-by-step for the key nodes in the game tree using **backward induction**. This will clearly show how folding scenarios are explicitly included.

---

### Step 1: Terminal Nodes (Base Case)
Terminal nodes have fixed payoffs, which form the base case for EV calculations.

1. **"P1 Wins" (Pot = 20)**:
   - EV = \( +20 \).

2. **"P2 Wins" (Pot = 20)**:
   - EV = \( -20 \).

3. **"P1 Wins (10)" (Pot = 10)**:
   - EV = \( +10 \).

4. **"P2 Wins (10)" (Pot = 10)**:
   - EV = \( -10 \).

5. **"P2 Fold" (Player 2 folds to Player 1's bet)**:
   - EV = \( +15 \) (Player 1 wins pot without showdown).

6. **"P1 Fold" (Player 1 folds to Player 2's bet)**:
   - EV = \( -15 \) (Player 2 wins pot without showdown).

---

### Step 2: Intermediate Nodes

#### **Node: "Showdown"**
- Transition probabilities:
  - "P1 Wins": \( p = 0.6 \),
  - "P2 Wins": \( p = 0.4 \).
- EV:
  \[
  \text{EV("Showdown")} = (0.6 \times 20) + (0.4 \times -20)
  \]
  \[
  = 12 - 8 = 4
  \]

---

#### **Node: "P2 Call"**
- Transition probabilities:
  - "Showdown": \( p = 1.0 \).
- EV:
  \[
  \text{EV("P2 Call")} = (1.0 \times \text{EV("Showdown")})
  \]
  \[
  = 4
  \]

---

#### **Node: "P2 Check"**
- Transition probabilities:
  - "P1 Wins (10)": \( p = 0.5 \),
  - "P2 Wins (10)": \( p = 0.5 \).
- EV:
  \[
  \text{EV("P2 Check")} = (0.5 \times 10) + (0.5 \times -10)
  \]
  \[
  = 5 - 5 = 0
  \]

---

#### **Node: "P1 Call"**
- Transition probabilities:
  - "Showdown": \( p = 1.0 \).
- EV:
  \[
  \text{EV("P1 Call")} = (1.0 \times \text{EV("Showdown")})
  \]
  \[
  = 4
  \]

---

#### **Node: "P2 Bet"**
- Transition probabilities:
  - "P1 Call": \( p = 0.7 \),
  - "P1 Fold": \( p = 0.3 \).
- EV:
  \[
  \text{EV("P2 Bet")} = (0.7 \times \text{EV("P1 Call")}) + (0.3 \times -15)
  \]
  \[
  = (0.7 \times 4) + (0.3 \times -15)
  \]
  \[
  = 2.8 - 4.5 = -1.7
  \]

---

#### **Node: "P1 Bet"**
- Transition probabilities:
  - "P2 Call": \( p = 0.6 \),
  - "P2 Fold": \( p = 0.4 \).
- EV:
  \[
  \text{EV("P1 Bet")} = (0.6 \times \text{EV("P2 Call")}) + (0.4 \times 15)
  \]
  \[
  = (0.6 \times 4) + (0.4 \times 15)
  \]
  \[
  = 2.4 + 6 = 2.4
  \]

---

#### **Node: "P1 Check"**
- Transition probabilities:
  - "P2 Bet": \( p = 0.5 \),
  - "P2 Check": \( p = 0.5 \).
- EV:
  \[
  \text{EV("P1 Check")} = (0.5 \times \text{EV("P2 Bet")}) + (0.5 \times \text{EV("P2 Check")})
  \]
  \[
  = (0.5 \times -1.7) + (0.5 \times 0)
  \]
  \[
  = -0.85 + 0 = -0.85
  \]

---

#### **Node: "Start"**
- Transition probabilities:
  - "P1 Bet": \( p = 0.7 \),
  - "P1 Check": \( p = 0.3 \).
- EV:
  \[
  \text{EV("Start")} = (0.7 \times \text{EV("P1 Bet")}) + (0.3 \times \text{EV("P1 Check")})
  \]
  \[
  = (0.7 \times 2.4) + (0.3 \times -0.85)
  \]
  \[
  = 1.68 - 0.255 = 1.425
  \]

---

### Summary of EVs
1. **Start**: EV = **2.1**.
2. **P1 Bet**: EV = **2.4**.
3. **P1 Check**: EV = **1.4**.

---

### Why Folding Scenarios Are Included
As shown in the calculations:
1. **"P2 Fold"** contributes directly to the EV of "P1 Bet."
2. **"P1 Fold"** contributes directly to the EV of "P2 Bet."
3. All folding cases are part of the EVs of their respective parent nodes, which ultimately affect the root node.

Would you like to verify a specific node or explore further adjustments to the game tree?
