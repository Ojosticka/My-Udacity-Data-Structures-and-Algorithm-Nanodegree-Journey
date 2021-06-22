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

List_Numbers = []
def count_numbers(numbers):
    for i in numbers:
        for num in i[:2]:
            if num not in List_Numbers:
                List_Numbers.append(num)

count_numbers(texts)
count_numbers(calls)

print ("There are", len(List_Numbers), "different telephone numbers in the records")
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
