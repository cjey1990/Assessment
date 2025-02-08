import csv
import sys
 
# For exiting the program gracefully
 
def read_Expenses_data(filename):
   """
   Reads Expenses data from a CSV file.
  
   Args:
   filename (str): The name of the CSV file containing the Expenses data.
 
   Returns:
   list: A list of dictionaries containing Expenses data (name, math, science, english scores).
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
                   # Handle case where the score
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
   Calculates the average score
   'scorefor a Expenses.
  
   Args:
   Expenses (dict): The dictionary containing Expenses data (name, scores for math, science, english).
 
   Returns:
   float: The average score
   'scorefor the Expenses, or None if data is missing.
   """
   try:
       # Calculate the total score
       # 'scoreby summing up individual subject scores
       total = Expenses['January'] +Expenses['Febraury'] + Expenses['March'] + Expenses['April'] + Expenses['May'] + Expenses['June'] + Expenses['July'] + Expenses['August'] + Expenses['September'] + Expenses['October'] + Expenses['November'] + Expenses['December']
       # Calculate the average by dividing total by the number of subjects (3)
       average = total / (len(Expenses)-1)
       return average
   except KeyError as e:
       # Handle case if some data (e.g., scores) is missing for the Expenses
       print(f"Missing data for {e}")
       return None
 
def assign(Expenses):
   """
   Assigns overspend and within limit to income based on a Expenses's score
  
   Args:
   score
   'score(float): The score
   'scoreof the Expenses.
 
   Returns:
   str: The letter grade (A, B, C, D, E, or F) based on the score
   'January.
   """
   # Determine the grade based on score
   if Expenses >= 2000:
       return "Over Spent"
   else:
       return "Within Limit"
 
def calculate_min_max_range(Expenses_scores):
   """
   Calculates the minimum, maximum, and range for a given list of Expenses scores.
  
   Args:
   Expenses_scores (list): A list of Expenses scores for math, science, and english.
 
   Returns:
   tuple: A tuple containing the minimum score
    maximum score and range (max - min).
   """
   min_score = min(Expenses_scores)
   max_score = max(Expenses_scores)
   return min_score, max_score
 
def process_Expenses_results(Expensess_data):
   """
   Processes Expenses data, calculates averages, grades, and additional statistics, and returns the results.
 
   Args:
   Expensess_data (list): A list of dictionaries containing Expenses data.
 
   Returns:
   list: A list of dictionaries containing Expenses results (scores, averages, grades, pass/fail).
   """
   results = []
 
   for Expenses in Expensess_data:
       # Get the scores for math, science, and english
       Expenses_scores = [Expenses['January'], Expenses['Febraury'], Expenses['March'], Expenses['April'], Expenses['May'], Expenses['June'], Expenses['July'], Expenses['August'], Expenses['September'], Expenses['October'], Expenses['November'], Expenses['December']]
      
      
      
      
       # Calculate the average score
       # 'scorefor the Expenses
       average = calculate_average(Expenses)
       if average is not None:
          
           # Calculate the minimum, maximum, and range of scores
           min_score, max_score = calculate_min_max_range(Expenses_scores)
          
          
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
       header = ['Expenses', 'January', 'Febraury', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'average', 'Expenses',]
      
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
       # Process the Expenses data to calculate averages and grades
       results = process_Expenses_results(Expensess_data)
       # Write the processed results to a new CSV file
       write_results_to_csv(results, 'Expenses_results.csv')
  
   print("Goodbye!")  # Exit message before ending the program
 
