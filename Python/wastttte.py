from datetime import date
import requests
import datetime
pincode="281001"
today = date.today()
today = today.strftime("%d/%m/%Y")
url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode="+pincode+"&date="+str(today)
print(url)
result = requests.get(url)
print(result)
dict = result.json()
details=[]
if result.status_code!=200 or len(dict["sessions"])==0:
    print("Sorry, no vaccines available!")
else:
    print("Vaccines Available!!")
    print("details : ")
    for i in range(len(dict["sessions"])):
        a=dict["sessions"][i]
        print(a["name"],"(",a["min_age_limit"],"+) : ",a["available_capacity"])