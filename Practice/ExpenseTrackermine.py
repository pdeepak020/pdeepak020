import csv
class ExpenseTracker():

    def __init__(self,filename="data.csv"):
        self.filename = filename
        self.dic=[]
        self.loadExpenses()

    def addExpense(self,date,amount,category,desc):
        self.dic.append({"Date":date,"Amount":amount,"Category":category,"Desc":desc})
    
    def saveExpense(self):
          with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Date", "Amount", "Category", "Desc"])
            for row in self.dic:
                writer.writerow([row['Date'],row['Amount'],row['Category'],row['Desc']])
          print("Expense saved Successfully!!")
            
    def loadExpenses(self):
        try:
            with open(self.filename, "r",  newline='') as filein:
                reader = csv.DictReader(filein)
                for rows in reader:
                    values={"Date":rows['Date'],"Amount":rows['Amount'],'Category':rows['Category'],'Desc':rows['Desc']}
                    self.dic.append(values)
            print("Lets Start ExpenseTracking!! \nData Refresh!! Loaded your Last Expenses :)")
        except:
            print("Lets Start ExpenseTracking!!")
    
    
    def displayExpense(self):
        if not self.dic:
            print("no expenses added yet")
        else:
            for row in self.dic:
                if all(key in row for key in ['Date','Amount','Category','Desc']):
                    print(row["Date"],row["Amount"],row["Category"],row["Desc"])
                else:
                    print('empty values')

    def trackBudget(self):
        budget=float(input("Enter the amount as budget of your Month"))
        self.compareBudget(budget)

    def compareBudget(self,budget):
        sum=0
        if not self.dic:
            print("no expenses added yet, can't calculate budget")
        else:
            for row in self.dic:
                if all(key in row for key in ['Date','Amount','Category','Desc']):
                    sum=float(sum)+float(row['Amount'])
                else:
                    print('empty values')
                    
        if budget >= sum :
            val= budget - sum
            print("You still have :",val,"bucks to spent!!")
        else:
            print("You have exceeded your budget!")

    def menu(self):
        while True:
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Track Budget")
            print("4. Save Expenses")
            print("5. Exit")

            print("Choose an option Please")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                date=str(input("Enter date in YYYY-MM-DD format please:"))
                amount=float(input("Enter amount please:"))
                category=str(input("Enter category of expense please"))
                desc=str(input("Enter description of expense please"))
                print("All done")
                self.addExpense(date,amount,category,desc)
            elif choice == 2:
                self.displayExpense()
            elif choice == 3:
                self.trackBudget()
            elif choice == 4:
                self.saveExpense()
            elif choice == 5:
                break
            else:
                "Invalid option, Please choose a valid option"

    #Track start!!
tracker = ExpenseTracker()
tracker.menu()

