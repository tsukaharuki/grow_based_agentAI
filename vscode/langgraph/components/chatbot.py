from langchain_core.messages import AIMessage, SystemMessage

def get_chatbot_node(llm):
    def chatbot_node(state):
        system_message = SystemMessage(content=(
            "あなたは優秀なAIアシスタントです。"
            "回答には必ず日本語を使用してください。"
            "ツール（tavily_search）を呼び出す際は、JSON形式の末尾に余計な記号（` や ' など）を絶対に含めないでください。"
            "語尾は必ず「ですます調」にしてください。"
            ))
        messages = state["messages"]
        response = llm.invoke([system_message] + messages)
        return {"messages": [response]}
    return chatbot_node