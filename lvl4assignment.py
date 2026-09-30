#create a python list entering expenses until they enter a 0 to finish
#add expenses to the list 
expenses_list= []
expenses=float(input("Enter an expense or enter 0 to finish:"))

# while expenses is not 0, keep asking the user for input
while expenses != 0:
    if expenses == 0: 
        print("No expenses")
    elif expenses < 0:
        print("Invalid expense")
    else: 
        expenses_list.append(expenses)
        expenses = float(input("Enter an expense or enter 0 to finish:"))

#if its a small expense, it will be less than $25
small_expense=0
medium_expense=0
large_expense=0

for expense in expenses_list:
    if expense < 25: 
        small_expense += 1
       
    elif expense >=25 and expense <= 100:
        medium_expense+=1
        
    elif expense >100:
        large_expense+=1
        

total=sum(expenses_list)
average=total/len(expenses_list)
smallest=min(expenses_list)
largest=max(expenses_list)

print(f"total expenses: ${total:.2f}")
print(f"average expenses: ${average:.2f}") 
print(f"smallest expense: ${smallest:.2f}")
print(f"largest expense: ${largest:.2f}") 

print(f"number of small expense: {small_expense}") 
print(f"number of large expense:{large_expense}")
print(f"number of medium expense:{medium_expense}") 
print(f"number of expenses entered: {len(expenses_list)}")