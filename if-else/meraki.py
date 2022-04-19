#1st
day = input("Din enter karo\n")
if day == "monday": 
  print("Rajma Chawal")
elif day == "tuesday": 
  print("Pao Bhaji")
elif day == "wednesday": 
  print("Chole Bhature")
elif day == "thursday":
  print("Dosa")
elif day == "friday": 
  print("Litti Chokha")
elif day == "saturday": 
  print("Thukpa")
else:
  print("Poha")

#2nd
value = "delhi"
guess = input("Sheher ka naam guess karo> ")
if guess != value:
  print("Aapka guess galat hai")
else:
  print("Aapka guess sahi hai")

#3rd
speed = input("Gaadi ki kya speed thi?")
speed = int(speed)
if speed <= 60:
  print("Gaadi speed limit ke andar thi.")
else:
  print("Gaadi speed limit ke bahar thi.")

#4th
day = input("Din enter karo> ")
meal = input("Meal enter karo, jaise breakfast lunch aur dinner mein se ek> ")
if day == "monday":
  if meal == "breafast":
    print("Poha")
  elif meal == "lunch":
    print("Rajma Chawal")
  else:
    print("Roti Sabzi")
elif day == "tuesday":
  if meal == "breakfast":
    print("Poori Sabzi")
  elif meal == "lunch":
    print("Thukpa")
  elif meal=="dinner":
    print("Chicken Chawal")
  else:
    print("Aur kisi bhi din hum daal roti sabzi khaynege.")
else:
  print("aloo paratha")

#5th
number=44*30
number1=int(input("enter"))
if number<number1:
  print("greater")
else:
  print("not greater")
  
#6th
varx=56
value=int(input("enter"))
if value==varx:
  print('equal')
else:
  print("not equal")

#8th
varx=int(input("enter number"))
if varx%2==0:
  print("divisible")
else:
  print("not divisible")

#9th
number=int(input ("enter the numbers"))
if number<10:
  print("less than 10")
elif number>10 and number<10:
  print("less than 20")
else:
  print("greater than 20")
  
#10th
varx=int(input("enter the number="))
vary=int(input("enter the number="))
if varx%vary==0:
  print("divisible")
else:
  print("not divisible")

#13th
age=int(input("enter the age=="))
if age>5:
  print("can go to school")
if age>18:
  print("eligible for  vote")
if age>21:
  print("eligible for driving a car")
if age>24:
  print("eligible for marriage")
if  age>25:
  print("elligible for drinking")

#15th
price_milk =int( input("1L milk ka price daalo?"))
print("10L milk",price_milk*10,"rupees ka aata hai.")

#16th
number = int(input("please enter a  number"))
print("your number divided by 2 is equal to = ",number%2==0)

#18th
speed = int(input("Gaadi ki speed daalo > "))
if speed < 60:
  print("Speed kam hai")
elif speed < 30:
  print("Speed bahot kam hai")
elif speed > 100:
  print("Speed bahot fast hai")

#19th
day = input("Aaj ka din kya hai? (monday/tuesday) > ")
time = input("Kaunse samay ka khana banana hai? (lunch/dinner) > ")
if day == "monday" and time=="lunch":
  print("Daal-Roti banegi aaj")
elif day == "monday" and time=="dinner":
  print("Daal-Roti banegi aaj")
elif day=="tuesday"and time=="lunch":
   print("Daal-Roti banegi aaj")
else:
  print("Pav-Bhaji banegi aaj toh :")

