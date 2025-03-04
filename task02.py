import csv
import random
import matplotlib.pyplot as plt

# Set up casual logging
def log(message):
    print(f"[LOG] {message}")

class Stock:
    """A class to represent a stock in my portfolio."""
    
    def __init__(self, stock_no, num_shares, buy_price, current_price):
        self.stock_no = stock_no
        self.num_shares = num_shares
        self.buy_price = buy_price
        self.current_price = current_price

    def curr_value(self):
        """Calculate how much this stock is worth now."""
        return self.num_shares * self.current_price

    def profit_loss(self):
        """Calculate how much I've made or lost on this stock."""
        return self.curr_value() - (self.num_shares * self.buy_price)

    def to_list(self):
        """Get stock data as a list for saving."""
        return [self.stock_no, self.num_shares, self.buy_price, self.current_price]

class Portfolio:
    """A class to manage my collection of stocks."""
    
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        """Add a new stock to my portfolio."""
        self.stocks.append(stock)
        log(f"Added stock #{stock.stock_no} to my portfolio. Nice!")

    def price_update(self, stock_no, new_price):
        """Update the price of a stock in my portfolio."""
        for stock in self.stocks:
            if stock.stock_no == stock_no:
                old_price = stock.current_price  # Unnecessary variable assignment
                stock.current_price = new_price
                log(f"Updated stock #{stock_no} price to ${new_price:.2f}. Old price was ${old_price}.")
                return
        print("Hmm, can't find that stock in my portfolio.")

    def remove_stock(self, stock_no):
        """Remove a stock from my portfolio, with a little confirmation."""
        for stock in self.stocks:
            if stock.stock_no == stock_no:
                confirmation = input(f"Are you sure you want to remove stock #{stock_no}? (y/n): ")
                if confirmation.lower() == 'y':
                    self.stocks.remove(stock)
                    log(f"Removed stock #{stock_no} from my portfolio. Bye-bye!")
                return
        print("Nope, that stock isn't in my portfolio.")

    def show_portfolio(self):
        """Show all the stocks I own, sorted by how well they're doing."""
        if not self.stocks:
            print("My portfolio is empty. Time to buy some stocks!")
            return

        # Sort stocks by profit/loss using a manual loop instead of a list comprehension
        sorted_stocks = []
        for stock in self.stocks:
            inserted = False
            for i in range(len(sorted_stocks)):
                if stock.profit_loss() > sorted_stocks[i].profit_loss():
                    sorted_stocks.insert(i, stock)
                    inserted = True
                    break
            if not inserted:
                sorted_stocks.append(stock)

        total_investment = total_current_value = 0
        print("\nMY STOCK PORTFOLIO:")
        print('-' * 40)

        for stock in sorted_stocks:
            current_value = stock.curr_value()
            pl = stock.profit_loss()
            total_investment += stock.num_shares * stock.buy_price
            total_current_value += current_value

            sign = "+" if pl >= 0 else ""
            print(f"Stock#{stock.stock_no}: {stock.num_shares} shares")
            print(f"~ Buy Price: ${stock.buy_price:.2f}")
            print(f"~ Current Price: ${stock.current_price:.2f}")
            print(f"~ Value: ${current_value:.2f} {sign}${abs(pl):.2f}")
            print("-" * 40)

        overall_pl = total_current_value - total_investment
        sign = "+" if overall_pl >= 0 else ""
        print(f"Total Investment: ${total_investment:.2f}")
        print(f"Current Portfolio Value: ${total_current_value:.2f}")
        print(f"Overall Profit/Loss: {sign} ${abs(overall_pl):.2f}")

    def save_to_csv(self, filename):
        """Save my portfolio to a CSV file."""
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Stock No", "Num Shares", "Buy Price", "Current Price"])
            for stock in self.stocks:
                writer.writerow(stock.to_list())
        log("Saved my portfolio to CSV. Hope it's accurate!")

    def load_from_csv(self, filename):
        """Load my stocks from a CSV file."""
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    stock = Stock(
                        stock_no=int(row['Stock No']),
                        num_shares=int(row['Num Shares']),
                        buy_price=float(row['Buy Price']),
                        current_price=float(row['Current Price'])
                    )
                    self.add_stock(stock)
        except FileNotFoundError:
            log("Couldn't find the CSV file. Starting fresh!")
        except Exception as e:
            log(f"Error loading CSV file: {e}. Something went wrong.")

    def simulate_market(self, stock):
        """Simulate some market changes for a stock."""
        change = random.uniform(-0.05, 0.05)  # ±5% change
        stock.current_price *= (1 + change)

    def visualize_portfolio(self):
        """Show how my stocks are doing visually."""
        stock_nos = [stock.stock_no for stock in self.stocks]
        values = [stock.curr_value() for stock in self.stocks]
        colors = ['green' if stock.profit_loss() >= 0 else 'red' for stock in self.stocks]

        plt.bar(stock_nos, values, color=colors)
        plt.xlabel('Stock Number')
        plt.ylabel('Current Value')
        plt.title('My Stock Portfolio Values')
        plt.show()

        # Trend view of total investment vs current value
        total_investment = [stock.num_shares * stock.buy_price for stock in self.stocks]
        plt.plot(stock_nos, total_investment, label='Total Investment', marker='o')
        plt.plot(stock_nos, values, label='Current Value', marker='o')
        plt.xlabel('Stock Number')
        plt.ylabel('Value')
        plt.title('Investment vs Current Value')
        plt.legend()
        plt.show()

def main():
    portfolio = Portfolio()
    portfolio.load_from_csv('portfolio.csv')

    while True:
        print('MAIN MENU')
        print("1. Add Stock")
        print("2. Update Price")
        print("3. Remove Stock")
        print("4. Show Portfolio")
        print("5. Visualize Portfolio")
        print("6. Exit")

        choice = input("What's your choice? ")

        if choice == "1":
            try:
                stock_no = int(input('Enter the stock number: '))
                num_shares = int(input('How many shares? '))
                buy_price = float(input('What was the buy price per share? '))
                current_price = float(input('What’s the current market price? '))
                stock = Stock(stock_no, num_shares, buy_price, current_price)
                portfolio.add_stock(stock)
                print("Stock added! 🎉")
            except ValueError:
                print("Oops, something went wrong with the inputs. Try again.")

        elif choice == "2":
            try:
                stock_no = int(input('Enter the stock number to update price: '))
                new_price = float(input("What’s the new market price? "))
                portfolio.price_update(stock_no, new_price)
            except ValueError:
                print("Oops, that wasn't a valid number. Try again.")

        elif choice == "3":
            try:
                stock_no = int(input('Enter the stock number you want to remove: '))
                portfolio.remove_stock(stock_no)
            except ValueError:
                print("That input doesn’t look right. Give it another shot.")

        elif choice == "4":
            portfolio.show_portfolio()

        elif choice == "5":
            portfolio.visualize_portfolio()

        elif choice == "6":
            print("See you later! 👋")
            break

        else:
            print("Hmm, I didn't catch that. Choose a valid option.")

        # Automatically save after every change
        portfolio.save_to_csv('portfolio.csv')
if __name__ == "__main__":
    main()