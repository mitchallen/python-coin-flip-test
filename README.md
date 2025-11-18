# python-coin-flip-test

A comprehensive sample application to test the [mitchallen-coin](https://pypi.org/project/mitchallen-coin/) Python package.

## Overview

This project demonstrates various uses of the `flip()` function from the `mitchallen.coin` package, including:

1. **Basic Coin Flip Simulation** - Classic heads/tails coin flipping
2. **Probability-Based Events** - Weather forecasts and random event generation
3. **Distribution Analysis** - Statistical analysis of random value distribution
4. **Monte Carlo Pi Estimation** - Estimate Pi using random sampling
5. **Dice Roll Simulation** - Simulate 6-sided dice rolls

## Requirements

- Python 3.12 or higher
- mitchallen-coin package (installed automatically)

## Installation

1. Clone this repository (or use your local copy)
2. Install dependencies using Make, uv, or pip:

```bash
# Using Make (recommended)
make install

# Or using uv directly
uv sync

# Or using pip
pip install -e .
```

## Usage

### Using Make (recommended)

```bash
# See all available commands
make help

# Install and run
make all

# Just run the application
make run

# Clean up cache files
make clean
```

### Direct Python execution

```bash
python main.py
```

This will execute all five demonstration functions and display comprehensive output showing various applications of the mitchallen-coin package.

## What is mitchallen-coin?

The `mitchallen-coin` package is a lightweight random number generator that provides a single `flip()` function. This function returns a random floating-point number in the range [0.0, 1.0), making it ideal for:

- Simulations
- Games
- Probability-based applications
- Monte Carlo methods
- Any scenario requiring uniform random numbers

## Example Output

The application will display:
- Coin flip results and statistics
- Probability-based weather forecasts
- Distribution histograms
- Pi estimation accuracy
- Dice roll distributions

## License

MIT
