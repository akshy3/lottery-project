
import pandas as pd


url = 'https://www.lotto.in/kerala-state-lotteries/win-win-results'
serial = 'W-666'

df = pd.read_html(url, match = serial)
table = df[0]
table.columns = table.columns.str.replace('Ticket Numbers','tickets')
table.columns = table.columns.str.replace('Prize Amount','prize')
tickets = table['tickets']

for i,row in tickets.iteritems():
    tickets[i]=row.replace("Ending With:","")

print(tickets)
