# ESPP # 
Employee Stock Purchase Plan Model

## Disclaimer ##
This project is for entertainment purposes only. Nothing in this project can be considered advice or guidance for investment decisions or, for that matter, any other decisions. If uncertain, always consult an investment advisor and/or accountant. The owner, creator, and any associated party of this project makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use.

COPYRIGHT POLICY: Unless otherwise noted, all content in this project is the property of the sole creator. All content is protected by U.S. and international copyright laws. When you quote the following material or repost content please make sure you give credit to the source.

Credits:
- Kalvin Hong Jun Choi - Financial Model
- Kyu Jin Kim - Python Project

## Before You Begin ##
You MUST follow the steps below to query for the stock prices.

1. Visit [IEX Cloud](iexcloud.io) to create an API Key.
2. In Tools/config_sample.py - replace YOUR_API_KEY_HERE with your API Key.
3. Rename the config_sample.py file to config.py.

## Description ##
This project runs a model for an Employee Stock Purchase Plan model and compares the different strategies between holding stocks based on the following inputs:

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
