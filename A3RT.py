import streamlit as st
import pya3rt

apikey = "DZZ0bWBhcaF7OTfaqe905FLlmn9hiTYk"
client = pya3rt.TalkClient(apikey)

st.title("Chatbot with streamlit")
st.subheader("メッセージを入力してから送信をタップしてください")
message = st.text_input("メッセージ")

chat_logs = []

def send_pya3rt():
    ans_json = client.talk(message)
    ans = ans_json['results'][0]['reply']
    chat_logs.append('you: ' + message)
    chat_logs.append('AI: ' + ans)
    for chat_log in chat_logs:
        st.write(chat_log)

if st.button("送信"):
    send_pya3rt()