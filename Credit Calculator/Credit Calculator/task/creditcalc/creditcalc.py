import math
import argparse


def annuity_payment(self, principal, n, i):
	self.i = i / (100 * 12)
	payment = round(principal * (self.i * math.pow(1 + self.i, n) / (math.pow(1 + self.i, n) - 1)), 2)
	overpayment = math.ceil(payment) * n - principal
	print(f'Your annuity payment = {math.ceil(payment)}!')
	print(f'Overpayment = {math.floor(overpayment)}')
	return math.ceil(payment)


def credit_principal(self, a, period, i):
	self.i = i / (100 * 12)
	complex_value = (self.i * math.pow(1 + self.i, period)) / (math.pow(1 + self.i, period) - 1)
	principal = a / complex_value
	overpayment = {abs(a * period - principal)}
	print(f'Your credit principal = {math.floor(principal)}!')
	print(f'Overpayment = {overpayment}')
	
	return math.floor(principal)


def diff(self, p, n, i):
	self.i = float(i / (100 * 12))
	overpayment = 0
	for m in range(1, int(n) + 1):
		d = math.ceil(p / n + self.i * (p - p * (m - 1) / n))
		print(f'Month {m}: paid out {d}')
		overpayment += d
	
	print(f'Overpayment = {int(overpayment - p)}')


def count(self, p, a, i):
	self.i = float(i / (100 * 12))
	n = math.ceil(math.log(a / (a - (self.i * p)), 1 + self.i))
	month = n % 12
	year = n // 12
	if month > 0 and year > 0:
		print(f'You need {year} years and {month} months to repay this credit!')
	elif month == 0:
		print(f'You need {year} years to repay this credit!')
	else:
		print(f'You need {month} months to repay this credit!')
	
	overpayment = math.ceil(a) * n - p
	print(f'Overpayment = {math.floor(overpayment)}')
	return n


parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str, choices=['annuity', 'diff'], required=True)
parser.add_argument('--payment', type=int)
parser.add_argument('--principal', type=int)
parser.add_argument('--self.i', type=float)
parser.add_argument('--periods', type=int)
args = parser.parse_args()

if not args.payment and args.type == 'diff':
	diff(args.principal, args.periods, args.self.i)
elif args.type == 'annuity':
	if not args.principal:
		credit_principal(args.payment, args.periods, args.self.i)
	elif not args.periods:
		count(args.principal, args.payment, args.self.i)
	elif not args.payment:
		annuity_payment(args.principal, args.periods, args.self.i)
else:
	print('Incorrect parameters.')
