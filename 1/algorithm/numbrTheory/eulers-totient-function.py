# Python program to compute
# Totient function for
# all numbers smaller than
# or equal to n.

# Computes and prints
# totient of all numbers
# smaller than or equal to n.
def computeTotient(n):

	# Create and initialize
	# an array to store
	# phi or totient values
	phi=[]
	for i in range(n + 2):
		phi.append(0)

	for i in range(1, n+1):

		phi[i] = i # indicates not evaluated yet
					# and initializes for product
					# formula.

	# Compute other Phi values
	for p in range(2,n+1):
	
		# If phi[p] is not computed already,
		# then number p is prime
		if (phi[p] == p):
		
			# Phi of a prime number p is
			# always equal to p-1.
			phi[p] = p-1

			# Update phi values of all
			# multiples of p
			for i in range(2*p,n+1,p):
			
				# Add contribution of p to its
				# multiple i by multiplying with
				# (1 - 1/p)
				phi[i] = (phi[i]//p) * (p-1)
	

	# Print precomputed phi values
	for i in range(1,n+1):
		print("Totient of ", i ," is ",
		phi[i])

# Driver code

n = 5
computeTotient(n)

# This code is contributed
# by Anant Agarwal
