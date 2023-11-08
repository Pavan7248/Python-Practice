questions = [
  [
    "What is the capital of India?", "New Delhi", "Mumbai", "Kolkata", "Chennai", 1
  ],
  [
  "The language of Lakshadweep. a Union Territory of India, is", "English", "Hindi", "Marathi", "Telugu", 2
  ],
  [
  "Bahubali festival is related to", "Islam", "Hinduism", "Muslim", "Jainism", 4
  ],
  [
  "Which day is observed as the World Standards  Day?", "July 2", "June 23", "May 4", "Oct 14", 4
  ],
  [
  "Which of the following was the theme of the World Red Cross and Red Crescent Day?", "Dignity for all - focus on women", 
   "Dignity for all - focus on children", "Focus on health for all", "Nourishment for all-focus on children"
  ],
  [
  "Which of the following is not a festival of India?", "Diwali", "Holi", "Eid", "Christmas", 4
  ],
  [
  "What is the capital of UttarPtradesh", "Lucknow", "Kolkata", "Ahmedabad", "Gandhinagar", 1 
  ],
  [
  "What is the capital of Bihar?", "Patna", "Patiala", "Agra", "Ajmer", 1
  ],
]

levels = [1000,2000,3000,4500,10000,15000,25000,70000,90000,100000]
money = 0
for i in range(0, len(questions)):
  question = questions[i]
  print(f"\n\n{i+1}. {question[0]}")
  print("1.", question[1],   "2.", question[2]) 
  print("3.", question[3],   "4.", question[4])
  answer = int(input("Enter your answer between 1-4: "))
  if answer == question[5]:
    print("Correct Answer!")
    print(f"You have earned Rs. {levels[i]} money")
    if(i == 4):
      money = 1000
    elif(i == 7):
      money = 70000
  
  else:
    print("Wrong Answer!")
    breakpoint

print(f"You have earned Rs. {money} money")
    
    
    
    