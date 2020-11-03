# ESPP
Employee Stock Purchase Plan Model

-----------------------------------------------------------------
**IMPORTANT** - You MUST follow the steps below to query for the stock prices.

1. Visit [IEX Cloud](iexcloud.io) to create an API Key.
2. In Tools/config_sample.py - replace YOUR_API_KEY_HERE with your API Key.
3. Rename this file to config.py.

-----------------------------------------------------------------
This project runs an ESPP model and determines the strategy for holding stocks based on the following inputs:

Model:

    Symbol
    Quantity
    Purchase Date
    Transaction Cost
    Diversification Benefit

Tax Bracket:

    Income
    Short Term
    Long Term
    
Future Sale (Loop):

    Future Date
