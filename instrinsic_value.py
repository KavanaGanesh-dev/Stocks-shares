import os
import pandas as pd

# Inputs (you can change these values)
data = {
    'Input': ['Current Stock Price', 'Intrinsic Value', 'Discount Rate', 'Investment Amount', 'Investment Horizon (Years)', 'Expected Return', 'Margin of Safety (%)'],
    'Value': [294, round(162.98,2), round(0.10,2), 1000, 5, round(0.10,2), 10]
}

# Create DataFrame
inputs = pd.DataFrame(data)

# Derived Calculations
market_price = inputs.loc[inputs['Input'] == 'Current Stock Price', 'Value'].values[0]
intrinsic_value = inputs.loc[inputs['Input'] == 'Intrinsic Value', 'Value'].values[0]
discount_rate = inputs.loc[inputs['Input'] == 'Discount Rate', 'Value'].values[0]
# print(discount_rate)
investment = inputs.loc[inputs['Input'] == 'Investment Amount', 'Value'].values[0]
horizon = int(inputs.loc[inputs['Input'] == 'Investment Horizon (Years)', 'Value'].values[0])
expected_return = inputs.loc[inputs['Input'] == 'Expected Return', 'Value'].values[0]
margin_of_safety = inputs.loc[inputs['Input'] == 'Margin of Safety (%)', 'Value'].values[0]

# Valuation Comparison
if intrinsic_value > market_price:
    recommendation = 'Potential Buy'
elif intrinsic_value == market_price:
    recommendation = 'Fairly Priced'
else:
    recommendation = 'Overvalued'

# Apply Margin of Safety
safe_price = intrinsic_value * (1 - margin_of_safety / 100)

# Future Value / Profit Projection
future_value = investment * (1 + expected_return) ** horizon
profit = future_value - investment

# Results DataFrame
results = pd.DataFrame({
    'Metric': ['Recommendation', 'Safe Buy Price', 'Future Value', 'Profit'],
    'Value': [recommendation, safe_price, future_value, profit]
})

# Export to Excel
with pd.ExcelWriter('/Users/kavanakiran/Documents/stocks/TSMC_stocks.xlsx') as writer:
    inputs.to_excel(writer, sheet_name='Inputs', index=False)
    results.to_excel(writer, sheet_name='Results', index=False)



print(os.getcwd())