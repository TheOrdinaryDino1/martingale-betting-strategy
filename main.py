import random

def martingale_simulation(initial_cash, initial_bet, max_rounds, gambles_per_simulation):
    wins = 0
    losses = 0

    for sim in range(1, max_rounds + 1):
        cash = initial_cash
        bet = initial_bet

        print(f"\nSimulation {sim}:")

        for _ in range(gambles_per_simulation):
            if cash <= 0:
                print("Out of cash! Simulation terminated.")
                break

            outcome = random.choice([0, 1])

            if outcome == 1:
                cash += bet
                print(f"Win: Bet {bet}, Cash {cash}")
                bet = initial_bet
            else:
                cash -= bet
                print(f"Lose: Bet {bet}, Cash {cash}")
                bet *= 2

        if cash <= 0 or cash < initial_cash:
            losses += 1
        elif cash >= initial_cash:
            wins += 1

    return wins, losses

initial_cash = 1000
initial_bet = 1
max_rounds = 10000
gambles_per_simulation = 50

total_wins, total_losses = martingale_simulation(initial_cash, initial_bet, max_rounds, gambles_per_simulation)

with open("results.txt", "a") as results_file:
    results_file.write("\nFinal Summary:\n")
    results_file.write(f"Total wins: {total_wins}\n")
    results_file.write(f"Total losses: {total_losses}\n")
    if total_wins >= total_losses:
        results_file.write("Overall result: Profitable\n")
    else:
        results_file.write("Overall result: Unprofitable\n")

print("\nFinal Summary:")
print(f"Total wins: {total_wins}")
print(f"Total losses: {total_losses}")
if total_wins >= total_losses:
    print("Overall result: Profitable")
else:
    print("Overall result: Unprofitable")
