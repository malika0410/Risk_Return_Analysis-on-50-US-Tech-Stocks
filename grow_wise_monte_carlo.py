#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import yfinance as yf
from yahoo_fin.stock_info import get_data
from MCForecastTools import MCSimulation
import warnings
warnings.filterwarnings('ignore')

# requires python 3.9 min


# In[3]:


# define investment amount
investment_amount = 100000


# In[4]:


#List of 50 stocks/tickers
tickers = ["AAPL", "GOOGL", "AMZN", "META","TSM","MSFT", "TSLA", "NVDA", "PYPL", "INTC", "AMD", "IBM", "CSCO", "ORCL", "CRM", "ADBE", "ZM", "SQ", "DOCU", "NFLX", "SNAP", "SPOT", "DBX", "UBER", "LYFT", "WDAY", "NOW", "TEAM", "SHOP", "TWLO", "ZS", "OKTA", "MDB", "CRWD", "NET", "FSLY", "DDOG", "SNOW", "PLTR", "U", "RBLX", "AFRM", "PATH", "COUR", "COIN", "BIDU", "JD", "BABA", "TCEHY", "ZI"]

# fetch historical data for each ticker grouping
ticker_data = yf.download(tickers, start="2013-01-01", end="2023-05-08")
prices_df = ticker_data

# display the resulting DataFrame
prices_df


# In[5]:


# calculate daily returns for ticker data in prices DataFrame 
daily_returns = prices_df["Close"].pct_change()

# format daily returns DataFrame to make usable with MCForecastTools
daily_returns.columns = pd.MultiIndex.from_product([daily_returns.columns, ["daily_return"]])
daily_returns=daily_returns.swaplevel(axis=1).dropna()

# display resulting DataFrame
daily_returns


# In[6]:


# concatenate ticker DataFrame with Daily Returns DataFrame
prices_df = pd.concat([prices_df, daily_returns], axis=1, join="inner")

# display resulting DataFrame
prices_df


# In[7]:

def sharpe_return(high_sharpe_tickers,med_sharpe_tickers,low_sharpe_tickers):
    # list portfolio groupings by sharpe ratio ranking based on Risk_Return_Analysis 
    #high_sharpe_tickers = ['NVDA', 'MSFT', 'SHOP', 'TSLA', 'AAPL', 'NFLX', 'AMD', 'MDB', 'ADBE', 'NOW', 'AMZN', 'GOOGL', 'TSM', 'TEAM', 'META'] 
    #med_sharpe_tickers = ['NET', 'TCEHY', 'SQ', 'DDOG', 'OKTA', 'ZS', 'CRWD', 'CRM', 'ORCL', 'CSCO', 'WDAY', 'TWLO', 'PYPL', 'DOCU', 'JD', 'INTC'] 
    #low_sharpe_tickers = ['ZM', 'BIDU', 'UBER', 'FSLY', 'PLTR', 'SPOT', 'BABA', 'SNAP', 'IBM', 'DBX', 'RBLX', 'SNOW', 'ZI', 'U', 'AFRM', 'LYFT', 'COIN', 'COUR', 'PATH']

    # create DataFrame for each list
    high_sharpe_df = prices_df.loc[:, prices_df.columns.get_level_values(1).isin(high_sharpe_tickers)]
    med_sharpe_df = prices_df.loc[:, prices_df.columns.get_level_values(1).isin(med_sharpe_tickers)]
    low_sharpe_df = prices_df.loc[:, prices_df.columns.get_level_values(1).isin(low_sharpe_tickers)]


    # display results of DataFrame
    #display(high_sharpe_df, med_sharpe_df, low_sharpe_df)


    # In[7]:


    # determine even weighting for Monte Carlo simulations 
    high_sharpe_weight = []
    weight_n = len(high_sharpe_tickers)

    for n in range(weight_n):
        high_sharpe_weight.append(1/weight_n)

    # print(n)        
    high_sharpe_weight


    # In[8]:


    # determine even weighting for Monte Carlo simulations 
    med_sharpe_weight = []
    weight_n = len(med_sharpe_tickers)

    for n in range(weight_n):
        med_sharpe_weight.append(1/weight_n)

    # print(n)        
    med_sharpe_weight


    # In[9]:


    # determine even weighting for Monte Carlo simulations 
    low_sharpe_weight = []
    weight_n = len(low_sharpe_tickers)

    for n in range(weight_n):
        low_sharpe_weight.append(1/weight_n)

    # print(n)        
    low_sharpe_weight


    # In[10]:


    # Configure a Monte Carlo simulation to forecast 10 years cumulative returns for high sharpe ratio portfolio
    #The weights should be split evenly across the portfolio
    # Run 500 samples.
    MC_10_yrs_high_sharpe = MCSimulation(
        portfolio_data=high_sharpe_df,
        weights=high_sharpe_weight,
        num_simulation=500,
        num_trading_days=252*10
    )

    # Review the simulation input data
    #display(MC_10_yrs_high_sharpe.portfolio_data.head())
    #display(MC_10_yrs_high_sharpe.portfolio_data.tail())



    # In[11]:


    # Run the Monte Carlo simulation to forecast 10 years cumulative returns
    MC_10_yrs_high_sharpe.calc_cumulative_return()


    # In[12]:


    # Visualize the 10-year Monte Carlo simulation by creating an
    # overlay line plot
    MC_10_yrs_high_sharpe_line_plot = MC_10_yrs_high_sharpe.plot_simulation()


    # In[13]:


    # Visualize the probability distribution of the 10-year Monte Carlo simulation 
    # by plotting a histogram
    MC_10_yrs_high_sharpe_distribution_plot = MC_10_yrs_high_sharpe.plot_distribution()


    # In[14]:


    # Generate summary statistics from the 10-year Monte Carlo simulation results
    MC_10_yrs_high_sharpe_sum_statistics = MC_10_yrs_high_sharpe.summarize_cumulative_return()

    # Review the 10-year Monte Carlo summary statistics
    #display(MC_10_yrs_high_sharpe_sum_statistics)


    # In[15]:


    # Use the lower and upper `95%` confidence intervals to calculate the range of the possible outcomes for the high sharpe portfolio
    ci_lower_ten_cumulative_return_hs = MC_10_yrs_high_sharpe_sum_statistics[8]*investment_amount
    ci_upper_ten_cumulative_return_hs = MC_10_yrs_high_sharpe_sum_statistics[9]*investment_amount

    # Print the result of your calculations
    print(f"There is a 95% chance that an investment of ${investment_amount} in the High Sharpe GrowWise portfolio over the next 10 years will end within the range of ${ci_lower_ten_cumulative_return_hs:.2f} and ${ci_upper_ten_cumulative_return_hs:.02f}")


    # In[16]:


    # Configure a Monte Carlo simulation to forecast 10 years cumulative returns for med sharpe ratio portfolio
    #The weights should be split evenly across the portfolio
    # Run 500 samples.
    MC_10_yrs_med_sharpe = MCSimulation(
        portfolio_data=med_sharpe_df,
        weights=med_sharpe_weight,
        num_simulation=500,
        num_trading_days=252*10
    )


    # In[17]:


    # Run the Monte Carlo simulation to forecast 10 years cumulative returns
    MC_10_yrs_med_sharpe.calc_cumulative_return()


    # In[18]:


    # Visualize the 10-year Monte Carlo simulation by creating an
    # overlay line plot
    MC_10_yrs_med_sharpe_line_plot = MC_10_yrs_med_sharpe.plot_simulation()


    # In[19]:


    # Visualize the probability distribution of the 10-year Monte Carlo simulation 
    # by plotting a histogram
    MC_10_yrs_med_sharpe_distribution_plot = MC_10_yrs_med_sharpe.plot_distribution()


    # In[20]:


    # Generate summary statistics from the 10-year Monte Carlo simulation results
    MC_10_yrs_med_sharpe_sum_statistics = MC_10_yrs_med_sharpe.summarize_cumulative_return()

    # Review the 10-year Monte Carlo summary statistics
    #display(MC_10_yrs_med_sharpe_sum_statistics)


    # In[21]:


    # Use the lower and upper `95%` confidence intervals to calculate the range of the possible outcomes for the med sharpe portfolio
    ci_lower_ten_cumulative_return_ms = MC_10_yrs_med_sharpe_sum_statistics[8]*investment_amount
    ci_upper_ten_cumulative_return_ms = MC_10_yrs_med_sharpe_sum_statistics[9]*investment_amount

    # Print the result of your calculations
    print(f"There is a 95% chance that an investment of ${investment_amount} in the Med Sharpe GrowWise portfolio over the next 10 years will end within the range of ${ci_lower_ten_cumulative_return_ms:.2f} and ${ci_upper_ten_cumulative_return_ms:.02f}")


    # In[22]:


    # Configure a Monte Carlo simulation to forecast 10 years cumulative returns for med sharpe ratio portfolio
    #The weights should be split evenly across the portfolio
    # Run 500 samples.
    MC_10_yrs_low_sharpe = MCSimulation(
        portfolio_data=low_sharpe_df,
        weights=low_sharpe_weight,
        num_simulation=500,
        num_trading_days=252*10
    )


    # In[23]:


    # Run the Monte Carlo simulation to forecast 10 years cumulative returns
    MC_10_yrs_low_sharpe.calc_cumulative_return()


    # In[24]:


    # Visualize the 10-year Monte Carlo simulation by creating an
    # overlay line plot
    MC_10_yrs_low_sharpe_line_plot = MC_10_yrs_low_sharpe.plot_simulation()


    # In[25]:


    # Visualize the probability distribution of the 10-year Monte Carlo simulation 
    # by plotting a histogram
    MC_10_yrs_low_sharpe_distribution_plot = MC_10_yrs_low_sharpe.plot_distribution()


    # In[26]:


    # Generate summary statistics from the 10-year Monte Carlo simulation results
    MC_10_yrs_low_sharpe_sum_statistics = MC_10_yrs_low_sharpe.summarize_cumulative_return()

    # Review the 10-year Monte Carlo summary statistics
    #display(MC_10_yrs_low_sharpe_sum_statistics)


    # In[27]:


    # Use the lower and upper `95%` confidence intervals to calculate the range of the possible outcomes for the low sharpe portfolio
    ci_lower_ten_cumulative_return_ls = MC_10_yrs_low_sharpe_sum_statistics[8]*investment_amount
    ci_upper_ten_cumulative_return_ls = MC_10_yrs_low_sharpe_sum_statistics[9]*investment_amount

    # Print the result of your calculations
    print(f"There is a 95% chance that an investment of ${investment_amount} in the Low Sharpe GrowWise portfolio over the next 10 years will end within the range of ${ci_lower_ten_cumulative_return_ls:.2f} and ${ci_upper_ten_cumulative_return_ls:.02f}")


# In[28]:

def beta_return(high_beta_tickers,med_beta_tickers,low_beta_tickers):
    # list portfolio groupings by beta ratio ranking based on Risk_Return_Analysis 
    #high_beta_tickers = ['AFRM', 'COIN','U','FSLY', 'NET', 'RBLX', 'PATH', 'LYFT', 'DDOG', 'UBER', 'SQ', 'SNOW', 'MDB', 'CRWD', 'PLTR'] 
    #med_beta_tickers = ['DOCU', 'ZI', 'SHOP', 'SNAP', 'ZS', 'COUR', 'TWLO', 'SPOT', 'OKTA', 'NVDA', 'AMD', 'PYPL', 'DBX', 'TSLA','TEAM','NOW'] 
    #low_beta_tickers = ['ADBE', 'WDAY','CRM', 'META', 'JD', 'MSFT', 'INTC', 'NFLX', 'AAPL', 'AMZN', 'GOOGL', 'BIDU', 'BABA', 'ZM', 'TSM', 'CSCO', 'ORCL', 'TCEHY', 'IBM']


    # create DataFrame for each list
    high_beta_df = prices_df.loc[:, prices_df.columns.get_level_values(1).isin(high_beta_tickers)]
    med_beta_df = prices_df.loc[:, prices_df.columns.get_level_values(1).isin(med_beta_tickers)]
    low_beta_df = prices_df.loc[:, prices_df.columns.get_level_values(1).isin(low_beta_tickers)]


    # display results of DataFrame
    #display(high_sharpe_df, med_sharpe_df, low_sharpe_df)


    # In[49]:


    # determine even weighting for Monte Carlo simulations 
    high_beta_weight = []
    weight_n = len(high_beta_tickers)
    for n in range(weight_n):
        high_beta_weight.append(1/weight_n)

    med_beta_weight = []
    weight_n = len(med_beta_tickers)
    for n in range(weight_n):
        med_beta_weight.append(1/weight_n)
            
    low_beta_weight = []
    weight_n = len(low_beta_tickers)
    for n in range(weight_n):
        low_beta_weight.append(1/weight_n)
            
            
    # print(n)        
    #high_beta_weight
    #med_beta_weight
    #low_beta_weight


    # In[30]:


    # Configure a Monte Carlo simulation to forecast 10 years cumulative returns for high beta portfolio
    #The weights should be split evenly across the portfolio
    # Run 500 samples.
    MC_10_yrs_high_beta = MCSimulation(
        portfolio_data=high_beta_df,
        weights=high_beta_weight,
        num_simulation=500,
        num_trading_days=252*10
    )


    # In[31]:


    # Run the Monte Carlo simulation to forecast 10 years cumulative returns
    MC_10_yrs_high_beta.calc_cumulative_return()


    # In[32]:


    # Visualize the 10-year Monte Carlo simulation by creating an
    # overlay line plot
    MC_10_yrs_high_beta_line_plot = MC_10_yrs_high_beta.plot_simulation()


    # In[33]:


    # Visualize the probability distribution of the 10-year Monte Carlo simulation 
    # by plotting a histogram
    MC_10_yrs_high_beta_distribution_plot = MC_10_yrs_high_beta.plot_distribution()


    # In[34]:


    # Generate summary statistics from the 10-year Monte Carlo simulation results
    MC_10_yrs_high_beta_sum_statistics = MC_10_yrs_high_beta.summarize_cumulative_return()

    # Review the 10-year Monte Carlo summary statistics
    #display(MC_10_yrs_high_beta_sum_statistics)


    # In[35]:


    # Use the lower and upper `95%` confidence intervals to calculate the range of the possible outcomes for the high beta portfolio
    ci_lower_ten_cumulative_return_hb = MC_10_yrs_high_beta_sum_statistics[8]*investment_amount
    ci_upper_ten_cumulative_return_hb = MC_10_yrs_high_beta_sum_statistics[9]*investment_amount

    # Print the result of your calculations
    print(f"There is a 95% chance that an investment of ${investment_amount} in the High Beta GrowWise portfolio over the next 10 years will end within the range of ${ci_lower_ten_cumulative_return_hb:.2f} and ${ci_upper_ten_cumulative_return_hb:.02f}")


    # In[36]:


    # Configure a Monte Carlo simulation to forecast 10 years cumulative returns for med beta portfolio
    #The weights should be split evenly across the portfolio
    # Run 500 samples.
    MC_10_yrs_med_beta = MCSimulation(
        portfolio_data=med_beta_df,
        weights=med_beta_weight,
        num_simulation=500,
        num_trading_days=252*10
    )


    # In[37]:


    # Run the Monte Carlo simulation to forecast 10 years cumulative returns
    MC_10_yrs_med_beta.calc_cumulative_return()


    # In[38]:


    # Visualize the 10-year Monte Carlo simulation by creating an
    # overlay line plot
    MC_10_yrs_med_beta_line_plot = MC_10_yrs_med_beta.plot_simulation()


    # In[39]:


    # Visualize the probability distribution of the 10-year Monte Carlo simulation 
    # by plotting a histogram
    MC_10_yrs_med_beta_distribution_plot = MC_10_yrs_med_beta.plot_distribution()


    # In[40]:


    # Generate summary statistics from the 10-year Monte Carlo simulation results
    MC_10_yrs_med_beta_sum_statistics = MC_10_yrs_med_beta.summarize_cumulative_return()

    # Review the 10-year Monte Carlo summary statistics
    #display(MC_10_yrs_med_beta_sum_statistics)


    # In[41]:


    # Use the lower and upper `95%` confidence intervals to calculate the range of the possible outcomes for the med beta portfolio
    ci_lower_ten_cumulative_return_mb = MC_10_yrs_med_beta_sum_statistics[8]*investment_amount
    ci_upper_ten_cumulative_return_mb = MC_10_yrs_med_beta_sum_statistics[9]*investment_amount

    # Print the result of your calculations
    print(f"There is a 95% chance that an investment of ${investment_amount} in the Med Beta GrowWise portfolio over the next 10 years will end within the range of ${ci_lower_ten_cumulative_return_mb:.2f} and ${ci_upper_ten_cumulative_return_mb:.02f}")


    # In[42]:


    # Configure a Monte Carlo simulation to forecast 10 years cumulative returns for low beta portfolio
    #The weights should be split evenly across the portfolio
    # Run 500 samples.
    MC_10_yrs_low_beta = MCSimulation(
        portfolio_data=low_beta_df,
        weights=low_beta_weight,
        num_simulation=500,
        num_trading_days=252*10
    )


    # In[43]:


    # Run the Monte Carlo simulation to forecast 10 years cumulative returns
    MC_10_yrs_low_beta.calc_cumulative_return()


    # In[44]:


    # Visualize the 10-year Monte Carlo simulation by creating an
    # overlay line plot
    MC_10_yrs_low_beta_line_plot = MC_10_yrs_low_beta.plot_simulation()


    # In[45]:


    # Visualize the probability distribution of the 10-year Monte Carlo simulation 
    # by plotting a histogram
    MC_10_yrs_low_beta_distribution_plot = MC_10_yrs_low_beta.plot_distribution()


    # In[46]:


    # Generate summary statistics from the 10-year Monte Carlo simulation results
    MC_10_yrs_low_beta_sum_statistics = MC_10_yrs_low_beta.summarize_cumulative_return()

    # Review the 10-year Monte Carlo summary statistics
    #display(MC_10_yrs_low_beta_sum_statistics)


    # In[47]:


    # Use the lower and upper `95%` confidence intervals to calculate the range of the possible outcomes for the low beta portfolio
    ci_lower_ten_cumulative_return_lb = MC_10_yrs_low_beta_sum_statistics[8]*investment_amount
    ci_upper_ten_cumulative_return_lb = MC_10_yrs_low_beta_sum_statistics[9]*investment_amount

    # Print the result of your calculations
    print(f"There is a 95% chance that an investment of ${investment_amount} in the Low Beta GrowWise portfolio over the next 10 years will end within the range of ${ci_lower_ten_cumulative_return_lb:.2f} and ${ci_upper_ten_cumulative_return_lb:.02f}")


    # In[50]:

def correlation_return(high_correlation_tickers,med_correlation_tickers,low_correlation_tickers):
    # list portfolio groupings by beta ratio ranking based on Risk_Return_Analysis 
    #high_correlation_tickers = ['AFRM', 'COIN','U','FSLY', 'NET', 'RBLX', 'PATH', 'LYFT', 'DDOG', 'UBER', 'SQ', 'SNOW', 'MDB', 'CRWD', 'PLTR'] 
    #med_correlation_tickers = ['DOCU', 'ZI', 'SHOP', 'SNAP', 'ZS', 'COUR', 'TWLO', 'SPOT', 'OKTA', 'NVDA', 'AMD', 'PYPL', 'DBX', 'TSLA','TEAM','NOW'] 
    #low_correlation_tickers = ['ADBE', 'WDAY','CRM', 'META', 'JD', 'MSFT', 'INTC', 'NFLX', 'AAPL', 'AMZN', 'GOOGL', 'BIDU', 'BABA', 'ZM', 'TSM', 'CSCO', 'ORCL', 'TCEHY', 'IBM']


    # create DataFrame for each list
    high_correlation_df = prices_df.loc[:, prices_df.columns.get_level_values(1).isin(high_correlation_tickers)]
    med_correlation_df = prices_df.loc[:, prices_df.columns.get_level_values(1).isin(med_correlation_tickers)]
    low_correlation_df = prices_df.loc[:, prices_df.columns.get_level_values(1).isin(low_correlation_tickers)]


    # display results of DataFrame
    #display(high_correlation_df, med_correlation_df, low_correlation_df)


    # In[51]:


    # determine even weighting for Monte Carlo simulations 
    high_correlation_weight = []
    weight_n = len(high_correlation_tickers)
    for n in range(weight_n):
        high_correlation_weight.append(1/weight_n)

    med_correlation_weight = []
    weight_n = len(med_correlation_tickers)
    for n in range(weight_n):
        med_correlation_weight.append(1/weight_n)
            
    low_correlation_weight = []
    weight_n = len(low_correlation_tickers)
    for n in range(weight_n):
        low_correlation_weight.append(1/weight_n)
            
            
    # print(n)        
    #high_correlation_weight
    #med_correlation_weight
    #low_correlation_weight


    # In[52]:


    # Configure a Monte Carlo simulation to forecast 10 years cumulative returns for high correlation portfolio
    #The weights should be split evenly across the portfolio
    # Run 500 samples.
    MC_10_yrs_high_correlation = MCSimulation(
        portfolio_data=high_correlation_df,
        weights=high_correlation_weight,
        num_simulation=500,
        num_trading_days=252*10
    )


    # In[53]:


    # Run the Monte Carlo simulation to forecast 10 years cumulative returns
    MC_10_yrs_high_correlation.calc_cumulative_return()


    # In[54]:


    # Visualize the 10-year Monte Carlo simulation by creating an
    # overlay line plot
    MC_10_yrs_high_correlation_line_plot = MC_10_yrs_high_correlation.plot_simulation()


    # In[55]:


    # Visualize the probability distribution of the 10-year Monte Carlo simulation 
    # by plotting a histogram
    MC_10_yrs_high_correlation_distribution_plot = MC_10_yrs_high_correlation.plot_distribution()


    # In[56]:


    # Generate summary statistics from the 10-year Monte Carlo simulation results
    MC_10_yrs_high_correlation_sum_statistics = MC_10_yrs_high_correlation.summarize_cumulative_return()

    # Review the 10-year Monte Carlo summary statistics
    #display(MC_10_yrs_high_correlation_sum_statistics)


    # In[57]:


    # Use the lower and upper `95%` confidence intervals to calculate the range of the possible outcomes for the high correlation portfolio
    ci_lower_ten_cumulative_return_hc = MC_10_yrs_high_correlation_sum_statistics[8]*investment_amount
    ci_upper_ten_cumulative_return_hc = MC_10_yrs_high_correlation_sum_statistics[9]*investment_amount

    # Print the result of your calculations
    print(f"There is a 95% chance that an investment of ${investment_amount} in the High Correlation GrowWise portfolio over the next 10 years will end within the range of ${ci_lower_ten_cumulative_return_hc:.2f} and ${ci_upper_ten_cumulative_return_hc:.02f}")


    # In[58]:


    # Configure a Monte Carlo simulation to forecast 10 years cumulative returns for high beta portfolio
    #The weights should be split evenly across the portfolio
    # Run 500 samples.
    MC_10_yrs_med_correlation = MCSimulation(
        portfolio_data=med_correlation_df,
        weights=med_correlation_weight,
        num_simulation=500,
        num_trading_days=252*10
    )


    # In[59]:


    # Run the Monte Carlo simulation to forecast 10 years cumulative returns
    MC_10_yrs_med_correlation.calc_cumulative_return()


    # In[60]:


    # Visualize the 10-year Monte Carlo simulation by creating an
    # overlay line plot
    MC_10_yrs_med_correlation_line_plot = MC_10_yrs_med_correlation.plot_simulation()


    # In[61]:


    # Visualize the probability distribution of the 10-year Monte Carlo simulation 
    # by plotting a histogram
    MC_10_yrs_med_correlation_distribution_plot = MC_10_yrs_med_correlation.plot_distribution()


    # In[62]:


    # Generate summary statistics from the 10-year Monte Carlo simulation results
    MC_10_yrs_med_correlation_sum_statistics = MC_10_yrs_med_correlation.summarize_cumulative_return()

    # Review the 10-year Monte Carlo summary statistics
    #display(MC_10_yrs_med_correlation_sum_statistics)


    # In[63]:


    # Use the lower and upper `95%` confidence intervals to calculate the range of the possible outcomes for the med correlation portfolio
    ci_lower_ten_cumulative_return_mc = MC_10_yrs_med_correlation_sum_statistics[8]*investment_amount
    ci_upper_ten_cumulative_return_mc = MC_10_yrs_med_correlation_sum_statistics[9]*investment_amount

    # Print the result of your calculations
    print(f"There is a 95% chance that an investment of ${investment_amount} in the Med Correlation GrowWise portfolio over the next 10 years will end within the range of ${ci_lower_ten_cumulative_return_mc:.2f} and ${ci_upper_ten_cumulative_return_mc:.02f}")


    # In[64]:


    # Configure a Monte Carlo simulation to forecast 10 years cumulative returns for low correlation portfolio
    #The weights should be split evenly across the portfolio
    # Run 500 samples.
    MC_10_yrs_low_correlation = MCSimulation(
        portfolio_data=low_correlation_df,
        weights=low_correlation_weight,
        num_simulation=500,
        num_trading_days=252*10
    )


    # In[65]:


    # Run the Monte Carlo simulation to forecast 10 years cumulative returns
    MC_10_yrs_low_correlation.calc_cumulative_return()


    # In[66]:


    # Visualize the 10-year Monte Carlo simulation by creating an
    # overlay line plot
    MC_10_yrs_low_correlation_line_plot = MC_10_yrs_low_correlation.plot_simulation()


    # In[67]:


    # Visualize the probability distribution of the 10-year Monte Carlo simulation 
    # by plotting a histogram
    MC_10_yrs_low_correlation_distribution_plot = MC_10_yrs_low_correlation.plot_distribution()


    # In[68]:


    # Generate summary statistics from the 10-year Monte Carlo simulation results
    MC_10_yrs_low_correlation_sum_statistics = MC_10_yrs_low_correlation.summarize_cumulative_return()

    # Review the 10-year Monte Carlo summary statistics
    #display(MC_10_yrs_low_correlation_sum_statistics)


    # In[70]:


    # Use the lower and upper `95%` confidence intervals to calculate the range of the possible outcomes for the low correlation portfolio
    ci_lower_ten_cumulative_return_lc = MC_10_yrs_low_correlation_sum_statistics[8]*investment_amount
    ci_upper_ten_cumulative_return_lc = MC_10_yrs_low_correlation_sum_statistics[9]*investment_amount

    # Print the result of your calculations
    print(f"There is a 95% chance that an investment of ${investment_amount} in the Low Correlation GrowWise portfolio over the next 10 years will end within the range of ${ci_lower_ten_cumulative_return_lc:.2f} and ${ci_upper_ten_cumulative_return_lc:.02f}")


    # In[ ]:




