transactions = [("Mike", -30), ("Tom", -20),("Jack", -30)]
people = ["Mike", "Tom", "Jack","Mary"]

from collections import defaultdict
from heapq import heapify, heappop, heappush

def split(transactions, people):
    tran_lookup = defaultdict(float)
    total_spend = 0.0
    average = 0
    receive = []
    pay = []
    result = []
    for person, amount in transactions:
        tran_lookup[person] += amount
        total_spend += amount
    average = total_spend / len(people)
    for person in people:
        diff = - tran_lookup[person] + average
        if diff > 0:
            receive.append((diff, person))
        elif diff < 0:
            pay.append((-diff, person))
    while pay:
        pay_amount, payer = heappop(pay)
        receive_amount, receiver = heappop(receive)
        if receive_amount == pay_amount:
            result.append((payer, receiver, pay_amount))
        elif pay_amount > receive_amount:
            result.append((payer, receiver, receive_amount))
            heappush(pay, (pay_amount - receive_amount,payer))
        else:
            result.append((payer, receiver, pay_amount))
            heappush(receive, (receive_amount - pay_amount, receiver))
    print(result)
    heapify(pay)
    heapify(receive)
    print(pay, receive, total_spend, len(people), average)
split(transactions, people)