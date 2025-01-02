import networkx as nx
import matplotlib.pyplot as plt

# Expanded game tree with corrected probabilities and payoffs
game_tree_expanded = nx.DiGraph()

# Add initial nodes with labels and payoffs
game_tree_expanded.add_node("Start", label="Player 1 Starts")
game_tree_expanded.add_node("P1 Bet", label="Player 1 Bets")
game_tree_expanded.add_node("P1 Check", label="Player 1 Checks")
game_tree_expanded.add_node("P2 Call", label="Player 2 Calls (Pot=20)")
game_tree_expanded.add_node("P2 Fold", label="Player 2 Folds (Pot=15)")
game_tree_expanded.add_node("P2 Bet", label="Player 2 Bets")
game_tree_expanded.add_node("P2 Check", label="Player 2 Checks")
game_tree_expanded.add_node("P1 Call", label="Player 1 Calls (Pot=20)")
game_tree_expanded.add_node("P1 Fold", label="Player 1 Folds (Pot=15)")
game_tree_expanded.add_node("Showdown", label="Showdown")
game_tree_expanded.add_node("P1 Wins", label="Player 1 Wins (Pot=20)", payoff=20)
game_tree_expanded.add_node("P2 Wins", label="Player 2 Wins (Pot=20)", payoff=-20)
game_tree_expanded.add_node("P1 Wins (10)", label="Player 1 Wins (Pot=10)", payoff=10)
game_tree_expanded.add_node("P2 Wins (10)", label="Player 2 Wins (Pot=10)", payoff=-10)

# Add edges with corrected probabilities
game_tree_expanded.add_edges_from([
    ("Start", "P1 Bet", {"prob": 0.7}),  # Assume Player 1 Bets 70% of the time
    ("Start", "P1 Check", {"prob": 0.3}),  # Assume Player 1 Checks 30% of the time
    ("P1 Bet", "P2 Call", {"prob": 0.6}),  # Assume 60% chance Player 2 calls
    ("P1 Bet", "P2 Fold", {"prob": 0.4}),  # Assume 40% chance Player 2 folds
    ("P1 Check", "P2 Bet", {"prob": 0.5}),  # Assume 50% chance Player 2 bets
    ("P1 Check", "P2 Check", {"prob": 0.5}),  # Assume 50% chance Player 2 checks
    ("P2 Bet", "P1 Call", {"prob": 0.7}),  # Assume 70% chance Player 1 calls
    ("P2 Bet", "P1 Fold", {"prob": 0.3}),  # Assume 30% chance Player 1 folds
    ("P2 Call", "Showdown", {"prob": 1.0}),
    ("P2 Check", "P1 Wins (10)", {"prob": 0.5}),  # Assume even odds for $10 pot
    ("P2 Check", "P2 Wins (10)", {"prob": 0.5}),
    ("P1 Call", "Showdown", {"prob": 1.0}),
    ("Showdown", "P1 Wins", {"prob": 0.6}),  # Assume Player 1 wins 60% of $20 pots
    ("Showdown", "P2 Wins", {"prob": 0.4})   # Assume Player 2 wins 40% of $20 pots
])
