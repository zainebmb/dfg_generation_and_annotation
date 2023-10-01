import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd 
import preprocess_FlowFromEdge
import csv
import os

def create_model_subgraphs(facts_folder,models_with_data):
    Flow_file_path = facts_folder + '/FlowFromEdge.csv'
    processed_Flow_file_path = preprocess_FlowFromEdge.process_FFE(Flow_file_path, facts_folder+ '/FlowFromEdge_preprocessed.csv')
    data = pd.read_csv(processed_Flow_file_path, delimiter='\t', header=None)
    # print('-------')
    # print(models_with_data)

    for m in models_with_data:
        subgraph_data = []
        G = nx.DiGraph()
        model = m['Model']
        train_data = m['training_data']
        eval_data = m['eval_data']
        tr_meth = m['training_method']
        eval_meth = m['eval_method']
        invos = m['train_and_eval_invo']
        train_ctx=m['training_ctx']
        eval_ctx=m['eval_ctx']
        G.add_edge(model, tr_meth)
        G.add_edge(model, eval_meth)
        G.add_edge(tr_meth, train_data)
        G.add_edge(eval_meth, eval_data)

        for index, row in data.iterrows():
            if row[4] == 'data':
                from_node = row[0]
                to_node = row[2]
                edge_type = row[5]
                if from_node != to_node:
                    G.add_edge(from_node, to_node, edge_type=edge_type)

        subgraph = nx.ego_graph(G, model, radius=700, center=True, undirected=False)
        # pos = nx.spring_layout(subgraph, seed=42)
        # nx.draw(
        #     subgraph,
        #     pos,
        #     with_labels=True,
        #     node_size=1000,
        #     node_color='skyblue',
        #     font_size=10,
        #     font_color='black',
        #     font_weight='bold',
        #     arrows=True,
        # )
        
        # edge_types = nx.get_edge_attributes(subgraph, 'edge_type')
        # nx.draw_networkx_edge_labels(subgraph, pos, edge_labels=edge_types)

        # plt.title("Subgraph")
        # plt.show()

        for source, target, edge_type in subgraph.edges(data=True):
            subgraph_data.append({'Source': source, 'Target': target, 'Edge_Type': edge_type.get('edge_type', '')})

        new_folder_name = 'models_graphs'
        new_folder_path = os.path.join(facts_folder, new_folder_name)
        
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)

        file_name = str(invos)+"_"+train_ctx+"_"+eval_ctx + '.csv'
        file_path = os.path.join(new_folder_path, file_name)

        with open(file_path, 'w') as csvfile:
            fieldnames = ['Source', 'Target', 'Edge_Type']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in subgraph_data:
                writer.writerow(row)

# create_model_subgraphs(facts_folder="C:/Users/zaineb/Desktop/facts/new_1162_w_edge_type_fact")
