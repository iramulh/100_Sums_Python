def start_num(num):
  """
  Finds the first number in a consecutive sequence that adds up to the desired number. Takes the desired number.
  """

  #starting values for the sum, start, and adding numbers
  add = 1
  sum = 0
  start = 0
  
  while True:
    #records the current adding number as the starting number
    start = add
    
    while True:
      if add == num:
        return add

      #adds to the sum and increases the adding number by 1 to add consequetive numbers
      sum += add
      add += 1

      #returns the starting number when it gets to the desired number
      if sum == num:
        return start

      #resets the sum and makes the adding number 1 more from the current starting number before breaking out of the loop
      elif sum > num:
        sum = 0
        add = start + 1
        break

def num_list(num, start):
  """
  Returns the list of the numbers that will add up to the desired number. Takes the desired number and the first number to start from.
  """

  #initializes the result list
  nums = []
  
  while sum(nums) != num:
    
    #adds the starting number to the list and adds 1 to the starting number until it gets to the desired number
    nums.append(start)
    start += 1
  return nums

def output_string(list):
  """
  Returns a string showing the broken down sum or says not possible. Takes the list of numbers.
  """

  #intitializes the result list
  string = ""
  
  #says it's not possible if there's only one number in the list since there's nothing to add
  if len(list) == 1:
    return str(list[0]) + " is NOT possible."

  #prints the number and then the consequetive numbers that add up to it beside it
  else:
    string += str(sum(list)) + " = "
    for item in list:
      string += str(item)
      if item == list[-1]:
        break
      string += " + "
    return string

#uses the functions to write the broken down sum of each integer from 1-100 to sums.txt
with open("sums.txt", "w") as f:
  for integer in range(1, 101):
    f.write(str(output_string(num_list(integer, start_num(integer))))+"\n")