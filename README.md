# Warrant Implied Volatility Analysis

A Python tool for analyzing and visualizing warrant implied volatility data. This tool creates four different visualizations:

1. Implied Volatility Over Time with percentile bands
2. IV Distribution histogram
3. Intraday IV Patterns
4. IV vs Warrant Price scatter plot

## Requirements

- Python 3.x
- pandas
- matplotlib
- numpy

## Installation

```bash
pip install -r requirements.txt
```

## Usage

1. Place your data in a CSV file with the following columns:
   - Timestamp
   - option price
   - Equity Price
   - Implied Vol

2. Run the analysis:
```bash
python volatility_analysis.py
```

The script will generate a `warrant_iv_analysis.png` file containing all visualizations.

## Sample Output

The generated visualization includes:
- Time series analysis with 5th, 25th, 50th, 75th, and 95th percentile bands
- Distribution of implied volatility values
- Intraday patterns showing mean and standard deviation bands
- Price vs IV relationship scatter plot
