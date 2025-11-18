"""
Sample application to test the mitchallen-coin package.

This app demonstrates the three functions from mitchallen.coin:
1. flip() - Returns random boolean (True/False) with 50% probability
2. heads() - Returns random boolean (same as flip)
3. tails() - Returns opposite of heads()
"""

from mitchallen.coin import flip, heads, tails


def demo_flip() -> None:
    """Demonstrate the flip() function."""
    print(f"\n{'='*50}")
    print("1. TESTING flip()")
    print(f"{'='*50}")
    print("flip() returns a random boolean value\n")

    heads_count = 0
    tails_count = 0
    num_flips = 10

    print(f"Calling flip() {num_flips} times:\n")
    for i in range(1, num_flips + 1):
        result = flip()
        display = "Heads (True)" if result else "Tails (False)"
        print(f"  Flip {i:2d}: {display}")

        if result:
            heads_count += 1
        else:
            tails_count += 1

    print(f"\nResults: {heads_count} True, {tails_count} False")


def demo_heads() -> None:
    """Demonstrate the heads() function."""
    print(f"\n{'='*50}")
    print("2. TESTING heads()")
    print(f"{'='*50}")
    print("heads() returns a random boolean value (same as flip)\n")

    true_count = 0
    false_count = 0
    num_calls = 10

    print(f"Calling heads() {num_calls} times:\n")
    for i in range(1, num_calls + 1):
        result = heads()
        print(f"  Call {i:2d}: {result}")

        if result:
            true_count += 1
        else:
            false_count += 1

    print(f"\nResults: {true_count} True, {false_count} False")


def demo_tails() -> None:
    """Demonstrate the tails() function."""
    print(f"\n{'='*50}")
    print("3. TESTING tails()")
    print(f"{'='*50}")
    print("tails() returns the opposite of heads()\n")

    print(f"Calling heads() and tails() together:\n")
    for i in range(1, 11):
        heads_result = heads()
        tails_result = tails()
        match = "opposite ✓" if heads_result != tails_result else "same ✗"
        print(f"  Call {i:2d}: heads()={heads_result:5}, tails()={tails_result:5} ({match})")


def main():
    """Run all demonstrations."""
    print("\n" + "="*50)
    print("MITCHALLEN-COIN PACKAGE TEST")
    print("="*50)
    print("\nTesting all methods from mitchallen.coin")

    demo_flip()
    demo_heads()
    demo_tails()

    print(f"\n{'='*50}")
    print("ALL TESTS COMPLETED")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()
