# """ 


# 1. მომხმარებელს შეეკითხეთ თუ რომელ პროგრამირების აკადემიაში სწავლობს. თუ პასუხი იქნება "GOA", დაუბეჭდეთ რომ სწორია.
#  სხვა შემთხვევაში დაუბეჭდეთ, რომ არასწორი გადაწყვეტილება მიიღო.

# """

# user_input=input("რომელ პროგრამირების აკადემიაში სწავლობ?" )
# if user_input=="GOA":
#   print("სწორი არჩევანი მიიღე")
 
# else:
#   print("არასწორი არჩევანი მიგიღია")



# """
# მომხმარებელს შემოატანინეთ საყიდელი ნივთის ფასი და მისი ბიუჯეტი. თუ ბიუჯეტი აღემატება ან ტოლია საყიდელი ნივთის ფასის,
# დაუბეჭდეთ რომ თანხა ყოფნის. სხვა შემთხვევაში, დაუბეჭდეთ თუ რამდენი აკლდება საყიდლად.

# """


# price=int(input("საყიდელი ნივთის ფასი: "))
# budget=int(input("ბიუჯეტი"))

# if budget>=price:
#  print("თანხა გყოფნნით")
 
# else:
#  print("თქვენ გაკლდებათ "+ str(price - budget) +"ლარი")









# """"

# დაწერეთ პროგრამა, რომელიც შეამოწმებს მომხმარებლის
#  მიერ შემოტანილ რიცხვს. თუ რიცხვი მეტია ან ტოლი 
#  ხუთის, დაბეჭდეთ მისი ნამრავლი ორზე. სხვა შემთხვევაში დაბეჭდეთ მისი ნამრავლი ოთხზე.

# """

# num1=int(input("please enter your number: "))

# if num1>=5:
#  print(num1*2)
# else:
#  print(num1*4)




# """"

# თქვენს პროგრამაში ბილეთის ფასი იქნება
#  10 ლარი. მომხმარებელს შეეკითხეთ თუ 
#  რამდენი ბილეთის ყიდვა უნდა. თუ ეს რიცხვი ნაკლები
#    იქნება 5-ზე, გამოუტანეთ ჩვეულებრივი შედეგი. სხვა შემთხვევაში ყოველ ბილეთზე გააკეთეთ 30%-იანი ფასდაკლება.

# """

# tickets_price=10 
# user_tickets=int(input("რამდენი ბილეთის ყიდვა გინდა: "))
# total_price=user_tickets*tickets_price
# if user_tickets<5:
#  print(total_price)
# else:
#  print(total_price*0.7)




"""
შექმენით კალკულატორის პროგრამა, სადაც გექნებათ +, -, *, /. მომხმარებელს 
ჯერ შეეკითხეთ ორი რიცხვი, შემდეგ სასურველი ოპერაცია და ბოლოს დაუბეჭდეთ შედეგი.

"""


num5=int(input("please enter your number: "))
num6=int(input("please enter your number: "))


num7=input("desired operation")
if num7=="+":
 print(num5+num6)
elif num7=="-":
 print(num5-num6)
elif num7=="*":
 print(num5*num6)
elif num7=="/":
 print(num5/num6)
 