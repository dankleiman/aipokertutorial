from typing import List

# [[3, -1],  # Row 1: Player 1 gets 3 if P1 chooses A and P2 chooses X, -1 if P2 chooses Y.
#  [-2, 4]]  # Row 2: Player 1 gets -2 if P1 chooses B and P2 chooses X, 4 if P2 chooses Y.


def create_payoff_matrix(input: List[List]) -> List[List]:
    if not all(isinstance(lst, list) for lst in input):
        raise ValueError("Input must be a list of lists.")

    list_len = len(input[0])
    if not all(len(lst) == list_len for lst in input):
        raise ValueError("All lists in input must have the same length.")

    return input


# ### Testing the Function
# Write a few test cases:
# 1. A valid payoff matrix, e.g., `[[3, -1], [-2, 4]]`.
# 2. An invalid matrix where the rows have different lengths, e.g., `[[3, -1], [-2]]`.
# 3. A completely invalid input, e.g., `[3, -1]` (not a list of lists).

# Once you’ve written the test cases, run the function with them and share the results! Let me know if you need help refining the tests.


def test_create_payoff_matrix():
    # Test Case 1
    input = [[3, -1], [-2, 4]]
    assert create_payoff_matrix(input) == input

    # Test Case 2
    input = [[3, -1], [-2]]
    try:
        create_payoff_matrix(input)
    except ValueError as e:
        assert str(e) == "All lists in input must have the same length."

    # Test Case 3
    input = [3, -1]
    try:
        create_payoff_matrix(input)
    except ValueError as e:
        assert str(e) == "Input must be a list of lists."

    print("All tests passed successfully.")


# Task: Write a Function to Compute Payoffs
# Write a function compute_payoff(matrix, p1_strategy, p2_strategy):

# matrix is the payoff matrix.
# p1_strategy is Player 1’s chosen row (0-indexed).
# p2_strategy is Player 2’s chosen column (0-indexed).
# Returns the payoff for Player 1 (negative for Player 2).
# Validate inputs:

# Ensure strategies are within the matrix bounds.
# Raise an error for invalid indices.


def compute_payoff(matrix: List[List], p1_strategy: int, p2_strategy: int) -> int:
    if p1_strategy < 0 or p1_strategy >= len(matrix):
        raise ValueError("Player 1's strategy is out of bounds.")

    if p2_strategy < 0 or p2_strategy >= len(matrix[0]):
        raise ValueError("Player 2's strategy is out of bounds.")

    return matrix[p1_strategy][p2_strategy]


# Task: Write a Function to Compute Expected Payoff
# Function signature: compute_expected_payoff(matrix, p1_probs, p2_probs).
# matrix: The payoff matrix.
# p1_probs: A list of probabilities for Player 1’s strategies.
# p2_probs: A list of probabilities for Player 2’s strategies.
# Validate inputs:
# Probabilities must sum to 1.
# Lengths of p1_probs and p2_probs must match the matrix dimensions.
# Compute the expected payoff using the formula: \text{Expected Payoff} = \sum_{i,j} (\text{matrix}[i][j] \times \text{p1_probs}[i] \times \text{p2_probs}[j])


def compute_expected_payoff(
    matrix: List[List], p1_probs: List[float], p2_probs: List[float]
) -> float:
    if not all(isinstance(prob, (int, float)) for prob in p1_probs + p2_probs):
        raise ValueError("Probabilities must be integers or floats.")

    if not all(0 <= prob <= 1 for prob in p1_probs + p2_probs):
        raise ValueError("Probabilities must be between 0 and 1.")

    if abs(sum(p1_probs) - 1) > 1e-9 or abs(sum(p2_probs) - 1) > 1e-9:
        raise ValueError("Probabilities must sum to 1.")

    if len(p1_probs) != len(matrix) or len(p2_probs) != len(matrix[0]):
        raise ValueError(
            "Lengths of p1_probs and p2_probs must match the matrix dimensions."
        )

    expected_payoff = 0
    for p1_choice in range(len(matrix)):
        for p2_choice in range(len(matrix[0])):
            expected_payoff += (
                matrix[p1_choice][p2_choice] * p1_probs[p1_choice] * p2_probs[p2_choice]
            )

    return expected_payoff


def main():
    matrix = create_payoff_matrix([[3, -1], [-2, 4]])
    p1_strategy = 0
    p2_strategy = 1
    print(f"Payoff for Player 1: {compute_payoff(matrix, p1_strategy, p2_strategy)}")

    p1_probs = [0.7, 0.3]
    p2_probs = [0.5, 0.5]
    print(f"Expected payoff: {compute_expected_payoff(matrix, p1_probs, p2_probs)}")


if __name__ == "__main__":
    main()
