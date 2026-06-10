# U - Understand the problem
         # Given input
         # dictionary with day mapping to number of tickets
         # Expected output
         # num of tickets sold
         # Edge cases
         # Any constraints

# M - Match (have you seen this problem before?)
    # most likely loop or sum func

# P - Plan your approach (written plan or pseudo code)
    # 
# I - Implement 

# R - Review (test run the code)

# E - Evaluate (time and space complexity?)

def total_sales(ticket_sales):
    total = 0
    for ticket in ticket_sales:
        total += ticket_sales.get(ticket)
    return total

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))