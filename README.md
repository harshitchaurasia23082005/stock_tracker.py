feat: add interactive stock portfolio tracker CLI

Implement a command-line tool that lets users select from a
predefined set of stocks, input share quantities, and view a
running portfolio with per-stock and total investment values.

- Validate stock symbol and quantity input with retry loops
- Calculate per-stock investment and running total
- Display formatted portfolio summary table
- Support exporting results to .txt or .csv on request
