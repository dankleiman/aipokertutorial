import matplotlib.pyplot as plt

def calculate_ev(pot_size, bet_size, p_bluff):
    """
    Calculate the Expected Value (EV) of calling in a poker scenario.

    :param pot_size: Total pot size before the bet.
    :param bet_size: Size of the bet to call.
    :param p_bluff: Probability that the opponent is bluffing (0 to 1).
    :return: EV of calling, EV of folding (always 0), and a recommendation.
    """
    win_size = pot_size + (2 * bet_size)
    loss = bet_size

    p_value = 1 - p_bluff

    ev = (win_size * p_bluff) - (loss * p_value)

    print(f"pot: {pot_size} // bet: {bet_size} // p_bluff: {p_bluff}")

    if ev > 0:
      recommendation = "Call"
    elif ev < 0:
      recommendation = "Fold"
    else:
      recommendation = "No decision"

    print(f"ev: {ev} // recommendation: {recommendation}")
    return ev, recommendation


def simulate_bluff_probability(pot_size, bet_size):
    probabilities = [i / 100 for i in range(101)]  # Bluff probabilities from 0 to 1
    ev_values = []

    for p_bluff in probabilities:
        ev, _ = calculate_ev(pot_size, bet_size, p_bluff)
        ev_values.append(ev)

    # Plot the results
    plt.plot(probabilities, ev_values, label=f"Pot: {pot_size}, Bet: {bet_size}")
    plt.xlabel("Probability of Bluffing")
    plt.ylabel("EV of Calling")
    plt.title("EV vs. Bluff Probability")
    plt.legend()
    plt.grid()
    plt.show()

# Example simulation
simulate_bluff_probability(100, 50)
