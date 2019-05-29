wageInput = input('Input your hourly wage\n')
try:
    wage = float(wageInput)
except:
    print('That is an illegal entry.')

hoursInput = input('Input the number of hours you have worked\n')
try:
    hours = float(hoursInput)
except:
    print('That is an illegal entry.')

pay = wage * hours
print('You earned $' + str(pay))
