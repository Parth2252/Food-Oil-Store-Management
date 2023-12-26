# from odoo import models, fields




# class ResPartner(models.Model):
#     _inherit = 'res.partner'

#     work_email_store = fields.Char(copy=False)


#     *
#    * *
#   * * *
#  * * * *
# * * * * * 
  

# a = int(input("enter row of tringale: "))
# for i in range(a*2+1,a,-1):
#     # for j in range(i+1):
   
#     print(" " * (i-(a+1)), end=" ")
#     print("* " * ((a*2+2)-i), end=" ")
#     print(" " * (i-(a+1)), end=" ")

#     print( )


# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern triangle
def triangle(n):
	
	# number of spaces
	k = n - 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# inner loop to handle number spaces
		# values changing acc. to requirement
		for j in range(0, k):
			print(end=" ")
	
		# decrementing k after each loop
		k = k - 1
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("* ", end="")
	
		# ending line after each row
		print("\r")

# Driver Code
n = 35
triangle(n)
