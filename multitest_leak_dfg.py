import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import utils
import get_models_data
import preprocess_FlowFromEdge

G = nx.DiGraph()

models_with_data = get_models_data.get_models_withdata()
Flow_file_path = utils.notebook + '/FlowFromEdge.csv'
processed_Flow_file_path = preprocess_FlowFromEdge.process_FFE(
    Flow_file_path, utils.notebook + '/FlowFromEdge_preprocessed.csv')
data = pd.read_csv(processed_Flow_file_path, delimiter='\t', header=None)
print(models_with_data)

composite_graph = nx.DiGraph()

eval_meth_nodes = {}

for m in models_with_data:

    model = m['Model']
    eval_data = m['eval_data']
    eval_meth = m['eval_method']

    G.add_node(model)

    G.add_edge(model, eval_data)

    if eval_meth not in eval_meth_nodes:
        eval_meth_nodes[eval_meth] = f"{eval_meth}_node"
        G.add_node(eval_meth_nodes[eval_meth])
        G.add_edge(eval_meth_nodes[eval_meth], eval_data)

    for index, row in data.iterrows():
        if row[4] == 'data':
            from_node = row[0]
            to_node = row[2]
            edge_type = row[5]
            if from_node != to_node:
                G.add_edge(from_node, to_node, edge_type=edge_type)

    subgraph = nx.ego_graph(G, model, radius=10, center=True, undirected=False)

    pos = nx.spring_layout(subgraph, seed=42)

    composite_graph.add_edges_from(subgraph.edges(data=True))

plt.figure(figsize=(10, 10))
pos = nx.spring_layout(composite_graph, seed=42)
nx.draw(
    composite_graph,
    pos,
    with_labels=True,
    node_size=1000,
    node_color='skyblue',
    font_size=10,
    font_color='black',
    font_weight='bold',
    arrows=True,
)

edge_types = nx.get_edge_attributes(composite_graph, 'edge_type')
nx.draw_networkx_edge_labels(composite_graph, pos, edge_labels=edge_types)

plt.title("Composite Graph with Subgraphs")
plt.show()
print(composite_graph.edges)























# import networkx as nx
# import matplotlib.pyplot as plt
# import pandas as pd
# import utils
# import get_models_data
# import preprocess_FlowFromEdge

# G = nx.DiGraph()

# models_with_data = get_models_data.get_models_withdata()
# Flow_file_path = utils.notebook + '/FlowFromEdge.csv'
# processed_Flow_file_path = preprocess_FlowFromEdge.process_FFE(
#     Flow_file_path, utils.notebook + '/FlowFromEdge_preprocessed.csv')
# data = pd.read_csv(processed_Flow_file_path, delimiter='\t', header=None)
# print(models_with_data)

# # Create a composite graph to store all subgraphs
# composite_graph = nx.DiGraph()

# for m in models_with_data:

#     model = m['Model']
#     eval_data = m['eval_data']
#     # eval_meth = m['eval_method']
#     G.add_edge(model, eval_data)
#     # G.add_edge(eval_meth, eval_data)
#     for index, row in data.iterrows():
#         if row[4] == 'data':
#             from_node = row[0]
#             to_node = row[2]
#             edge_type = row[5]
#             if from_node != to_node:
#                 G.add_edge(from_node, to_node, edge_type=edge_type)

#     # Create subgraph with variables related to a given model
#     subgraph = nx.ego_graph(G, model, radius=4, center=True, undirected=False)

#     # Position the nodes based on the layout of the subgraph
#     pos = nx.spring_layout(subgraph, seed=42)

#     # Combine the subgraph into the composite graph
#     composite_graph.add_edges_from(subgraph.edges(data=True))

# # Draw the composite graph
# plt.figure(figsize=(10, 10))
# pos = nx.spring_layout(composite_graph, seed=42)
# nx.draw(
#     composite_graph,
#     pos,
#     with_labels=True,
#     node_size=1000,
#     node_color='skyblue',
#     font_size=10,
#     font_color='black',
#     font_weight='bold',
#     arrows=True,
# )

# # Add edge types as labels
# edge_types = nx.get_edge_attributes(composite_graph, 'edge_type')
# nx.draw_networkx_edge_labels(composite_graph, pos, edge_labels=edge_types)

# plt.title("Composite Graph with Subgraphs")
# plt.show()
# print(composite_graph.edges)