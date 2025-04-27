# Value-at-Risk (VaR) Calculation using Monte Carlo Simulation

## Overview

This project calculates Value-at-Risk (VaR) and Conditional Value-at-Risk (CVaR) for a portfolio of stocks using Monte Carlo simulation. It retrieves stock data from Yahoo Finance, calculates portfolio returns, and estimates VaR and CVaR.

## Functionality

The project performs the following steps:

1.  **Data Retrieval:** Downloads historical stock prices for a given list of stocks from Yahoo Finance using the `yfinance` library.
2.  **Return Calculation:** Calculates daily returns for each stock in the portfolio.
3.  **Covariance Matrix Calculation:** Computes the covariance matrix of the stock returns.
4.  **Monte Carlo Simulation:** Simulates portfolio values over time using a Monte Carlo approach, assuming a normal distribution of returns and using the Cholesky decomposition of the covariance matrix.
5.  **VaR and CVaR Calculation:** Calculates VaR and CVaR from the simulated portfolio values.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/git098/Value_at_Risk.git
    cd Value_at_Risk
    ```

2.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the `MonteCarlo_VaR.py` script:**

    ```bash
    python MonteCarlo_VaR.py
    ```

    The script will:

    *   Download stock data from Yahoo Finance.
    *   Perform a Monte Carlo simulation of portfolio values.
    *   Plot the simulated portfolio values.
    *   Calculate and print the VaR and CVaR for the portfolio.

## Requirements

*   Python 3.6+
*   `pandas`
*   `numpy`
*   `matplotlib`
*   `yfinance`

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.
