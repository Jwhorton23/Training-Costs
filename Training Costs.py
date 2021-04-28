#Print menu
print ('\t\t\tMENU WORKSHOP SELECTOR')
print ('\tWORKSHOPS \tRegistration Fee \tDays')
print ('1) Handling Stress \t$1000 \t\t\t3 ')
print ('2) Time Management\t$800 \t\t\t3 ')
print ('3) Supervision Skills\t$1600 \t\t\t3 ')
print ('4) How to Interview \t$500 \t\t\t1\n')

print ('\tLOCATION \tLodging Fee per Day')
print ('1) Austin \t\t$150')
print ('2) Chicago\t\t$225 ')
print ('3) Phoenix\t\t$175 ')
print ('4) Orlando\t\t$300 ')


# Named constants for workshop selection
workshop1 = 1000
workshop2 = 800
workshop3 = 1600
workshop4 = 500

# Named constants for location selection
location1 = 150
location2 = 225
location3 = 175
location4 = 300


# Obtain user training selection
selected_training = int(input('Enter number associated with the workshop training of your choice: '))


# Obtain user location selection
selected_location = int(input('Enter the number associated with the location of your choice: '))


# Assign workshop number to user input number 
if selected_training == 1:
    selected_training = workshop1
    number_days = 3

elif selected_training == 2:
    selected_training = workshop2   
    number_days = 3

elif selected_training == 3:
    selected_training = workshop3
    number_days = 3

elif selected_training == 4:
    selected_training = workshop4 
    number_days = 1
else:
    print('Invalid selection')  


# Assign location number to user input number
if selected_location == 1:
    selected_location = location1

elif selected_location == 2: 
    selected_location = location2 

elif selected_location == 3:
    selected_location = location3 

elif selected_location == 4: 
    selected_location = location4 

else:
    print('Invalid selection')   


# Display registration fee 
Registration_fee = selected_training
print('Your registration fee is' , Registration_fee)
      
# display the lodging fee
lodging_fee = selected_location * number_days
print('Your lodging fee is' , lodging_fee)   

# Display the total cost
total = Registration_fee + lodging_fee
print('Your total cost is ' , total)




