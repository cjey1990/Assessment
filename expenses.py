import csv
import sys
 
# For exiting the program gracefully
 
def read_Expenses_data(filename):
   """
   Reads Expenses data from a CSV file.
  
   Args:
   filename (str): The name of the CSV file containing the Expenses data.
 
   Returns:
   list: A list of dictionaries containing Expenses data (Expense, and Months).
   """
   data = []
 
   try:
       # Open the CSV file for reading
       with open(filename, 'r', encoding='utf-8') as file:
           csv_reader = csv.reader(file)
           header = next(csv_reader)  # Read the header (first row)
 
           # Iterate over each row in the CSV file
           for row in csv_reader:
               # Skip rows that don't have enough data
               if len(row) < 4:
                   print(f"Incomplete data in row: {row}")
                   continue
               try:
                   # Ensure the scores are integers and handle any non-integer input
                   data.append({
                       'Expenses': row[0],
                       'January': int(row[1]),
                       'Febraury': int(row[2]),
                       'March': int(row[3]),
                       'April': int(row[4]),
                       'May': int(row[5]),
                       'June': int(row[6]),
                       'July': int(row[7]),
                       'August': int(row[8]),
                       'September': int(row[9]),
                       'October': int(row[10]),
                       'November': int(row[11]),
                       'December': int(row[12])
                   })
               except ValueError as e:
                   # Handle case where the Expenses
                   # 'scoreis not an integer
                   print(f"Invalid data in row {row}: {e}")
                   print("Only integer scores are allowed. Goodbye!")
                   sys.exit(1)  # Exit the program with status 1 (error)
 
   except FileNotFoundError:
       # Handle case when the file is not found
       print(f"Error: {filename} not found.")
       print("Goodbye!")
       sys.exit(1)  # Exit the program with status 1 (error)
   except Exception as e:
       # Handle any unexpected errors
       print(f"An unexpected error occurred: {e}")
       print("Goodbye!")
       sys.exit(1)  # Exit the program with status 1 (error)
 
   return data
#Utils and error checking
 
def calculate_average(Expenses):
   """
   Calculates the average Expenses
   'Expensesfor a Expenses.
  
   Args:
   Expenses (dict): The dictionary containing Expenses data (Expenses and months).
 
   Returns:
   float: The average Expenses
   'Expensesfor the Expenses, or None if data is missing.
   """
   try:
       # Calculate the total Expenses
       # 'expensesby summing up individual Expenses 
       total = Expenses['January'] +Expenses['Febraury'] + Expenses['March'] + Expenses['April'] + Expenses['May'] + Expenses['June'] + Expenses['July'] + Expenses['August'] + Expenses['September'] + Expenses['October'] + Expenses['November'] + Expenses['December']
       # Calculate the average by dividing total by the number of Expenses (3)
       average = total / (len(Expenses)-1)
       return average
   except KeyError as e:
       # Handle case if some data (e.g., expenses) is missing for the Expenses
       print(f"Missing data for {e}")
       return None
 
def assign(Expenses):
   """
   Assigns overspend and within limit to income based on a Expenses's
  
   Args:
   Expenses
   'Expenses(float): The Expenses
   'scoreof the Expenses.
 
   """
   # Determine the grade based on Expenses
   if Expenses >= 2000:
       return "Over Spent"
   else:
       return "Within Limit"
 
def calculate_min_max_range(Montly_expenses):
   """
   Calculates the minimum, maximum, and range for a given list of Expenses .
  
   Args:
   Montly_expenses (list): A list of Expenses all months.
 
   Returns:
   tuple: A tuple containing the minimum Expenses
    maximum Expenses and range (max - min).
   """
   min_score = min(Montly_expenses)
   max_score = max(Montly_expenses)
   return min_score, max_score
 
def process_Expenses_results(Expensess_data):
   """
   Processes Expenses data, calculates averages, and additional statistics, and returns the results.
 
   Args:
   Expensess_data (list): A list of dictionaries containing Expenses data.
 
   Returns:
   list: A list of dictionaries containing Expenses results.
   """
   results = []
 
   for Expenses in Expensess_data:
       # Get the expenses for all months
       Montly_expenses = [Expenses['January'], Expenses['Febraury'], Expenses['March'], Expenses['April'], Expenses['May'], Expenses['June'], Expenses['July'], Expenses['August'], Expenses['September'], Expenses['October'], Expenses['November'], Expenses['December']]
      
      
      
      
       # Calculate the average Expenses
       # 'Expensesfor the Expenses
       average = calculate_average(Expenses)
       if average is not None:
        Expense_limit = assign(average)
          
           # Calculate the minimum, maximum, and range of Expenses
        min_score, max_score = calculate_min_max_range(Montly_expenses)
          
          
           # Create a dictionary with the Expenses's data and calculated results
        Expenses_results = {
               'Expenses': Expenses['Expenses'],
               'January': Expenses['January'],
               'Febraury': Expenses['Febraury'],
               'March': Expenses['March'],
               'April': Expenses['April'],
               'May': Expenses['May'],
               'June': Expenses['June'],
               'July': Expenses['July'],
               'August': Expenses['August'],
               'September': Expenses['September'],
               'October': Expenses['October'],
               'November': Expenses['November'],
               'December': Expenses['December'],
               'average': average,
               'Expenses_limit': Expense_limit
               }
        results.append(Expenses_results)
  
   return results
 
def write_results_to_csv(results, filename):
   """
   Writes the processed Expenses results to a new CSV file.
 
   Args:
   results (list): A list of dictionaries containing Expenses results.
   filename (str): The name of the CSV file to save the results.
   """
   if results:
       # Define the header for the CSV file
       header = ['Expenses', 'January', 'Febraury', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'average', 'Expenses_limit']
      
       # Open the CSV file for writing
       with open(filename, 'w', newline='', encoding='utf-8') as file:
           writer = csv.DictWriter(file, fieldnames=header)
           writer.writeheader()  # Write the header row
           writer.writerows(results)  # Write the Expenses results
 
       print(f"Results written to {filename}")
   else:
       print("No results to write.")
 
if __name__ == "__main__":
   # The name of the input CSV file containing Expenses data
   filename = "Expenses.csv"  # Replace with your actual CSV file name
   Expensess_data = read_Expenses_data(filename)
 
   if Expensess_data:
       # Process the Expenses data to calculate averages and Expenses_limit
       results = process_Expenses_results(Expensess_data)
       # Write the processed results to a new CSV file
       write_results_to_csv(results, 'Expenses_results.csv')
  
   print("Goodbye!")  # Exit message before ending the program
 
