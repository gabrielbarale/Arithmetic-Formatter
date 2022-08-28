def arithmetic_arranger(problems, solution = False):
  
  line1 = line2 = line3 = line4 = ""
  
  #Checking for Errors
  if len(problems) > 5:
    return "Error: Too many problems."
  for problem in problems:
    top_number = problem.split()[0]
    operator = problem.split()[1]
    bottom_number = problem.split()[2]
    if top_number.isnumeric() == False or bottom_number.isnumeric() == False:
      return "Error: Numbers must only contain digits."
    if operator != "+" and operator != "-":
        return "Error: Operator must be '+' or '-'."
    if len(top_number) > 4 or len(bottom_number) > 4:
      return "Error: Numbers cannot be more than four digits."

  #Iterating through the problems
  for problem in problems:
    
    #Splitting the problem into numbers and operator 
    top_number = problem.split()[0]
    operator = problem.split()[1]
    bottom_number = problem.split()[2]
    
    #Calculating the result
    if operator == "+":
      answer = int(top_number) + int(bottom_number)
    if operator == "-":
      answer = int(top_number) - int(bottom_number)
      
    #Giving the requested format
    width = max(len(top_number), len(bottom_number))
    line1 += top_number.rjust(width + 2) + "    "
    line2 += operator + " " + bottom_number.rjust(width) + "    "
    line3 += '-' * (width + 2) + "    "
    line4 += str(answer).rjust(width + 2) + "    "
    
    #Checking if answers should be displayed
    if solution == True:
      result = line1.rstrip()+"\n"+line2.rstrip()+"\n"+line3.rstrip()+"\n"+line4.rstrip()
    else:
      result = line1.rstrip()+"\n"+line2.rstrip()+"\n"+line3.rstrip()


  return result