
import pandas as pd


BASE_URL = 'https://www.lotto.in/kerala-state-lotteries/'


def getResults(name,serial):
    url = BASE_URL+name+'-results'

    try:
        with open("data/"+name+"/"+serial+".json") as file:
            data = file.read()
            return data
    except:

        try:
            df = pd.read_html(url, match = serial)
        except:
            return {"error": "Invalid serial"}

        
        table = df[0]
        table.columns = table.columns.str.replace('Ticket Numbers','tickets')
        table.columns = table.columns.str.replace('Prize Amount','prize')
        tickets = table['tickets']

        for i,row in tickets.iteritems():
            tickets[i]=row.replace("Ending With:","")
        data_json = tickets.to_json()
        tickets.to_json("data/"+name+"/"+serial +".json")
        return data_json


