# Miles to kilometers converter
# kilometers = miles * 1.60934
# enter miles 5
# 5 miles = 8.04 kilometers

# User enters number in miles
miles = input('Enter miles: ')

# String to integer converter
miles = int(miles)

# Calculate by multiplying 1.60934 times miles
kilometers = miles * 1.60934

# Finally display info to user
print("{} miles equals {} kilometers".format(miles, kilometers))