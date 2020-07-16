print('Enter the credit principal:')
principal = int(input('> '))
print('''What do you want to calculate?
type "m" - for count of months,
type "p" - for monthly payment''')
calculate = input('> ')
if calculate == 'p':
	print('Enter count of months:')
	months = int(input('> '))
	payment = round(principal / months)
	if payment % 2 != 0:
		payment += 1
		last_payment = principal - (months - 1) * payment
		print(f'Your monthly payment = {payment} with last month payment = {last_payment}.')
	else:
		print(f'Your monthly payment = {payment}')
elif calculate == 'm':
	print('Enter monthly payment:')
	payment = int(input('> '))
	months = round(principal / payment)
	print(f'It takes {months} month to repay the credit')
