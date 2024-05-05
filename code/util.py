import numpy as np

def split_dataframe(df, train_ratio):
    # Ensure the ratios < 1
    assert train_ratio < 1, "Ratios must less than 1"
    # Calculate the number of rows for the training set
    train_rows = int(df.shape[0] * train_ratio)

    # Split the dataframe
    train_df = df.iloc[:train_rows]
    test_df = df.iloc[train_rows:]

    return train_df, test_df

def binarize_y(y):
    # Binarize the y to -1 and 1
    bin_arr =  y.apply(lambda x : 1 if x>=0 else -1)
    return bin_arr


def ff2(df):
    # plot the reutrn result
    return

def ff3(df):
    # plot the signal compare
    return

def calculate_daily_risk_free_log_return(risk_free_annual_rate=0.02, trading_days=252):
    daily_rate = risk_free_annual_rate / trading_days
    daily_log_return = np.log(1 + daily_rate)
    return daily_log_return

def calculate_sharpe_ratio(returns, risk_free_rate=calculate_daily_risk_free_log_return()):
    """
    Calculate the Sharpe ratio of a portfolio.
    
    Parameters:
    - returns: A pandas Series representing the returns of the portfolio.
    - risk_free_rate: The risk-free rate of return.
    
    Returns: The Sharpe ratio.
    """
    excess_returns = returns - risk_free_rate
    sharpe_ratio = np.mean(excess_returns) / np.std(excess_returns, axis=0)
    return sharpe_ratio

def calculate_treynor_ratio(returns, risk_free_rate, beta=1):
    """
    Calculate the Treynor ratio of a portfolio.
    
    Parameters:
    - returns: A pandas Series representing the returns of the portfolio.
    - risk_free_rate: The risk-free rate of return.
    - beta: The beta of the portfolio.
    
    Returns: The Treynor ratio.
    """
    excess_returns = returns - risk_free_rate
    treynor_ratio = np.mean(excess_returns) / beta
    return treynor_ratio

def calculate_jensens_alpha(returns, market_returns, risk_free_rate, beta=1):
    """
    Calculate Jensen's Alpha of a portfolio.
    
    Parameters:
    - returns: A pandas Series representing the returns of the portfolio.
    - market_returns: A pandas Series representing the returns of the market.
    - risk_free_rate: The risk-free rate of return.
    - beta: The beta of the portfolio.
    
    Returns: Jensen's Alpha.
    """
    expected_returns = risk_free_rate + beta * (market_returns - risk_free_rate)
    jensens_alpha = np.mean(returns - expected_returns)
    return jensens_alpha