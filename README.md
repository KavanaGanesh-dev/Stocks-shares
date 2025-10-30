# Stocks-shares
**Stock Valuation Calculator**
This project provides a python script to analyse company's intrinsic value versus its current market price and generate investment insights like Margin of Safety, future value and profit projections. It also exports results to an Excel File for tracking.

**Features**
1. Compares intrinsic value with the current market price
2. Calculates safe buy price based on margin of safety
3. Projects future value and profit over an investment horizon
4. Generates a recommendation (Potential Buy, Failry priced, OverValued)
5. Export all results to am organized Excel File


**How it Works**
Script uses key financial inputs such as
  1. Cuurent stock price
  2. Intinsic Value
  3. Discount Rate
  4. Investment Amount
  5. Investment Horizon
  6. Expected Return
  7. Margin of Safety

**Then it Computes**
  1. Safe Buy Price = Intrinsic Value * (1 -  Margin of Safety)
  2. Future Value = Investment * (1 + Expected Return)^ Years
  3. Profit = Future Value - Investment

