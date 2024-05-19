"""
შექმენით ალგორითმი, რომელიც მომხმარებელს შეეკითხება
 ტემპერატურას ცელსიუსში და გადაიყვანს ფარენჰეიტში. ((variable * 1.8) + 32)

"""

celsius = int(input("please enter a number of celsius: "))
farenhait=((celsius * 1.8) + 32)

print(farenhait)

"""

მომხმარებელს შეეკითხეთ ასაკი და მოახდინეთ შედარება ისე,
რომ ასაკი ნაკლები იყოს ოცზე და მეტი იყოს თორმეტზე.

"""
user_input = int(input("how old are you?: "))
print(user_input<20 and user_input>12)

"""
მომხმარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ
 არის თუ არა ის 100-ზე მეტი და 9-ის ჯერადი (9-ზე სრულად იყოფა).

"""
num1 = int(input("please enter your number: "))
print(num1 <= 100 and num1/9)

"""

მომხმარებელს შემოატანინეთ მართკუთხედის
 c(retangle) გვერდები (გაითვალისწინეთ, რომ შესაძლოა რიცხვი ათწილადიც იყოს) და დაუბეჭდეთ მისი ფართობი.

"""
num5 = int(input("A-please enter the length of the rectangle: " ) )
num6 = int(input("B-please enter the width of the rectangle " ) )
print(num5 * num6 )

"""
ივარჯიშეთ And და Or ოპერატორებზე და თქვენით ჩამოწერეთ ყველა შესაძლო ვარიანტი მათზე მუშაობისას.

"""

#or
print(False or False)
print(True or True)
print(True or False)
print(False or True )
#and
print(False and False)
print(True and False)
print(False and True)
print(True and True)










