from langgraph.graph.state import CompiledStateGraph

def draw_graph(graph: CompiledStateGraph):
    try:
        graph_image = graph.get_graph().draw_mermaid_png()
        file_path = f"output.png"
        with open(file_path, "wb") as f:
            f.write(graph_image)
            print(f"Graph image saved to {file_path}")
    except Exception as e:
        print(f"Error occurred while drawing graph: {e}")
        pass