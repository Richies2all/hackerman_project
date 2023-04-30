## This is Streamlit Predcition App

import streamlit as st
import pandas as pd
import numpy as np
from autogluon.tabular import TabularPredictor


st.title('Sentiment Prediction')
friends = st.number_input('author.properties.friends', 0,2000)
status_count = st.number_input('author.properties.status_count', 0,50000)
verified = st.selectbox('author.properties.verified', options=['True', 'False'])
body = st.selectbox('content.body', options=["Can't believe I'm missing Love Island 😩", 'How many times does he wonna say the phrase "i deal with shit" #LoveIsland', "@Amyyy14 thank u so much Amy you really get me ❤️ I come home tmrw let's get drinks", "@sickkening Yep you're also that xx"])
country = st.selectbox('location.country', options=['GB', 'GG', 'IM', 'JE'])
platform = st.selectbox('properties.platform', options=['twitter'])
latitude = st.number_input('location.latitude', 0,100)
longitude = st.number_input('location.longitude', -5,5)
sentiments=st.form('Sentiments prediction', clear_on_submit=True)


sample_data_dict = {
    
    "author.properties.friends": friends,
    "author.properties.status_count": status_count,
    "author.properties.verified": verified,
    "content.body": body,
    "location.country": country,
    "properties.platform": platform,
    "location.latitude": latitude,
    "location.longitude": longitude
    
}
st.write(sample_data_dict)

sample_data=pd.DataFrame([sample_data_dict])

st.write(sample_data)

save_path  = "artefacts/models_multiclass"

save_model_predictor = TabularPredictor.load(save_path, require_version_match=False)
submit = st.button("CLICK TO PREDICT SENTIMENTS")
if submit:
    sentiments_prediction = save_model_predictor.predict(sample_data)[0]
    st.write(f"Sentiments prediction value is: {sentiments_prediction}")