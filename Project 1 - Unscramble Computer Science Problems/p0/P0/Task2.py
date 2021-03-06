%%time
"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

numbers = {}

for call in calls:
    numbers[call[0]] = numbers.get(call[0], 0) + int(call[-1])
    numbers[call[1]] = numbers.get(call[1], 0) + int(call[-1])
    
Number = max(numbers, key=numbers.get)

print (f"{Number} spent the longest time, {numbers[Number]} seconds, on the phone during September 2016")




