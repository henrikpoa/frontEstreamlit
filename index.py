import requests
import streamlit as st
import pandas as pd
import models.onus as onus
import json

st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">', unsafe_allow_html=True)
        

BASE_URL = "http://localhost:8080"

def getOnus():
    url = f'{BASE_URL}/onus'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def insertOnus(data):
    url = f'{BASE_URL}/onus'
    response = requests.post(url, json=data)
    if response.status_code == 201:
        return 'created'
    else:
        return 'fail'
    
    
def home():

    st.sidebar.title('Menu')
    pageCliente = st.sidebar.selectbox('Onu', ['Incluir', 'Consultar', 'Alterar', 'Excluir'])

    if pageCliente == 'Incluir':
        st.title('Incluir Onus')
        with st.form(key='Include_onu'):
            input_onuName = st.text_input(label='Insira o nome da Onu', value='OnuX')
            input_onuNumber = st.text_input(label='Insira o Número da Onu', value='99')
            input_onuSerial = st.text_input(label='Insira o Serial da Onu', value='ZTEzx12yz34')
            input_vlanGerId = st.text_input(label='Insira Vlan Id da rede gerência', value='100')        
            input_vlanCliente = st.text_input(label='Insira nome da Vlan do Cliente', value='Nome rede')
            input_VlanId = st.text_input('Inserir vlanid cliente', value='101')
            input_pon = st.selectbox(label='Selecione a PON', options=['1/2/1', '1/2/2', '1/2/3', '1/2/4', '1/2/5'])
            input_ipOnu = st.text_input(label='Insira o endereço IP da Onu', value='10.255.136.10')        
            input_vlanName3 = st.text_input(label='Insira o Nome da rede 3', value='103')
            input_vlanId3 = st.text_input(label='Insira o Id da vlan 3', value='104')

            input_buttonSubmit = st.form_submit_button('Enviar')
        
        if input_buttonSubmit:        
            dataDict = {'onu_number' : input_onuNumber, 'serial' : input_onuSerial, 'vlan_ger' : input_vlanGerId,
                        'vlan_name' : input_vlanCliente, 'ip':  input_ipOnu, 'pon' : input_pon,
                        'vlan_name3' :input_vlanName3, 'vlan_id3' :input_vlanId3, 'name' : input_onuName, 
                        'vlan_id' : input_VlanId}

            insertOnus(dataDict)
            st.success('Onu incluída com sucesso')            

    if pageCliente == 'Consultar':
        st.title('Consulta Onus')
        if st.button('Buscar'):
            infoUser = getOnus()
            if infoUser is not None:           
                st.write(pd.DataFrame(infoUser['content']))             


home()