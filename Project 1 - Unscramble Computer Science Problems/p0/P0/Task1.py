from os import times


%%time
"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

List_Numbers = set()

def count_numbers(numbers):
    for num in numbers:
        List_Numbers.add(num[0])
        List_Numbers.add(num[1])

count_numbers(texts)
count_numbers(calls)

print ("There are", len(List_Numbers), "different telephone numbers in the records")
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
