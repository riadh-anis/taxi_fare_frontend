import streamlit as st
import requests
from datetime import datetime
'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

pickup_date = st.date_input('Pickup Date',value =None , disabled=False)
pickup_time = st.time_input('Pickup Time',value =None , disabled=False)
pickup_longitude = st.number_input('Select a pickup longitude')
pickup_latitude= st.number_input('Select a pickup latitude')
dropoff_longitude = st.number_input('Select a dropoff longitude')
dropoff_latitude= st.number_input('Select a dropoff latitude')
passenger= st.number_input('Select the number of passengers')
# st.write('The current date & time is', pickup_datetime)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

passenger = int(passenger)
pickup_datetime = f'{pickup_date} {pickup_time}'

data = {
        # "key": "2021-07-06 17:18:00.000000119",
        "pickup_datetime": f'{pickup_date} {pickup_time}',
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger
    }

# pass_type = type(f'{pickup_date} {pickup_time}')
# pass_type
# pickup_datetime
r = requests.get(url, params=data)
resp = r.json()
resp
