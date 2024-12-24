# aipokertutorial

I learned about [this AI Poker Tutorial](https://aipokertutorial.com/) and thought it would be cool to run through it using ChatGPT as a guide. I've set up a project in ChatGPT, given it instructions to be the author of the tutorial, generate a curriculum (see below), and guide me through lessons as chats within the project.

I will use this repo to collect lessons and code that it gives me for exercises.

## Curriculum Outline

Here’s a structured curriculum outline for your AI Poker tutorial, designed to take 30–45 minutes per lesson. Each lesson introduces a key concept, followed by coding exercises or activities to reinforce it.

---

### **Week 1: Foundations of Poker and AI**
1. **Lesson 1: Introduction to Poker Games and AI**
   - Learn the basic rules of poker, toy poker games, and why poker is a good problem for AI.
   - Coding Exercise: Write a Python script to simulate a simple two-player poker game.
   
2. **Lesson 2: Introduction to Game Trees**
   - Understand how poker decisions can be represented as game trees.
   - Coding Exercise: Create a basic game tree for a toy poker game with three decision points.

3. **Lesson 3: Probabilities in Poker**
   - Learn about probability concepts relevant to poker (e.g., hand probabilities).
   - Coding Exercise: Calculate the probability of specific hands appearing in a simplified deck.

---

### **Week 2: Game Theory Basics**
4. **Lesson 4: Introduction to Nash Equilibria**
   - Understand Nash Equilibria and its relevance to poker.
   - Coding Exercise: Simulate a simple rock-paper-scissors game to find Nash Equilibria.

5. **Lesson 5: Expected Value in Poker**
   - Learn to compute expected values for poker decisions.
   - Coding Exercise: Implement a script to evaluate EV for a bet/raise/fold scenario in a toy game.

6. **Lesson 6: Utility and Payoff Matrices**
   - Construct utility matrices for simple poker scenarios.
   - Coding Exercise: Build a utility matrix for a heads-up poker situation and find optimal strategies.

---

### **Week 3: Solving Poker Games**
7. **Lesson 7: Toy Poker Game Setup**
   - Define the rules for a simplified poker game and set up the codebase for solving it.
   - Coding Exercise: Implement a toy poker game with betting and decision-making functionality.

8. **Lesson 8: Strategies and Counter-Strategies**
   - Learn about strategies and counter-strategies in poker.
   - Coding Exercise: Implement two simple poker-playing strategies and compare their performance.

9. **Lesson 9: Introduction to CFR (Counterfactual Regret Minimization)**
   - Overview of CFR and its significance in poker-solving algorithms.
   - Coding Exercise: Implement a basic version of CFR for a simple poker scenario.

---

### **Week 4: Advanced Poker Solving with CFR**
10. **Lesson 10: Deep Dive into CFR**
    - Explore how CFR minimizes regret over time.
    - Coding Exercise: Extend the CFR implementation to handle more decision points.

11. **Lesson 11: Exploitive vs. Optimal Strategies**
    - Understand the trade-offs between optimal and exploitive strategies.
    - Coding Exercise: Modify your CFR code to test against an exploitive strategy.

12. **Lesson 12: Evaluating Solvers**
    - Evaluate solvers’ performance on your toy game.
    - Coding Exercise: Write tests to measure the performance of different strategies.

---

### **Week 5: Building Advanced Agents**
13. **Lesson 13: Dealing with Imperfect Information**
    - Learn how to handle hidden cards and information in poker.
    - Coding Exercise: Update the toy game to include imperfect information scenarios.

14. **Lesson 14: Monte Carlo Tree Search (MCTS) Basics**
    - Explore MCTS as an alternative to CFR.
    - Coding Exercise: Implement a basic version of MCTS for decision-making in the toy game.

15. **Lesson 15: Combining CFR and MCTS**
    - Learn when and how to combine CFR and MCTS.
    - Coding Exercise: Integrate CFR and MCTS into your toy poker solver.

---

### **Week 6: Real-World Poker AI**
16. **Lesson 16: Modern Poker AI Agents**
    - Overview of top poker AI agents (e.g., DeepStack, Libratus).
    - Coding Exercise: Research and implement a simplified feature from one of these agents.

17. **Lesson 17: Scalability and Efficiency**
    - Learn how poker solvers are scaled for larger games.
    - Coding Exercise: Optimize your poker solver for speed and memory usage.

18. **Lesson 18: Wrap-Up and Capstone Project**
    - Consolidate what you’ve learned with a capstone project.
    - Coding Exercise: Build a fully functional toy poker solver and evaluate its performance.

---

### Optional Deep Dive Topics
- **Neural Networks in Poker AI**: Implement a basic neural network for strategy evaluation.
- **Exploration vs. Exploitation in AI**: Use reinforcement learning concepts to fine-tune strategies.
