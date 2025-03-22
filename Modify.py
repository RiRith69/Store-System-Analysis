import pandas as pd
import os
import msvcrt

file_path = "Retail Sales Data Set.csv"
df = pd.read_csv(file_path)

class StoreAnalysisSystem:
    def __init__(self, df):
        self.df = df

# Function to clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#TODO: Modify - Touch Lyheng
class Modify(StoreAnalysisSystem):
    def __init__(self, Transaction_ID=None, Date=None, Gender=None, Age=None, Age_Group=None, Product_Category=None, Quantity=None, Price_per_Unit=None, Total_Amount=None):
        self.Transaction_ID = Transaction_ID
        self.Date = Date
        self.Gender = Gender
        self.Age = Age
        self.Age_Group = Age_Group
        self.Product_Category = Product_Category
        self.Quantity = Quantity
        self.Price_per_Unit = Price_per_Unit
        self.Total_Amount = Total_Amount

    # This is Add Function: To Add More Customer 
    def add(self, file_name):
        self.collect_input(file_name)  
        new_data = pd.DataFrame([{
            "Transaction ID": self.Transaction_ID,
            "Date": self.Date,
            "Gender": self.Gender,
            "Age": self.Age,
            "Age Group": self.Age_Group,
            "Product Category": self.Product_Category,
            "Quantity": self.Quantity,
            "Price per Unit": self.Price_per_Unit,
            "Total Amount": self.Total_Amount
        }])
        new_data.to_csv(file_name, mode='a', header=False, index=False)
        print(f"Data added successfully with Transaction ID: {self.Transaction_ID}")
        print("Press any key to return to the menu...")
        msvcrt.getch()  # Wait for key press
        clear_screen()
        
    # This is Collect Input Function: To Input Information And Give Back to Add Function
    def collect_input(self, file_name):
        self.Transaction_ID = self.get_next_transaction_id(file_name)
        # Input Date 
        while True:
            try:
                day, month = map(int, input("Date (DD/MM): ").split('/'))
                if 1 <= month <= 12:
                    self.Date = f"{day:02d}/{month:02d}/2023"
                    break
                else:
                    print("Error: Month must be between 1-12.")
            except ValueError:
                print("Error: Enter date in DD/MM format.")
        # Input Gender
        gender_options = {"1": "Male", "2": "Female"}
        while True:
            choice_gender = input("Choose Gender (1. Male, 2. Female): ")
            if choice_gender in gender_options:
                self.Gender = gender_options[choice_gender]
                break
            print("Error: Choose a valid option (1 or 2).")
        # Input Age
        while True:
            try:
                self.Age = int(input("Age: "))
                if 17 < self.Age <= 100:
                    break
                else:
                    print("Age must be betwern 18 to 100, Input again....")
            except ValueError :
                print("Error: Age must be a number.")
        # Input Category
        category_options = {"1": "Clothing", "2": "Electronics", "3": "Beauty"}
        while True:
            choice = input("Choose Product Category (1. Clothing, 2. Electronics, 3. Beauty): ")
            if choice in category_options:
                self.Product_Category = category_options[choice]
                break
            print("Error: Choose a valid option (1, 2, or 3).")
        # Input Quantity
        while True:
            try:
                self.Quantity = int(input("Quantity: "))
                break
            except ValueError:
                print("Error: Quantity must be a number.")
        # Input Price Per Unit
        while True:
            try:
                user_input = input("Price per Unit: ").strip()
                
                if user_input:
                    self.Price_per_Unit = float(user_input)  
                else:
                    self.Price_per_Unit = int(user_input)  
                break  
            except ValueError:
                print("Error: Price must be a valid number.")

        self.Age_Group = self.get_age_group(self.Age)
        self.Total_Amount = self.Quantity * self.Price_per_Unit

    # This is Function: Get Age By Group
    def get_age_group(self, age):
        if 18 <= age <= 31:
            return "Adolescent"
        elif 32 <= age <= 54:
            return "Middle Age"
        elif 55 <= age < 65:
            return "Old"
        else:
            return "Unknown"

    def get_next_transaction_id(self, file_name):
        try:
            df = pd.read_csv(file_name)
            if df["Transaction ID"].empty:
                return 1000
            return df["Transaction ID"].max() + 1
        except (FileNotFoundError, KeyError):
            return 1000
    # This is Function: Update
    def update(self, file_name):
        df = pd.read_csv(file_name)
        # Input ID 
        while True:
            transaction_id = input("Enter the ID to update: ").strip()
            try:
                transaction_id = int(transaction_id)  
            except ValueError:
                print("\nError: Invalid input ID.")
                continue  
            if transaction_id not in df["Transaction ID"].values:
                print("\nError: ID not found. Please try again.")
            else:
                break  

        index = df[df["Transaction ID"] == int(transaction_id)].index[0]
    	# Input Category
        new_product_category = {"1": "Clothing", "2": "Electronics", "3": "Beauty"}
        while True:
            choice = input("Choose Product Category (1. Clothing, 2. Electronics, 3. Beauty): ")
            if choice in new_product_category:
                    df.at[index, "Product Category"] = new_product_category[choice]
                    break
            print("Error: Choose a valid option (1, 2, or 3).")

        # Input Quantity
        while True:
            try: 
                new_quantity = int(input("Input Quantity: ").strip())
                if new_quantity:
                    df.at[index, "Quantity"] = int(new_quantity)
                    break
            except ValueError:
                print("Error: Value Error. Please try again.")
        # Input Price Per Unit
        while True:  
            try:
                input_per_unit = input("Price per Unit: ").strip()
                if input_per_unit:
                    new_price_per_unit = float(input_per_unit)  
                else:
                    new_price_per_unit = int(input_per_unit) 
                    if new_price_per_unit:
                        df.at[index, "Price per Unit"] = float(new_price_per_unit) 
                break 
            except ValueError:
                print("Error: Value Error. Please try again.")
      
        quantity = df.at[index, "Quantity"]
        price_per_unit = df.at[index, "Price per Unit"]
        df.at[index, "Total Amount"] = quantity * price_per_unit

        df.to_csv(file_name, index=False)
        print("Data updated successfully.")
        print("Press any key to return to the menu...")
        msvcrt.getch()  # Wait for key press
        clear_screen()
    # This is Function: Delete
    def delete(self, file_name):
        try:
            df = pd.read_csv(file_name)
            if df.empty:
                print("The File has nothing!! ")
                return
            if "Transaction ID" not in df.columns:
                print(" Transaction ID column dont have in file.")
                return
            while True:
                try:
                    transaction_id = int(input("Enter the ID to delete: ").strip())

                    if transaction_id not in df["Transaction ID"].values:
                        print("Error: ID not found. Please try again.")
                    else:
                        df = df[df["Transaction ID"] != transaction_id]
                        df = df.reset_index(drop=True)
                        df["Transaction ID"] = df.index + 1  
                        df.to_csv(file_name, index=False)
                        print("Data deleted successfully.")
                        print("Press any key to return to the menu...")
                        msvcrt.getch()  # Wait for key press
                        clear_screen()
                        break  
                except ValueError:
                    print("Error: Invalid input ID.")
        except FileNotFoundError:
            print(f"Error: The file '{file_name}' was not found.")

# This is Function : Menu
def menu():
    modify = Modify()
    file_name = "Retail Sales Data Set.csv"
    while True:
        print("\t\t\t\t=========================================")
        print("\t\t\t\t Welcome To Modify STORE ANALYSIS SYSTEM")
        print("\t\t\t\t=========================================")
        print("")
        print("\t\t\t\t1. Add Data")
        print("\t\t\t\t2. Update Data")
        print("\t\t\t\t3. Delete Data")
        print("\t\t\t\t4. Exit....!!")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            modify.add(file_name)
        elif choice == "2":
            modify.update(file_name)
        elif choice == "3":
            modify.delete(file_name)
        elif choice == "4":
            print("Exiting the program. See you letter")
            break
        else:
            print("Invalid choice!! Please select (1-4).")