# Consolidation Project #2: Tuple Out Dice Game
import random

def dice_roll():
    return [random.randint(1, 6) for _ in range(3)]

def tupled_out(dice_values):
    return len(set(dice_values)) == 1

def main():
    num_players = 2
    target_score = 100

    player_scores = [0] * num_players
    active_player = 0

    while max(player_scores) < target_score:
        print(f"Player {active_player + 1}'s turn:")
        input("Press Enter to roll the dice...")

        dice_values = dice_roll()
        print(f"Dice values: {dice_values}")

        if tupled_out(dice_values):
            print("Tupled out! Zero points for this turn.")
        else:
            turn_score = sum(dice_values)
            player_scores[active_player] += turn_score
            print(f"Turn score: {turn_score}, Total score: {player_scores[active_player]}")

        active_player = (active_player + 1) % num_players

    winner = player_scores.index(max(player_scores)) + 1
    print(f"Player {winner} wins with a score of {player_scores[winner - 1]}!")

if __name__ == "__main__":
    main()