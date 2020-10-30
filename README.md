# ESPP
Employee Stock Purchase Plan Model

-----------------------------------------------------------------
**IMPORTANT**

You MUST do the following to query for the stock prices.

1. Visit [IEX Cloud](iexcloud.io) to create an API Key.
2. Replace "YOUR_API_KEY_HERE" in the API Key in the Tools/secret_sample.json file with your newly created API Key.
3. Rename this file to secret.json.

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
    
Future Sale:

    Future Date
