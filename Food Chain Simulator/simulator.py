
#!/usr/bin/env python3
"""
Food Chain Simulator — with trophic validation + random batch mode (CSV export)

Usage:
    python simulator.py
    python simulator.py --random 10   # generate 10 random chains → chains.csv
"""

import argparse
import csv
import random

# Trophic levels in order (strict logic)
TROPHIC_LEVELS = [
    "Producer",
    "Primary consumer",
    "Secondary consumer",
    "Tertiary consumer",
    "Apex predator"
]

# Organisms per level
ORGANISMS = {
    "Producer": ["Grass", "Algae", "Phytoplankton", "Oak tree"],
    "Primary consumer": ["Grasshopper", "Rabbit", "Zooplankton", "Deer"],
    "Secondary consumer": ["Frog", "Small fish", "Weasel", "Bird (insectivore)"],
    "Tertiary consumer": ["Snake", "Large fish", "Hawk", "Fox"],
    "Apex predator": ["Eagle", "Shark", "Lion", "Tiger"]
}

def choose_from(level, options):
    """Let user choose an organism or pick random."""
    print(f"\n{level}:")
    for i, o in enumerate(options, 1):
        print(f"  {i}. {o}")
    choice = input(f"Choose {level} (1-{len(options)}) or press Enter to pick random: ").strip()

    if not choice:
        return random.choice(options)

    try:
        selected = options[int(choice) - 1]
        return selected
    except Exception:
        print("Invalid choice — using random.")
        return random.choice(options)


def validate_chain(chain):
    """
    Ensure the chain follows correct trophic order.
    This is mostly guaranteed by structure, but we double-check.
    """
    if len(chain) != len(TROPHIC_LEVELS):
        return False

    # Validate each organism belongs to correct trophic level
    for org, level in chain.items():
        if org not in ORGANISMS[level]:
            return False

    return True


def build_chain_user():
    """Build a chain interactively."""
    chain = {}
    for level in TROPHIC_LEVELS:
        chain[level] = choose_from(level, ORGANISMS[level])
    return chain


def build_chain_random():
    """Generate a valid random chain."""
    chain = {}
    for level in TROPHIC_LEVELS:
        chain[level] = random.choice(ORGANISMS[level])
    return chain


def pretty_print(chain):
    print("\nFood chain:")
    print(" → ".join(chain[level] for level in TROPHIC_LEVELS))


def export_csv(chains, filename="chains.csv"):
    """Export a list of chains to CSV."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(TROPHIC_LEVELS)  # header row

        for chain in chains:
            row = [chain[level] for level in TROPHIC_LEVELS]
            writer.writerow(row)

    print(f"\n✔ Exported {len(chains)} chains to {filename}")


def main():
    parser = argparse.ArgumentParser(description="Food Chain Simulator")
    parser.add_argument("--random", type=int,
                        help="Generate N random food chains and export to CSV")

    args = parser.parse_args()

    # Random batch generation mode
    if args.random:
        n = args.random
        print(f"Generating {n} random valid chains...")
        chains = [build_chain_random() for _ in range(n)]
        export_csv(chains)
        return

    # Normal interactive mode
    print("Welcome to Food Chain Simulator!")
    chain = build_chain_user()
    pretty_print(chain)


if __name__ == "__main__":
    main()
