"""3) შექმენით პროგრამა სადაც 0 დან 50 ის ჩათვლით ყველა
 5 ის ჯერად რიცხვებს შეკრიბავთ (5ზე რომელი რიცხვებიც იყოფა) გამოიყენეთ for ციკლიც და while ციკლიც"""


sum=0
for i in range(51):
    if i % 5 == 0:
     sum+=i
print(sum)
  

while i < 51:
  if i % 5 == 0:
    sum += i
    i += 1 


#1
for i in range(5, 40, 10):
  print(i) 

#2
for i in range(2, 6):
  print(i) 



#3
fruits = ["apple", "banana", "cherry"]
for i in fruits:
  print(i) 


#4
for x in "banana":
  print(x) 



#5
for x in range(6):
  print(x) 



#1
i = 1
while i < 10:
  print(i)
  i += 1



#2
i = 1
while i < 6:
  print(i)
  i += 1



#3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

  
