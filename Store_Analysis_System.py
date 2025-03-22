import pandas as pd
import os
import matplotlib.pyplot as plt
import mplcursors
from Customer_Behavior import displayDetailWithAge, Bar_chart
from Best_Selling_And_Unsold import display
from Modify import menu
from Total_And_Report import total_sell, general_report
import msvcrt  # Import to allow "press any key to continue"

# Load the dataset
file_path = "Retail Sales Data Set.csv"
df = pd.read_csv(file_path)

class StoreAnalysisSystem:
    def __init__(self, df):
        self.df = df

# Function to clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main menu loop
while True:
    try:
        clear_screen()
        # Display Menu
        print("\t\t\t\t==================================")
        print("\t\t\t\t Welcome To STORE ANALYSIS SYSTEM")
        print("\t\t\t\t==================================\n")
        print("\t\t\t\t1. Customer Behavior")
        print("\t\t\t\t2. Best Selling and Unsold Category")
        print("\t\t\t\t3. Total Sale in Stock")
        print("\t\t\t\t4. Modify System")
        print("\t\t\t\t5. General Report")
        print("\t\t\t\t6. Exit\n")
        
        # Get user choice
        choices = int(input("\t\t\t\tEnter your choice: "))

        # Option 1: Customer Behavior - Chren Sophearith
        if choices == 1:
            clear_screen()
            displayDetailWithAge(df)

            print("\nPress any key to view the Dashboard...")
            msvcrt.getch()  # Wait for key press=
            Bar_chart(df)

            print("\nPress any key to return to the menu...")
            msvcrt.getch()  # Wait for key press

        # Option 2: Best Selling & Unsold - Techleng Tang
        elif choices == 2:
            clear_screen()
            display(df)

            print("\nPress any key to return to the menu...")
            msvcrt.getch()  # Wait for key press

        # Option 3: Total Sell - Rith Phearinsathya
        elif choices == 3:
            clear_screen()
            print("Total Sale in Stock feature is under development!")

            total_sell()     

            print("\nPress any key to return to the menu...")
            msvcrt.getch()  # Wait for key press

        # Option 4: Modify - Touch Lyheng
        elif choices == 4:
            clear_screen()
            menu()  # Call modify function

            print("\nPress any key to return to the menu...")
            msvcrt.getch()  # Wait for key press

        # Option 5: Report - Rith Phearinsathya
        elif choices == 5:
            clear_screen()
            print("General Report feature is under development!")

            general_report()            

            print("\nPress any key to return to the menu...")
            msvcrt.getch()  # Wait for key press

        # Option 6: Exit Program
        elif choices == 6:
            clear_screen()
            print("Program Ending.... Goodbye!")
            break

        # Invalid choice 
        else:
            print("\nInvalid choice! Please enter a number between 1 and 6.")
            print("Press any key to continue...")
            msvcrt.getch()  # Wait before reloading the menu

    except ValueError:
        print("\nError: Please enter a valid number!")
        print("Press any key to continue...")
        msvcrt.getch()  # Wait before reloading the menu

