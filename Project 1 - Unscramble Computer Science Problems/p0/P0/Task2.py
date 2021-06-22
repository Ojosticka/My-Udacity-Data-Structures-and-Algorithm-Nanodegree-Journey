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

num_time = {}

for call_log in calls:
    if call_log[0] in num_time:
        num_time[call_log[0]] += int(call_log[-1])
    else:
        num_time[call_log[0]] = int(call_log[-1])
        
    if call_log[1] in num_time:
        num_time[call_log[1]] += int(call_log[-1])
    else:
        num_time[call_log[1]] = int(call_log[-1])
        
Number = max(num_time, key=num_time.get)

print (f"{Number} spent the longest time, {num_time[Number]} seconds, on the phone during September 2016.")

"""TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
