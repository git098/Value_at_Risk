import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf

# Importing data
def get_data(stocks, start, end):
    stock_data = yf.download(stocks, start=start, end=end)['Close']
    returns = stock_data.pct_change()
    mean_returns = returns.mean()
    cov_matrix = returns.cov()
    return mean_returns, cov_matrix

stocks1 = ['BEL.BO', 'AXISBANK.NS', 'DLF.NS', 'IDEA.NS', 'PNB.NS', 'RELIANCE.NS']
end_date = dt.datetime.now()
start_date = end_date - dt.timedelta(days=300)

mean_returns, cov_matrix = get_data(stocks1, start_date, end_date)

print(mean_returns)

weights = np.array([0.1, 0.2, 0.2, 0.1, 0.2, 0.2])

#Monte Carlo Simualation
#Number of simulations
mc_sims = 1000
T = 100

meanM = np.full(shape=(T, len(weights)), fill_value= mean_returns)
mean_M = meanM.T

portfolio_sims = np.full(shape=(T, mc_sims), fill_value=0.0)

initialPortfolio = 10000

for m in range(0, mc_sims):
    Z = np.random.normal(size=(T, len(weights)))
    L = np.linalg.cholesky(cov_matrix)
    dailyReturns =mean_M + np.inner(L, Z)
    portfolio_sims[:, m] = np.cumprod(np.inner(weights, dailyReturns.T)+1)* initialPortfolio

plt.plot(portfolio_sims)
plt.ylabel('Portfolio Value (Rs)')
plt.xlabel('Days')
plt.title('MC simulation of a portfolio')
plt.show()

def mcVaR(returns, alpha=5):
    """ input: pandas series of returns
        output: percentile on return distribution to a given confidence level alpha
     """
    
    if isinstance(returns, pd.Series):
        return np.percentile(returns, alpha)
    else:
        raise TypeError('Expected a pandas data series')
    
def mcCVaR(returns, alpha=5):
    """ input: pandas series of returns
        output: expected shortfall below VaR
     """
    
    if isinstance(returns, pd.Series):
        belowVaR = returns<= mcVaR(returns, alpha=alpha)
        return returns[belowVaR].mean()
    else:
        raise TypeError('Expected a pandas data series')
    
PortfolioResults = pd.Series(portfolio_sims[-1,:])

VaR = initialPortfolio - mcVaR(PortfolioResults, alpha=5)
CVaR = initialPortfolio - mcCVaR(PortfolioResults, alpha=5)
    
print('VaR = Rs {}'.format(round(VaR,2)))
print('CVaR = Rs {}'.format(round(CVaR,2)))