# Display a multiplication table.

number = int(input ("Enter the number of which you want to see the multiplication table: "))       

# We are using "for loop" to iterate the multiplication 10 times.       
print ("The multiplication table of: {number}")    
for count in range(1, 11):      
   print (number, 'x', count, '=', number * count)  
   
