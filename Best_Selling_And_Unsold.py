import pandas as pd
import matplotlib.pyplot as plt
import msvcrt    # import to press any to view dashboard

# Load the dataset
file_path = "Retail Sales Data Set.csv"
df = pd.read_csv(file_path)


class StoreAnalysisSystem:
    def __init__(self, df):
        self.df = df
        self.df["Date"] = pd.to_datetime(self.df["Date"], errors='coerce')
        self.df["Month"] = self.df["Date"].dt.strftime('%B')

    def get_sales_by_category(self):
        return self.df.groupby("Product Category")["Total Amount"].sum()
    
    def best_selling_product(self):
        sales_by_category = self.get_sales_by_category()
        best_category = sales_by_category.idxmax()
        best_sales = sales_by_category.max()
        total_sales = sales_by_category.sum()
        percentage = (best_sales / total_sales) * 100
        return best_category, best_sales, percentage
    
    def best_selling_per_month(self):
        sales_by_month = self.df.groupby(["Month", "Product Category"])['Total Amount'].sum()
        best_per_month = {}
        for month in self.df["Month"].dropna().unique():
            if month in sales_by_month:
                monthly_sales = sales_by_month.loc[month]
                best_product = monthly_sales.idxmax()
                best_sales = monthly_sales.max()
                best_per_month[month] = (best_product, best_sales)
        return best_per_month
    
    def unsold_products(self):
        all_categories = set(self.df["Product Category"].unique())
        sold_categories = set(self.get_sales_by_category().index)
        unsold = list(all_categories - sold_categories)
        return "None" if not unsold else ", ".join(unsold)
    
    def display_results(self):
        best_category, best_sales, percentage = self.best_selling_product()
        print("\n===== BEST SELLING AND UNSOLD PRODUCTS =====")
        print(f"Best Selling Product: {best_category} - ${best_sales:.2f} ({percentage:.2f}%)")
        
        print("\nBest Selling Product by Month:")
        best_monthly_sales = self.best_selling_per_month()
        for month in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
            if month in best_monthly_sales:
                product, sales = best_monthly_sales[month]
                print(f" {month}: {product} - ${sales:.2f}")
        
        print(f"\nUnsold Products: {self.unsold_products()}")
        print("========================================")
    
    def plot_best_selling_per_month(self):
        best_per_month = self.best_selling_per_month()
        
        # Sort months in correct order
        month_order = ["January", "February", "March", "April", "May", "June", "July",
                       "August", "September", "October", "November", "December"]
        sorted_best_per_month = {month: best_per_month[month] for month in month_order if month in best_per_month}
        
        # Extract data for plotting
        months = list(sorted_best_per_month.keys())
        products = [sorted_best_per_month[m][0] for m in months]
        sales = [sorted_best_per_month[m][1] for m in months]

        # Plot bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(months, sales, color='blue')
        plt.xlabel("Month")
        plt.ylabel("Total Sales ($)")
        plt.title("Best-Selling Product Category Per Month")
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # Annotate each bar with product names
        for i, (product, sale) in enumerate(zip(products, sales)):
            plt.text(i, sale + 500, product, ha='center', fontsize=10, rotation=45)

        # Show the plot
        plt.tight_layout()
        plt.show()
def display(self):
    analysis = StoreAnalysisSystem(df)
    analysis.display_results()
    print("\nPress Enter To View Dashbord:")
    msvcrt.getch()
    analysis.plot_best_selling_per_month()

