import requests

import datetime
def get_data(pincode):
    try:
        current_time=datetime.date.today().strftime('%d-%m-%Y')
        data= requests.get(f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={current_time}') 
        s=data.json()
        if s.get('available_capacity')!=0:
            return s
        else:
            return "No Available Capacity"
    except Exception as e:
        print(e)

    return False