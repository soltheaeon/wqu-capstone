#region imports
from AlgorithmImports import *
#endregion
from datetime import date

class RunConfig:
    # Start date for backtesting
    StartDate = date(2017, 1, 1)
    
    # End date for backtesting
    EndDate = date(2019, 12, 31)
    
    # Initial Cash
    StrategyCash = 1900000
    
    # Resolution of the price data
    Resolution = Resolution.Daily

    # Set the Account Currency code
    AccountCurrency = 'USD'
    
    # # Benchmark Index used for evaluation
    Benchmark = "SPY"

    # Num of Stocks - pick top #of stocks
    NumOfStock = 50

    # Flag to indicate if Value/Quality Smart Beta model should be run
    # Set 'True' for Value and 'False' for Quality
    RunValueSmartBeta = True
    
    # Use ML Based rebalancing
    UseMLForRebalancing = False

