class PiggyBank:
	# create __init__ and add_money methods
	def __init__(self, dollars, cents):
		self.dollars = dollars
		self.cents = cents
	
	def add_money(self, deposit_dollars, deposit_cents):
		self.dollars += deposit_dollars
		if self.cents + deposit_cents > 99:
			self.dollars += (self.cents + deposit_cents) // 100
			self.cents = (self.cents + deposit_cents) % 100n
		else:
			self.cents += deposit_cents
	
		return self.dollars, self.cents
	
	def __repr__(self):
		return self.dollars, self.cents
