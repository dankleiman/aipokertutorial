from typing import Tuple, List


def solve_nash_equilibrium(
    matrix: List[List[float]],
) -> Tuple[Tuple[float, float], Tuple[float, float], float]:
    """
    Solves for the Nash equilibrium of a 2x2 zero-sum game.

    Args:
        matrix (List[List[float]]): 2x2 payoff matrix for Player 1.

    Returns:
        Tuple[Tuple[float, float], Tuple[float, float], float]:
            - Player 1's mixed strategy (p1, p2).
            - Player 2's mixed strategy (q1, q2).
            - Value of the game (expected payoff for Player 1).
    """
    # Matrix entries
    a, b = matrix[0]  # Row 1: Player 1's payoffs
    c, d = matrix[1]  # Row 2: Player 1's payoffs

    # Solve for Player 1's probabilities (p1, p2)
    # p1 * a + p2 * c = p1 * b + p2 * d
    # p1 * a + (1 - p1) * c = p1 * b + (1 - p1) * d
    # p1 * a + c - p1 * c = p1 * b + d - p1 * d
    # p1 * (a - c) + c = p1 * (b - d) + d
    # p1 * (a - c) - p1 * (b - d) = d - c
    # p1 * ((a - c) - (b - d)) = d - c
    p1 = (d - c) / ((a - c) - (b - d))
    p2 = 1 - p1

    # Solve for Player 2's probabilities (q1, q2)
    # q1 * a + q2 * b = q1 * c + q2 * d
    # q1 * a + (1 - q1) * b = q1 * c + (1 - q1) * d
    # q1 * a + b - q1 * b = q1 * c + d - q1 * d
    # q1 * (a - b) + b = q1 * (c - d) + d
    # q1 * (a - b) - q1 * (c - d) = d - b
    # q1 * ((a - b) - (c - d)) = d - b
    q1 = (d - b) / ((a - b) - (c - d))
    q2 = 1 - q1

    # Compute the value of the game
    value = p1 * (q1 * a + q2 * b) + p2 * (q1 * c + q2 * d)

    return (p1, p2), (q1, q2), value


# Example usage
matrix = [[3, -1], [-2, 4]]
player1_strategy, player2_strategy, game_value = solve_nash_equilibrium(matrix)

print("Player 1's strategy:", player1_strategy)
print("Player 2's strategy:", player2_strategy)
print("Value of the game:", game_value)
