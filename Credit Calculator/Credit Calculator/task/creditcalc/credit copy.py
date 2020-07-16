import math
import sys


def diff(p, n, i):
	i = (i / 100) / 12
	overpayment = 0
	for m in range(1, int(n) + 1):
		d = math.ceil(p / n + i * (p - p * (m - 1) / n))
		print(f'Month {m}: paid out {d}')
		overpayment += d
	
	print(f'Overpayment = {int(overpayment - p)}')


def count(p, a, i):
	i = (i / 100) / 12
	n = math.ceil(math.log(a / (a - i * p), 1 + i))
	print(n)
	month = n % 12
	year = n // 12
	if month > 0 and year > 0:
		print(f'You need {year} years and {month} months to repay this credit!')
	elif month == 0:
		print(f'You need {year} years to repay this credit!')
	else:
		print(f'You need {month} months to repay this credit!')
	
	return n


def annuity(p, n, i):
	i = (i / 100) / 12
	a = p * (i * pow((1 + i), n) / (pow(1 + i, n) - 1))
	overpayment = math.ceil(a) * n - p
	print(f'Your annuity payment = {math.ceil(a)}!')
	print(f'Overpayment = {math.floor(overpayment)}')


def p_principal(a, n, i):
	i = (i / 100) / 12
	p = a / (i * math.pow(1 + i, n) / (math.pow(1 + i, n) - 1))
	overpayment = {abs(a * n - int(p))}
	print(f'Your credit principal = {math.floor(p)}!')
	print(f'Overpayment = {overpayment}')


args = sys.argv
if len(args) != 5:
	print("Incorrect parameters.")

if len(args) == 5:
	if args[1].find("diff") != -1:
		principal = float(args[2][args[2].find('=') + 1:])
		period = int(args[3][args[3].find('=') + 1:])
		interest = float(args[4][args[4].find('=') + 1:])
		diff(principal, interest, period)
	elif args[1].find("annuity") != -1:
		if any("--payment" in arg for arg in args) is False:
			principal = float(args[2][args[2].find('=') + 1:])
			period = int(args[3][args[3].find('=') + 1:])
			interest = float(args[4][args[4].find('=') + 1:])
			if principal < 0 or period < 0 or interest < 0:
				print("Incorrect parameters")
			else:
				annuity(principal, period, interest)
		
		elif any("--principal" in arg for arg in args) is False:
			payment = int(args[2][args[2].find('=') + 1:])
			period = int(args[3][args[3].find('=') + 1:])
			interest = float(args[4][args[4].find('=') + 1:])
			if payment < 0 or period < 0 or interest < 0:
				print("Incorrect parameters")
			else:
				p_principal(payment, period, interest)
	
	elif any("periods" in arg for arg in args) is False:
		principal = float(args[2][args[2].find('=') + 1:])
		payment = float(args[3][args[3].find('=') + 1:])
		interest = float(args[4][args[4].find('=') + 1:])
		if principal < 0 or payment < 0 or interest < 0:
			print("Incorrect parameters.")
		else:
			count(payment, principal, interest)
