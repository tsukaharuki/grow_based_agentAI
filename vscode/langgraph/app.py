import streamlit as st #ローカルアドレスとネットワークアドレスでアプリを表示
from quickstart.graph import graph

st.title("簡易的なAIエージェント")

#チャット履歴を保存する箱
if "messages" not in st.session_state:
    st.session_state.messages = []

#過去のメッセージを画面に表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
#ユーザーからの入力を受け取る
if prompt := st.chat_input("何か聞いてください"):
    #メッセージの表示
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    #LangGraphのグラフを実行して、AIエージェントからの応答を得る
    with st.chat_message("assistant"):
        
        inputs = {"messages": [("user", prompt)]}
        result = graph.invoke(inputs)
        
        response = result["messages"][-1].content
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})