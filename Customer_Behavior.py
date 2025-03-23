import pandas as pd
file_path = "Retail Sales Data Set.csv"
df = pd.read_csv(file_path)

class StoreAnalysisSystem:
    def __init__(self, df):
        self.df = df


#TODO: Customer behavior (Chren Sophearith)
class CustomerBehavior(StoreAnalysisSystem):
    def __init__(self, df):
        super().__init__(df)
    def TotalQuantity(self):
        #Calculate the total of the quantity
        total = self.df["Quantity"].sum()
        gender = self.df["Gender"].count()
        #Display total and percentage
        print(f"\t\t\t\t========= Dispay =========")
        print(f"\t\t\t\t==========================")
        print(f"\t\t\t\t Total qunatity is: {total} ")
        print(f"\t\t\t\t Total percentage: {(total / total) * 100}%")
        print(f"\t\t\t\t Total customer:{gender}\t  ")
        print(f"\t\t\t\t==========================")
    def compareAge18to31(self):
        # Filter the DataFrame for customers aged between 18 and 31
        compareAge = self.df[(self.df['Age'] >= 18) & (self.df['Age'] <= 31)]
        
        # Quantity computational
        adolescent = compareAge['Quantity'].sum()
        return adolescent

        
    def CompareAge32to54(self):
        # Filter the DataFrame for customers aged between 32 and 54
        compareAge = self.df[(self.df['Age'] >= 32) & (self.df['Age'] <= 54)]
        
        # Qunatity computational
        middle = compareAge['Quantity'].sum()
        return middle

        
    def CompareAge55to64(self):
        # Filter the DataFrame for customers aged between 55 and 64
        compareAge = self.df[(self.df['Age'] >= 55) & (self.df['Age'] <= 64)]
        
        # Quantity computaional
        old = compareAge['Quantity'].sum()
        return old
    
    #Gender between age 18 to 31 years old
    def gender18to31(self):
        compareAge = self.df[(self.df['Age'] >= 18) & (self.df['Age'] <= 31)]
        total_customer = compareAge['Gender'].count()
        #We use shape[0] to give you number of row if we use shape[1] it will give you number of column 
        total_male = compareAge[compareAge['Gender'] == 'Male'].shape[0]
        total_female = compareAge[compareAge['Gender'] == 'Female'].shape[0]
        male_percentage = (100 * total_male) / total_customer
        female_percentage = (100 * total_female) / total_customer
        #Dispplay gender
        print()
        print("\t\tCustomer Between 18 - 32 ")
        print(f"Total customer between 18 to 32 years old: {total_customer} customer = 100%")
        print(f"Total male: {total_male} = {male_percentage:.2f}%")
        print(f"Total female: {total_female} = {female_percentage:.2f}%")
        print("===========================================================")
        
        #Gender between age 32 to 54 years old
    def gender32to54(self):
        compareAge = self.df[(self.df['Age'] >= 32) & (self.df['Age'] <= 54)]
        total_customer = compareAge['Gender'].count()
        #We use shape[0] to count all the condition in row 
        total_male = compareAge[compareAge['Gender'] == 'Male'].shape[0]
        total_female = compareAge[compareAge['Gender'] == 'Female'].shape[0]
        male_percentage = (100 * total_male) / total_customer
        female_percentage = (100 * total_female) / total_customer
        #Display gender
        print("\t\tCustomer Between 32 - 54")
        print(f"Total customer between 32 to 54 years old: {total_customer} customer = 100%")
        print(f"Total male: {total_male} = {male_percentage:.2f}%")
        print(f"Total female: {total_female} = {female_percentage:.2f}%")
        print("===========================================================")
        
        #Gender between age 55 to 64 years old
    def gender55to64(self):
        compareAge = self.df[(self.df['Age'] >= 55) & (self.df['Age'] <= 64)]
        total_customer = compareAge['Gender'].count()
        #We use shape[0] to count all the condition in row 
        total_male = compareAge[compareAge['Gender'] == 'Male'].shape[0]
        total_female = compareAge[compareAge['Gender'] == 'Female'].shape[0]
        male_percentage = (100 * total_male) / total_customer
        female_percentage = (100 * total_female) / total_customer
        #Display gender
        print("\t\tCustomer Between 55 - 64")
        print(f"Total customer between 55 to 64 years old: {total_customer} customer = 100%")
        print(f"Total male: {total_male} = {male_percentage:.2f}%")
        print(f"Total female: {total_female} = {female_percentage:.2f}%")
        print("===========================================================")
    #Display the information
def displayDetailWithAge(self):
    #create an object
    compare = CustomerBehavior(df)
    compare.TotalQuantity()
    compare.gender18to31()
    compare.gender32to54()
    compare.gender55to64()
    
# print("\nPress Enter To view Dashboard........ ")

def Bar_chart(self):
    import matplotlib.pyplot as plt
    import mplcursors
    #Create an objects
    customer_behavior = CustomerBehavior(df)
    # x-axis (horizontal)
    x = ["Adolescent(18-31)", "Middle(32-54)", "Old(55-64)"]
    # y-axis (vertical axis)
    y = [customer_behavior.compareAge18to31(), customer_behavior.CompareAge32to54(), customer_behavior.CompareAge55to64()]
    # Size of the bar chart
    plt.figure(figsize=(5, 5))
    plt.xlabel("Age")
    plt.ylabel("Quantity")
    plt.title("Quantity Bar Chart")
    #Set the bar chart to red color
    cursor = mplcursors.cursor(plt.bar(x, y, color='blue'), hover=False)
    #Customized text display when use hover on the bar chart  (sel: represent the event) Annotation is the small text bar
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"{sel.target[1]}quantity"))
    #set text change the text in the box
    plt.show()
    # display(df)

