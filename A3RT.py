import streamlit as st
import pya3rt

#apikey = "DZZ0bWBhcaF7OTfaqe905FLlmn9hiTYk"
#client = pya3rt.TalkClient(apikey)

import requests

# def talk_api(message):
#     apikey = "DZZ0bWBhcaF7OTfaqe905FLlmn9hiTYk"  #@param {type:"string",title:"キー入力"}
#     talk_url = "https://api.a3rt.recruit.co.jp/talk/v1/smalltalk"
#     payload = {"apikey": apikey, "query": message}
#     response = requests.post(talk_url, data=payload)



st.title("Chatbot with streamlit")
st.subheader("メッセージを入力してから送信をタップしてください")
message = st.text_input("メッセージ")

chat_logs = []

def talk_api(message):
    apikey = "DZZ0bWBhcaF7OTfaqe905FLlmn9hiTYk"  #@param {type:"string",title:"キー入力"}
    talk_url = "https://api.a3rt.recruit.co.jp/talk/v1/smalltalk"
    payload = {"apikey": apikey, "query": message}
    response = requests.post(talk_url, data=payload)
    ans = response['results'][0]['reply']
    chat_logs.append('you: ' + message)
    chat_logs.append('AI: ' + ans)
    for chat_log in chat_logs:
        st.write(chat_log)



# def send_pya3rt():
#     ans_json = client.talk(message)
#     ans = ans_json['results'][0]['reply']
#     chat_logs.append('you: ' + message)
#     chat_logs.append('AI: ' + ans)
#     for chat_log in chat_logs:
#         st.write(chat_log)

if st.button("送信"):
    talk_api(message)