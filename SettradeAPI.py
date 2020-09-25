import settrade.openapi
import time
import json
from datetime import datetime

app_id_test = "DUN9VgTfoUZEXocR"
app_secret_test = "ALSv8m13iHZKxEdJtbh+p9lAmMbX34Waf6U/6lJxstvG"
account_test = "ausiris5"
app_code_test = "ALGO"
broker_id_test = "063"
pin_test = "111111"


investor = settrade.openapi.Investor(
    app_id=app_id_test, 
    app_secret=app_secret_test, 
    broker_id=broker_id_test, 
    app_code=app_code_test)

deriAcc = investor.Derivatives(account_no="ausiris5")
mqtt = investor.MQTTWebsocket()

def main(result, subscriber):
    tm = datetime.now()
    date_time = tm.strftime('%Y-%m-%d %H:%M:%S')
    bid = result['bid_price1']
    ask = result['ask_price1']
    

    print(f'bid:{bid} ask:{ask} {date_time}  ',end="\r")

sub = mqtt.subscribe_bid_offer("S50H21", main)
sub.start() 

