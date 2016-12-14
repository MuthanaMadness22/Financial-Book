# Financial-Book
#The code is designed for my personal use. This helps keeps track of how much I spent on a weekly basis. 
import time

#The data will be uploaded and saved on a seperate folder
test = open('sheet.txt', 'a')


def weeknumber(x):
    week = 0
    for block in x:
        week += 1
    week = week/10
    return week + 1


accounts = {
    'Paypal': 0.0,
    'MnT': 0.0,
    'Discover': 0.0,
    'Cash': 0.0
}
accounts['Paypal'] = raw_input("How much on Paypal \n>>")
accounts['MnT'] = raw_input("How much on MnT \n>>")
accounts['Discover'] = raw_input("How much on Discover\n>>")
accounts['Cash'] = raw_input("How much on Cash\n>>")

total = 0

# Total equals the amount you have in your account
for key in accounts:
    total += float(accounts[key])

total = total - (2 * float(accounts['Discover']))
print total


def really(row, a):
    lines = []
    with open('sheet.txt', 'rt') as s:
        for line in s:
            lines.append(line)
    amount = lines[-row]
    amount = str(amount)
    amount = amount[a:]
    amount = float(amount)
    return amount


pay = really(3, 15)

difference = total - pay
test = open('sheet.txt', 'r+')
# appends total to sheet
with test as sheet:
    sheet.write('\n\nWeek#: ' + str(weeknumber(test)))
    sheet.write('\nDate: ' + time.strftime('%m/%d/%y'))
    sheet.write('\n\n' + 'Pay: ' + accounts['Paypal'])
    sheet.write('\n' + 'MnT: ' + accounts['MnT'])
    sheet.write('\n' + 'Dis: ' + accounts['Discover'])
    sheet.write('\n' + 'Csh: ' + accounts['Cash'])
    sheet.write('\n\nTotal Balance: '+str(total))
    sheet.write('\nDifference: ' + str(difference))
    sheet.write('\n_________________________________')
