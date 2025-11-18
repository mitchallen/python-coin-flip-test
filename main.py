"""
Sample application to test the mitchallen-coin package.

This app demonstrates various uses of the flip() function from mitchallen.coin:
1. Basic coin flip simulation
2. Probability-based events
3. Distribution analysis
4. Monte Carlo Pi estimation
5. Dice roll simulation
"""

from mitchallen.coin import flip


def demo_coin_flip(num_flips: int = 10) -> None:
    """Demonstrate basic coin flip simulation."""
    print(f"\n{'='*50}")
    print("1. BASIC COIN FLIP SIMULATION")
    print(f"{'='*50}")
    print(f"Flipping a coin {num_flips} times:\n")

    heads_count = 0
    tails_count = 0

    for i in range(1, num_flips + 1):
        result = "Heads" if flip() < 0.5 else "Tails"
        print(f"Flip {i:2d}: {result}")

        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1

    print(f"\nResults: Heads: {heads_count}, Tails: {tails_count}")
    print(f"Heads percentage: {heads_count/num_flips*100:.1f}%")


def demo_probability_events() -> None:
    """Demonstrate probability-based events."""
    print(f"\n{'='*50}")
    print("2. PROBABILITY-BASED EVENTS")
    print(f"{'='*50}")

    # Weather forecast (30% chance of rain)
    print("\nWeather Forecast (30% chance of rain):")
    for day in range(1, 8):
        if flip() < 0.3:
            print(f"  Day {day}: Rain expected - Bring an umbrella!")
        else:
            print(f"  Day {day}: Clear skies")

    # Random event generator
    print("\nRandom Event Generator:")
    value = flip()
    if value < 0.01:
        print(f"  Legendary event! (value: {value:.4f})")
    elif value < 0.10:
        print(f"  Rare event! (value: {value:.4f})")
    elif value < 0.30:
        print(f"  Uncommon event (value: {value:.4f})")
    else:
        print(f"  Common event (value: {value:.4f})")


def demo_distribution_analysis(num_samples: int = 1000) -> None:
    """Analyze the distribution of flip() results."""
    print(f"\n{'='*50}")
    print("3. DISTRIBUTION ANALYSIS")
    print(f"{'='*50}")
    print(f"Analyzing {num_samples} random values:\n")

    # Collect samples
    samples = [flip() for _ in range(num_samples)]

    # Calculate statistics
    avg = sum(samples) / len(samples)
    min_val = min(samples)
    max_val = max(samples)

    # Create histogram buckets
    buckets = [0] * 10
    for value in samples:
        bucket_index = min(int(value * 10), 9)
        buckets[bucket_index] += 1

    print(f"Average: {avg:.4f}")
    print(f"Min: {min_val:.4f}")
    print(f"Max: {max_val:.4f}")
    print("\nDistribution (10 buckets):")

    max_count = max(buckets)
    for i, count in enumerate(buckets):
        bar_length = int((count / max_count) * 40)
        bar = '█' * bar_length
        percentage = (count / num_samples) * 100
        print(f"  [{i/10:.1f}-{(i+1)/10:.1f}): {bar} {count} ({percentage:.1f}%)")


def demo_monte_carlo_pi(num_iterations: int = 100000) -> None:
    """Estimate Pi using Monte Carlo method."""
    print(f"\n{'='*50}")
    print("4. MONTE CARLO PI ESTIMATION")
    print(f"{'='*50}")
    print(f"Estimating Pi using {num_iterations} random points:\n")

    inside_circle = 0

    for _ in range(num_iterations):
        x, y = flip(), flip()
        # Check if point is inside quarter circle
        if x*x + y*y <= 1:
            inside_circle += 1

    pi_estimate = 4 * inside_circle / num_iterations
    error = abs(3.14159265359 - pi_estimate)
    error_percentage = (error / 3.14159265359) * 100

    print(f"Points inside circle: {inside_circle}/{num_iterations}")
    print(f"Estimated Pi: {pi_estimate:.8f}")
    print(f"Actual Pi:    3.14159265...")
    print(f"Error: {error:.8f} ({error_percentage:.2f}%)")


def demo_dice_rolls(num_rolls: int = 20) -> None:
    """Simulate dice rolls using flip()."""
    print(f"\n{'='*50}")
    print("5. DICE ROLL SIMULATION")
    print(f"{'='*50}")
    print(f"Rolling a 6-sided die {num_rolls} times:\n")

    rolls = []
    for i in range(1, num_rolls + 1):
        # Convert [0, 1) to [1, 6]
        roll = int(flip() * 6) + 1
        rolls.append(roll)
        print(f"Roll {i:2d}: {roll}")

    print(f"\nStatistics:")
    print(f"  Average: {sum(rolls)/len(rolls):.2f}")
    print(f"  Min: {min(rolls)}")
    print(f"  Max: {max(rolls)}")

    # Distribution
    print(f"\nDistribution:")
    for face in range(1, 7):
        count = rolls.count(face)
        percentage = (count / num_rolls) * 100
        bar = '█' * count
        print(f"  {face}: {bar} {count} ({percentage:.1f}%)")


def main():
    """Run all demonstrations."""
    print("\n" + "="*50)
    print("MITCHALLEN-COIN PACKAGE TEST")
    print("="*50)
    print("\nTesting mitchallen.coin.flip() function")
    print("Returns random float in range [0.0, 1.0)")

    # Run demonstrations
    demo_coin_flip(10)
    demo_probability_events()
    demo_distribution_analysis(1000)
    demo_monte_carlo_pi(100000)
    demo_dice_rolls(20)

    print(f"\n{'='*50}")
    print("ALL TESTS COMPLETED")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()
