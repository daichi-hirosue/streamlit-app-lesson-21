from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

st.title("treamlitを活用したWebアプリ開発")

st.write("##### 食事に関するアドバイザー")
st.write("食事に関する相談を入力フォームにテキストを入力し、「実行」ボタンを押すことでアドバイスをもらえます")
st.write("##### 睡眠に関するアドバイザー")
st.write("睡眠に関する相談を入力フォームにテキストを入力し、「実行」ボタンを押すことでアドバイスをもらえます")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["食事アドバイザー", "睡眠アドバイザー"]
)

st.divider()

if selected_item == "食事アドバイザー":
    input_message = st.text_input(label="食事に関する相談を入力してください")
else:
    input_message = st.text_input(label="睡眠に関する相談を入力してください")

if st.button("実行"):
    st.divider()

    if selected_item == "食事アドバイザー":
        if input_message:
            messages = [
                SystemMessage(content="あなたは食事に関するアドバイザーです。安全なアドバイスを提供してください。"),
                HumanMessage(content=input_message),
            ]
            result = llm(messages)
            st.write(result.content)
        else:
            st.error("回答の生成に失敗しました。正しく入力されているか確認してください")

    else:
        if input_message:
            messages = [
                SystemMessage(content="あなたは睡眠に関するアドバイザーです。安全なアドバイスを提供してください。"),
                HumanMessage(content=input_message),
            ]
            result = llm(messages)
            st.write(result.content)
        else:
            st.error("回答の生成に失敗しました。正しく入力されているか確認してください")