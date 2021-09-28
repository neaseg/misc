import random
import matplotlib.pyplot as plt
N_USERS = 10000
MIN_GAIN = 0
MAX_GAIN = 2
STARTING_CASH = 5
DAYS = 60
accounts = [STARTING_CASH] * N_USERS

total_cash = sum(accounts)

#print("Initial money in system: ${}".format(total_cash))
"""
for j in range(DAYS):
    for k in range(N_USERS):
        accounts[k] = accounts[k] * random.uniform(MIN_GAIN, MAX_GAIN)
    total_cash = sum(accounts)
    print("Money in system after {} days: ${}".format(j, total_cash))
    print("Max account: {}".format(max(accounts)))
print("Final total money: ${}".format(total_cash))
plt.plot(range(N_USERS), accounts)
plt.title("Final account totals\nTotal in system: ${}".format(total_cash))
"""
ending_cash = [0] * 200
for i in range(200):
    for j in range(DAYS):
        for k in range(N_USERS):
            accounts[k] = accounts[k] * random.uniform(MIN_GAIN, MAX_GAIN)
    ending_cash[i] = sum(accounts)
    accounts = [STARTING_CASH] * N_USERS
    
ending_cash_avg = sum(ending_cash) / len(ending_cash)
starting = STARTING_CASH * N_USERS


plt.plot(range(200), ending_cash)
plt.axhline(y=ending_cash_avg, color="red")
plt.axhline(y=starting, color="blue")
plt.title("Final Balances in System\nAverage: {}\nStarting: {}".format(ending_cash_avg, starting))