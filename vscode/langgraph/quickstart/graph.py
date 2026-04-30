import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# この下に既存の import などを書く
from components.chatbot import get_chatbot_node
from langgraph.graph import StateGraph, START, END
from components.llm import get_llm
from components.state import State
from Tool.tool import get_tool_node, tools
from route import route_tools


graph_builder = StateGraph(State)

llm = get_llm()
llm_with_tools = llm.bind_tools(tools)
chatbot = get_chatbot_node(llm_with_tools)
tool_node = get_tool_node()

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", tool_node)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges(
    "chatbot",
    route_tools,
    {"tools": "tools", END: END},
)

graph_builder.add_edge("tools", "chatbot")

graph = graph_builder.compile()

if __name__ == "__main__":
    from utils.draw import draw_graph
    draw_graph(graph)
print("successfully built the graph!")
    
if __name__ == "__main__":
    from utils.stream import stream_graph

    stream_graph(graph)

