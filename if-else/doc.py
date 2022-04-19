costprice= int(input('enter any number'))
if costprice>100000:
	print('tax =15%')
elif costprice>50000 and 100000:
	print('tax=10%')
elif costprice<=50000:
	print('tax=5%')
else:
	print('nothing')


A=input('enter any number')
B=input('enter any number')
C=input('enter any number')
D=input('enter any number')
if A>B and C>D:
	print('A is greater than B,C and D')
elif C>D>B>A:
	print('C is greater than D,A and E')
elif D>B>C>A:
	print('D is greater than A,B and C')
elif B>C>A>D:
	print('B is greater A,C and D')
else:
	print('Nothing')


ex_date=int(input('enter a ex date'))
ex_month=int(input('enter a ex month'))
ex_year=int(input('enter a ex year'))
re_date=int(input('enter a re date'))
re_month=int(input('enter a re month'))
re_year=int(input('enter a re year'))
if ex_date>=re_date:
	if ex_month<=re_month:
		if ex_year==re_year:
			print('no charge')
else:
	if ex_date<=re_date:
		if ex_month<=re_month:
			if ex_year<=re_year:
				day=re_date-ex_date
				charge=day*5
				month=re_month-ex_month
				char=month*500
				year=re_year-ex_year
				cha=year*1000
				print('Charge:',charge, 'no of day:',day)
				print('Charge:',char,'no of month:',month)
				print('Charge:',cha,'no of year:',year)


monument=input('enter any monument')
if monument=='Red fort':
	print('Delhi')
elif monument=='Taj Mahal':
	print('Agra')
elif monument=='Jai Mahal':
	print('Jaipur')
else:
	print('Nothing')


number=int(input('enter any number'))
if number>100 and number<999:
	print('three digit number')
else:
	print('nothing')


a=int(input('enter any number'))
b=int(input('enter any number'))
c= input('enter')
if c=='+':
	print(a+b,(type(c)))
else:
	print('nothing')


Female= int(input('enter any age'))
Male= int(input('enter any age'))
if Female>=18 and Female<30:
	print('750')
if Male>=18 and Female<30:
	print('700')
if Female>=30 and Female<=40:
	print('850')
if Male>=30 and Male<=40:
	print('800')
else:
	print('Nothing')
 

a= int(input('enter'))
b=int(input('enter'))
c=str(input('enter'))
if c=='+':
	print(a+b)
elif c=='-':
	print(a-b)
elif c=='*':
	print(a*b)
elif c=='/':
	print(a/b)
elif c=='%':
	print(a%b)
elif c=='^':
	print(a^b)
else:
	print('nothing')


days= int(input('enter any number'))
if days<5:
	print(days*2)
elif 5<10:
	print(days*3)
elif 10<15:
	print(days*4)
elif days<15:
	print(days*5)
else:
	print('nothing')
 
'''days= int(input('enter any number'))
if days<5:
	charges=days*2
	print ('charges')
else:
	if days>10 and days<10:
		charges=days*3
		print('charges')
	else:
		if days<15 and days>10:
		 	charges=days*4
		    print('charges')
		else:
		 	if days>15:
		 		charges=days*5
		 		print('charges')
		 	else:
		 		print('nothing')'''

quantity=int(input('enter any quantity'))
cost=input('quantity*100')
if quantity>1000:
	discount=('10/100* cost')
	total=(cost)
	print('total:',total)
else:
	print('nothing')
 

  
year= int (input('enter any year'))
if year% 4==0:
	print('leap year')
else:
	if year%400==0:
		print('it is leap year')
	else:
		print('not leap year')

months=input('enter any months')
if months in 'April,june,september,november':
	print('30 days')
elif months in 'January,March,May,july,August,October,December':
	print('31days')
elif months== 'February':
	print('28 or 29 days')
else:
	print('nothing')
 
unit= int(input('enter any unit'))
if unit < 100:
	print('no charge')
elif unit < 200:
	print('5 per unit')
elif unit >200:
	print('10 per unit')
else:
	print('nothing')
 
'''unit =int(input('enter'))
if unit<=100:
	print('no charge')
else:
	if unit>=100 and unit<=200:
		bill=unit*5
		print('bill per unit:',bill)
	else:
		if unit>=200 and unit<350:
		    bill=unit*10
		    print('bill per unit:',bill)
		else:
		    if unit==350:
		    	bill=2000
		    	print('total bill:',bill)
		    else:
		    	print('nothing')'''

number=int(input('enter any number'))
if number%10==0:
	print('last number,num%10')
elif number//10:
	print(' first number, num%5')
else:
	print('nothing')


n=int(input(""))
if n%2!=0:
    print("Weird")
else:
    if n>2 and n<5:
        print("Not Weird")
    elif n>6 and n<=20:
        print("Weird")
    elif n>20:
        print("Not Weird")