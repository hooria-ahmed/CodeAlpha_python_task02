# Stock Portfolio Management System

A simple yet effective command-line tool for managing a stock portfolio with visualization, real-time updates, and CSV file handling.

## Features

- Add, update, and remove stocks in the portfolio.
- Track profit/loss for individual stocks and the overall portfolio.
- Automatically save and load portfolio data from a CSV file.
- Simulate market changes to observe stock fluctuations.
- Visualize portfolio performance using bar charts and line graphs.

## How to Use

1. Run the script, and the main menu will be displayed.
2. Choose from the available options:
   - Add a new stock with stock number, shares, buy price, and current price.
   - Update the stock price when the market value changes.
   - Remove a stock from the portfolio with confirmation.
   - Display all stocks along with their profit/loss details.
   - Visualize stock values and trends graphically.
   - Exit the program (data is automatically saved).

## Running the Program

Ensure you have Python installed (3.x recommended) and required dependencies:

```bash
pip install matplotlib
python stock_portfolio.py
```

## Example Output

```
MAIN MENU
1. Add Stock
2. Update Price
3. Remove Stock
4. Show Portfolio
5. Visualize Portfolio
6. Exit

What's your choice? 4

MY STOCK PORTFOLIO:
----------------------------------------
Stock#1: 10 shares
~ Buy Price: $50.00
~ Current Price: $55.00
~ Value: $550.00 +$50.00
----------------------------------------
Overall Profit/Loss: +$50.00
```

## Requirements

- Python 3.x
- Matplotlib for visualization
- CSV file handling for persistent storage

## Internship Project

This stock portfolio management system was developed as part of my internship at **CodeAlpha**.

## Author

Developed as a command-line stock tracking and visualization tool.

## License

This project is open-source and available for modification and distribution.

