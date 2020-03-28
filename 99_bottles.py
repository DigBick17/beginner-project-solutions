bottle=99
for n in range(99,-1,-1):
	if n>2:
		print(n,"Bottles of beer in the wall,",n,"bottles of beer.")
		print("Take one down and pass it around,",n-1,"bottles of beer in the wall\n")
	elif n>1:
		print(n,"Bottles of beer in the wall,",n,"bottles of beer.")
		print("Take one down and pass it around,",n-1,"bottle of beer in the wall\n")
	elif n==1:
		print(n,"Bottle of beer in the wall,",n,"bottle of beer.")
		print("Take one down and pass it around, no more bottles of beer in the wall\n")
	elif n==0:
		print("No more bottles of beer in the wall, no more bottles of beer.")
		print("Go to the store and buy some more,",bottle,"bottles of beer in the wall")


