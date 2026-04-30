from langgraph.graph.state import CompiledStateGraph

def stream_graph(graph: CompiledStateGraph):
    def stream_graph_updates(user_input: str):
        for event in graph.stream({"messages": [("user", user_input)]}):
            for value in event.values():
                print("Assistant:", value["messages"][-1].content)
                
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit", "q"]:
            print("Goodbye!")
            break
        stream_graph_updates(user_input)
        