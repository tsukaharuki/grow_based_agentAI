from dotenv import load_dotenv
from langgraph.prebuilt import ToolNode

from langchain_community.tools.tavily_search import TavilySearchResults
load_dotenv()

tavily_tool = TavilySearchResults(max_results=2)

tools = [tavily_tool]

def get_tool_node():
    return ToolNode(tools=tools)

if __name__ == "__main__":#テストコードでこのファイルだけを確認したいときだけ使う
    print(tavily_tool.invoke("What is the capital of France?"))