import streamlit as st
import pickle
from joblib import load

st.title('Expresso churn')
region=st.number_input('REGION')
montant=st.number_input('MONTANT')
frequence=st.number_input('FREQUENCE_RECH')
revenue=st.number_input('REVENUE')
arpu=st.number_input('ARPU_SEGMENT')
frequen=st.number_input('FREQUENCE')
data=st.number_input('DATA_VOLUME')
net=st.number_input('ON_NET')
orange=st.number_input('ORANGE')
tigo=st.number_input('TIGO')
zone1=st.number_input('ZONE1')
zone2=st.number_input('ZONE2')
mrg=st.number_input('MRG')
regularity=st.number_input('REGULARITY')
freq=st.number_input('FREQ_TOP_PACK')



model = load('model.joblib')




if st.button("Predict"):
    prediction = model.predict([[region, montant,frequence,revenue,arpu,frequen,data,net,orange,tigo,zone1,zone2,mrg,regularity,freq ]])
    st.write(f"Prediction: {prediction[0]}")