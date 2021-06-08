import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


plt.rcParams["figure.figsize"] = (15, 15)
rules_edges = pd.read_excel(r'results\report.xlsx',
                            sheet_name="rules",
                            header=0)[['identifier',
                                       'linked_rule_identifier']]

G = nx.from_pandas_edgelist(rules_edges, source="identifier",
                            target="linked_rule_identifier")
nx.number_of_nodes(G)
cmap = plt.cm.plasma
pos = nx.spring_layout(G, 13648)
nodes = nx.draw_networkx_nodes(
    G,
    pos,
    node_size=105,
    node_shape='o',
    node_color='red',
    linewidths=1,
    edgecolors='blue'
)
edges = nx.draw_networkx_edges(
    G,
    pos,
    node_size=105,
    arrowstyle="->",
    arrowsize=10,
    edge_color='green',
    edge_cmap=cmap,
    width=1
)
plt.show()
