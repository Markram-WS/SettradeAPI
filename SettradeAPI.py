from settrade.openapi import Investor
import time
import json

app_id_test = "tVWsMHC3WGvoL8wq"
app_secret_test = "AL4LYw69AZB+wiSnqHe+hiuyCRf943QUyaZmjRRlH+hs"
account_test = "FT0015D"
is_auto_queue_test = False
app_code_test = "ALGO"
broker_id_test = "041"
pin_test = "111111"

##### Place Order
symbol="GOH21"
price=1620
volume=1
side="LONG"
position="OPEN"

account_test_fail = "UNKNOWN_ACC"

# Login
print("## Login")
investor = Investor(    
		app_id=app_id_test,    
		app_secret=app_secret_test,
        app_code=app_code_test,
        broker_id=broker_id_test,
        is_auto_queue=is_auto_queue_test)

# Set Derivative Account
print("## Set Derivative Account")
deri = investor.Derivatives(account_test)

print("## Set Derivative Account")
deri_fail = investor.Derivatives(account_test_fail)

# Set MQTT
mqtt = investor.MQTTWebsocket()


print(deri.get_account_info())