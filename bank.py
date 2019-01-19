class Account:

	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance

	def __str__(self):
		return 'Account owner: {} \nAccount balance: {}'.format(self.owner, self.balance)

	def deposit(self, amount):
		self.amount = amount
		self.balance = self.balance + amount
		print('Deposit Accepted')

	def withdraw(self, amount):
		self.amount = amount 
		if self.balance - amount < 0:
			print('Funds Unavailible!')
		else:
			self.balance = self.balance - amount
			print('Withdraw Accepted') 

			
	 

										










