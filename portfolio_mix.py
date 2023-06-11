
# #  Import dictionaries
# import pandas as pd




# Create a dictionary of options for a portfolio mix
# This dictionary has five keys corresponding to the five risk profiles 
# (Aggressive, Moderately Aggressive, Moderate, Moderately Conservative, and Conservative), 
# and each key contains a nested dictionary with the portfolio mix information. 
portfolio_mix = {
    'Aggressive': {'stocks': 0.7, 'cryptocurrency': 0.2, 'bonds': 0.1},
    'Moderately Aggressive': {'stocks': 0.5, 'cryptocurrency': 0.3, 'bonds': 0.2},
    'Moderate': {'stocks': 0.4, 'cryptocurrency': 0.3, 'bonds': 0.3},
    'Moderately Conservative': {'stocks': 0.3, 'cryptocurrency': 0.2, 'bonds': 0.5},
    'Conservative': {'stocks': 0.2, 'cryptocurrency': 0.1, 'bonds': 0.7}
}

# Example usage 
# This will print or return a list 
# containing the portfolio mix values for the 'Moderate' risk profile, 
# in the same order as the keys in the nested dictionary (stocks, cryptocurrency, and bonds). 
# You can then use this list to construct your investment portfolio.
risk_profile = 'Aggressive'
portfolio = portfolio_mix[risk_profile]
portfolio_weight = [v for k, v in portfolio.items()]
print(portfolio_weight)  # [0.4, 0.3, 0.3]