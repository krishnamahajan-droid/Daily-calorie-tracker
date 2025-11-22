# tracker.py                                       
#****************************************************************************#
#Task 1: Input and Data collection
# Author: Krishna Mahajan 
# Date  : 2025-10-25
# Project: Daily calorie tracker - Python mini project 
#****************************************************************************#
# Description: 
#A simple command-line tool that collects meals and calories,
# calculates total and average, compares against a daily limit,
# and optionally saves a session report.
#****************************************************************************#

#Task 2: Input and Data Collection 
print("   Welcome to the daily calorie tracker!   ")
print("This tool records your daily meals and calories...")

#Asking the user how many meals he/she will intake today...
num_meals = int(input("How many meals do you want to enter today? "))

# Create empty lists to store meal names and calories
meal_names = []
calorie_amounts = []

# Loop to get data
for i in range(num_meals):
    meal = input(f"Enter the name of meal {i+1}: ")
    calories = float(input(f"Enter calories for {meal}: "))

    # Add the values to the lists
    meal_names.append(meal)
    calorie_amounts.append(calories)

# Print the lists to check
print("Meals entered:", meal_names)
print("Calories entered:", calorie_amounts)

# --- Step 3: Calorie Calculations ---
print("\nNow let's calculate your calorie summary!")

# Calculate total calories using sum()
total_calories = sum(calorie_amounts)

# Calculate average calories
average_calories = total_calories / num_meals

# Ask for the user's daily calorie limit
daily_limit = float(input("Enter your daily calorie limit: "))
print("********************************************************************************")

# Compare total with limit
print(" Calorie Summary ")
print("********************************************************************************")
print("Total calories consumed:", total_calories)
print("Average calories per meal:", average_calories)
print("********************************************************************************")

# *** Step 4: Exceed Limit Warning System ***
if total_calories > daily_limit:
    message = "⚠️  WARNING: You have exceeded your daily calorie limit!"
    print(message)
    print("Try to balance your meals or exercise more tomorrow.")

elif total_calories == daily_limit:
    message = "⚖️  You have reached exactly your daily calorie limit."
    print(message)
    print("Maintain this balance for a healthy routine.")

else:
    message = "✅ Great job! You are within your daily calorie limit."
    print(message)
    print("Keep it up and continue your healthy eating habits!")

# *** Step 5: Neatly Formatted Summary Table ***
print("\n===================================")
print("        DAILY CALORIE REPORT       ")
print("===================================")
print("Meal Name\tCalories")
print("-----------------------------------")

for i in range(num_meals):
    print(f"{meal_names[i]}\t{calorie_amounts[i]}")

print("-----------------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories:.2f}")
print("-----------------------------------")
print(message)
print("===================================")

# *** Task 6: Save Report to a text file ***
save_choice = input("\nDo you want to save this report? (yes/no): ")

if save_choice.lower() == "yes":
    # Open a file to write the summary (UTF-8 supports emojis)
    with open("calorie_report.txt", "w", encoding="utf-8") as file:
        file.write("=== DAILY CALORIE REPORT ===\n")
        for i in range(num_meals):
            file.write(f"{meal_names[i]}\t{calorie_amounts[i]}\n")
        file.write("-----------------------------------\n")
        file.write(f"Total: {total_calories}\n")
        file.write(f"Average: {average_calories:.2f}\n")
        file.write(f"Status: {message}\n")
        file.write("===================================\n")

    print("✅ Report saved successfully as 'calorie_report.txt'!")
else:
    print("❌ Report not saved.")
    print("\nThank you for using the Daily Calorie Tracker! Stay healthy 😊")

