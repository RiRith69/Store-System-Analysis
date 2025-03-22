import pandas as pd
import matplotlib.pyplot as plt
import mplcursors
from abc import ABC, abstractmethod
import msvcrt

#-------------------------
# Read CSV file using pandas
#-------------------------
file_path = "Retail Sales Data Set.csv"
df = pd.read_csv(file_path)
df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y", errors='coerce')

#------------------
# Abstract Base Class
#------------------

class SellTracker(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def data_detail(self, *args):
        pass

    @abstractmethod
    def income(self, *args):
        pass

    def each_category_income(self, inputData, category):
        category_data = inputData[inputData["Product Category"] == category]
        return category_data["Total Amount"].sum()

    @abstractmethod
    def display_income(self, *args):
        pass

    @abstractmethod
    def sold(self, *args):
        pass

    def each_category_sold(self, inputData, category):
        category_data = inputData[inputData["Product Category"] == category]
        return category_data["Quantity"].sum()

    def compare_age(self, data, min_age, max_age):
        group = data[(data["Age"] >= min_age) & (data["Age"] <= max_age)]
        return group["Quantity"].sum()

    def adolescent(self, data):
        return self.compare_age(data, 18, 31)

    def middle_age(self, data):
        return self.compare_age(data, 32, 54)

    def old(self, data):
        return self.compare_age(data, 55, 64)

    @abstractmethod
    def display_report(self, *args):
        pass


# -----------------
# Monthly Sales Class
# -----------------
class MonthlySell(SellTracker):
    def __init__(self, data):
        super().__init__(data)

    def data_detail(self, month, year):
        return self.data[(self.data["Date"].dt.month == month) & (self.data["Date"].dt.year == year)]

    def income(self, month, year):
        return self.data_detail(month, year)["Total Amount"].sum()

    def display_income(self, month, year):
        print(f"\nMonth: {month} in {year} Income: ${self.income(month, year)}")
        print(f"Electronics Income: ${self.each_category_income(self.data_detail(month, year), 'Electronics')}")
        print(f"Beauty Income: ${self.each_category_income(self.data_detail(month, year), 'Beauty')}")
        print(f"Clothing Income: ${self.each_category_income(self.data_detail(month, year), 'Clothing')}")

    def sold(self, month, year):
        return self.data_detail(month, year)["Quantity"].sum()

    def display_report(self, month, year):
        print(f"\t Month {month} in {year} Report: ")
        print(f"Sold Products: {self.sold(month, year)} | Income: ${self.income(month, year)}")
        print(f"Adolescent Sales: {self.adolescent(self.data_detail(month, year))}")
        print(f"Middle Age Sales: {self.middle_age(self.data_detail(month, year))}")
        print(f"Old Age Sales: {self.old(self.data_detail(month, year))}")


# -----------------
# Yearly Sales Class
# -----------------
class YearlySell(SellTracker):
    def __init__(self, data):
        super().__init__(data)

    def data_detail(self, year):
        return self.data[self.data["Date"].dt.year == year]

    def income(self, year):
        return self.data_detail(year)["Total Amount"].sum()

    def display_income(self, year):
        print(f"\nYear: {year} Income: ${self.income(year)}")
        print(f"Electronics Income: ${self.each_category_income(self.data_detail(year), 'Electronics')}")
        print(f"Beauty Income: ${self.each_category_income(self.data_detail(year), 'Beauty')}")
        print(f"Clothing Income: ${self.each_category_income(self.data_detail(year), 'Clothing')}")

    def sold(self, year):
        return self.data_detail(year)["Quantity"].sum()

    def display_report(self, year):
        print(f"\t Year {year} Report: ")
        print(f"Sold Products: {self.sold(year)} | Income: ${self.income(year)}")


# -----------------
# Total Sales Class
# -----------------
class TotalSell(SellTracker):
    def __init__(self, data):
        super().__init__(data)

    def data_detail(self):
        return self.data

    def income(self):
        return self.data["Total Amount"].sum()

    def display_income(self):
        print(f"\nTotal Income: ${self.income()}")
        print(f"Electronics Income: ${self.each_category_income(self.data, 'Electronics')}")
        print(f"Beauty Income: ${self.each_category_income(self.data, 'Beauty')}")
        print(f"Clothing Income: ${self.each_category_income(self.data, 'Clothing')}")

    def sold(self):
        return self.data["Quantity"].sum()

    def display_report(self):
        print("\t Total Report: ")
        print(f"Sold Products: {self.sold()} | Income: ${self.income()}")


# Initialize Objects
monthly = MonthlySell(df)
yearly = YearlySell(df)
totally = TotalSell(df)


# -----------------------
# Yearly Income Bar Chart
# -----------------------
def yearly_bar_chart(year):
    x = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    y = [monthly.income(month, year) for month in range(1, 13)]
    
    bars = plt.bar(x, y, color='b')
    plt.xlabel("Month")
    plt.ylabel("Income ($)")
    plt.title(f"{year} Income Bar Chart")
    
    cursor = mplcursors.cursor(bars, hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"${sel.target[1]:,.2f}"))
    
    plt.show()


# -------------------------------
# Income Menu
# -------------------------------
def total_sell():
    while True:
        print("\n=============================")
        print("||      Income Features    ||")
        print("=============================")
        print("")
        print("1. Monthly Income")
        print("2. Yearly Income")
        print("3. Total Income")
        print("4. Exit")

        try:
            option = int(input("\nEnter your choice (1-4): "))
            if option == 1:
                while True:
                    try:
                        year = int(input("\nEnter year (yyyy): "))
                        break
                    except ValueError:
                        print("Error: Value, Input year again!!")

                while True:
                    try:
                        month = int(input("Enter month (1-12): "))
                        break
                    except ValueError:
                        print("Error: Value, Input month again!!")

                # Display
                monthly.display_income(month, year)

            elif option == 2:
                while True:
                    try:
                        year = int(input("\nEnter year (yyyy): "))
                        break
                    except ValueError:
                        print("Error: Value, Input year again!!")

                # Display
                yearly.display_income(year)

                print("\nPress any key to view dashboarh......")
                msvcrt.getch()  # Wait for key press

                yearly_bar_chart(year)
                
            elif option == 3:
                totally.display_income()

            elif option == 4:
                print("Program Ending.... Goodbye!")
                break
            else:
                print("!! Invalid choice, please try again.")
         
        except ValueError:
            print("!! Error: Invalid input, please try again.")
            continue

# -------------------------------
# Generate General Report
# -------------------------------
def general_report():
    while True:
        print("\n=============================")
        print("||     General Reports     ||")
        print("=============================")
        print("")
        print("1. Monthly Report")
        print("2. Yearly Report")
        print("3. Total Report")
        print("4. Exit")
        try:
            option = int(input("\nEnter your choice (1-4): "))
            if option == 1:
                while True:
                    try:
                        year = int(input("\nEnter year (yyyy): "))
                        break
                    except ValueError:
                        print("Error: Value, Input year again!!")

                while True:
                    try:
                        month = int(input("Enter month (1-12): "))
                        break
                    except ValueError:
                        print("Error: Value, Input month again!!")
                # Display
                monthly.display_report(month, year)

            elif option == 2:
                while True:
                    try:
                        year = int(input("\nEnter year (yyyy): "))
                        break
                    except ValueError:
                        print("Error: Value, Input year again!!")
                # Display
                yearly.display_report(year)
                
            elif option == 3:
                totally.display_report()
            elif option == 4:
                break
            else:
                print("Invalid choice, try again.")
        except ValueError:
            print("Error: Value, Input again!!")
            


