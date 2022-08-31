import streamlit as st
import urllib.request
import json
#import pya3rt
#from transformers import T5Tokenizer, AutoModelForCausalLM

#apikey = "DZZ0bWBhcaF7OTfaqe905FLlmn9hiTYk"
#client = pya3rt.TalkClient(apikey)

#import requests

# def talk_api(message):
#     apikey = "DZZ0bWBhcaF7OTfaqe905FLlmn9hiTYk"  #@param {type:"string",title:"キー入力"}
#     talk_url = "https://api.a3rt.recruit.co.jp/talk/v1/smalltalk"
#     payload = {"apikey": apikey, "query": message}
#     response = requests.post(talk_url, data=payload)



st.title("Chatbot with streamlit2")
st.subheader("メッセージを入力してから送信をタップしてください")
message = st.text_input("メッセージ")

chat_logs = []


def talk_api(message):
    API_URL = "https://api.a3rt.recruit.co.jp/talk/v1/smalltalk"
    post_data = {
        "apikey" : "DZZ0bWBhcaF7OTfaqe905FLlmn9hiTYk",  #自身のapikeyに書き換えてください。
        "query" : message,  #ここに投げたい言葉を入力します。
                }
    encoded_post_data = urllib.parse.urlencode(post_data).encode(encoding='utf-8')
    page_text = ""
    with urllib.request.urlopen(url=API_URL, data=encoded_post_data) as page:
        for line in page.readlines():
            page_text = page_text + line.decode('utf-8')
    data = json.loads(page_text)
    data = data['results'][0]['reply']

    chat_logs.append('you: ' + message)
    chat_logs.append('AI: ' + data)
    for chat_log in chat_logs:
        st.write(chat_log)
    

# def talk_api(message):
#     apikey = "DZZ0bWBhcaF7OTfaqe905FLlmn9hiTYk"  #@param {type:"string",title:"キー入力"}
#     talk_url = "https://api.a3rt.recruit.co.jp/talk/v1/smalltalk"
#     payload = {"apikey": apikey, "query": message}
#     response = requests.post(talk_url, data=payload)
#     ans = response['results'][0]['reply']
#     chat_logs.append('you: ' + message)
#     chat_logs.append('AI: ' + ans)
#     for chat_log in chat_logs:
#         st.write(chat_log)



# def send_pya3rt():
#     ans_json = client.talk(message)
#     ans = ans_json['results'][0]['reply']
#     chat_logs.append('you: ' + message)
#     chat_logs.append('AI: ' + ans)
#     for chat_log in chat_logs:
#         st.write(chat_log)

if st.button("送信"):
    talk_api(message)

