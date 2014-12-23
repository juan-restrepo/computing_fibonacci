class Fractions:

	def __init__(self, num, denom = 1):
		while num%2==0 and denom%2==0:
			num = num/2
			denom = denom/2
		self.num = num
		self.denom = denom

	def __add__(self, other):
		return Fractions(self.num*other.denom + self.denom*other.num, self.denom*other.denom)

	def __mul__(self, other):
		return Fractions(self.num*other.num, self.denom*other.denom)

	def __neg__(self):
		return Fractions(-self.num, self.denom)

	def __sub__(self, other):
		return self + -other

	def __eq__(self, other):
		if self.num*other.denom == self.denom*other.num:
			return True
		return False

	def __str__(self):
		if self.denom == 1:
			return "%d" % self.num
		else:
			return "%d/%d" % (self.num, self.denom)

class QuadraticNumberRing:
	# numbers in the number ring of Q(sqrt d)
	# this is, a+b*sqrt(d), a, b integers, if d is not 1 mod 4
	# or with the possibility of having half integers if it is
	#this first implementation will have d=5

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __add__(self, other):
		return QuadraticNumberRing(self.a+other.a, self.b+other.b)

	def __sub__(self, other):
		return QuadraticNumberRing(self.a - other.a, self.b - other.b)

	def __mul__(self, other):
		return QuadraticNumberRing(self.a*other.a + Fractions(5)*self.b*other.b, self.b*other.a + self.a*other.b)	

	#exp returns self raised to the n-th power
	def exp(self,n):
		if n==0:
			return QuadraticNumberRing(Fractions(1),Fractions(0))
		if n==1:
			return self
		temp = self.exp(n/2)
		if n%2==0:
			return temp*temp
		else:
			return self*temp*temp

	def __eq__(self,other):
		if self.a == other.a and self.b == other.b:
			return True
		return False

	def __str__(self):
		if self.b == Fractions(0):
			#return self.a
			#return "fix this"
			if self.a.denom == 1:
				return "%d" % self.a.num
			else:
				return "%d/%d" % (self.a.num, self.a.denom)
		elif self.a == Fractions(0):
			if self.b == Fractions(1):
				return "sqrt(5)"
			elif self.b == Fractions(-1):
				return "-sqrt(5)"
			else:
				return "%dsqrt(5)" % self.b.num
		elif self.b.num > 0:
			if self.b.denom == 1:
				if self.b == Fractions(1):
					return "%d+sqrt(5)" % (self.a.num)
				else:
					return "%d+%dsqrt(5)" % (self.a.num, self.b.num)
			else:
				if self.b == Fractions(1,2):
					return "(%d+sqrt(5))/2" % (self.a.num)
				else:
					return "(%d+%dsqrt(5))/2" % (self.a.num, self.b.num)
		else:
			if self.b.denom == 1:
				if self.b == Fractions(-1):
					return "%d-sqrt(5)" % (self.a.num)
				else:
					return "%d-%dsqrt(5)" % (self.a.num, -self.b.num)
			else:
				if self.b == -Fractions(1,2):
					return "(%d-sqrt(5))/2" % (self.a.num)
				else:
					return "(%d-%dsqrt(5))/2" % (self.a.num, -self.b.num)

#this functions gives the N-th fibonacci number
def fib(N):
	z = QuadraticNumberRing(Fractions(1,2),Fractions(1,2))
	zbar = QuadraticNumberRing(Fractions(1,2),Fractions(-1,2))
	return (z.exp(N) - zbar.exp(N)).b

		

def main(): #this is to do stuff

	#x = QuadraticNumberRing(1,2)
	#y = QuadraticNumberRing(4,5)
	#print x+y, x-y, x*y
	# z = QuadraticNumberRing(Fractions(1,2), Fractions(1,2))
	# print z, z*z
	# for i in range(10):
	# 	print z.exp(i)
	# print QuadraticNumberRing(Fractions(1),Fractions(0))
	N = input("Type a positive integer:")
	print "The %d-th fibonacci number is" % N, fib(N)


	# print Fractions(6,2)
	# print Fractions(3,2)
	# print Fractions(5,1)+Fractions(7,2)
	# print Fractions(8)
	# print Fractions(-32,4)
	# print Fractions(5,2)*Fractions(3,4)
	# print Fractions(5,2)*Fractions(7)
	# print Fractions(5,2)*Fractions(8)
	# print Fractions(5,4)*Fractions(4)
	# print Fractions(0) == Fractions(0)




if __name__ == '__main__': #don't touch this
    main()
