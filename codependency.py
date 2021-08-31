import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout

# This function reads in a table of CERES scores from DepMap
# Subsets this table by a list of genes
# Generates a correlation matrix for this subset
def subset_corr(file_path, gene_list):
    data = pd.read_csv(file_path, index_col = 0)
    subset = data[data.columns[data.columns.isin(gene_list)]]
    corr = subset.corr(method = 'pearson')
    corr.to_csv('correlation_matrix.csv')

# This function reads in a correlation table of genes
# And a separate table of categorical corresponding info
# Plots a clustered heatmap with categorical annotation
def heatmap(file_path, gene_list):
    # Importing my depmap correlations
    data = pd.read_csv(file_path, index_col=0)

    # Importing gene info
    info = pd.read_csv(gene_list, index_col=0)
    used = info[info.index.isin(list(data.index))]

    # Use these genes to reindex the data frame by go term
    data.index = pd.MultiIndex.from_arrays([data.columns, used['Category'].to_list()], names=["Gene", "GO"])

    # go labels
    go_labels = data.index.get_level_values("GO")
    go_pal = sb.color_palette("muted")
    go_lut = dict(zip(map(str, go_labels.unique()), go_pal))

    # Convert the palette to vectors that will be drawn on the side of the matrix
    row_colors = pd.Series(go_labels, index=data.index).map(go_lut)
    col_colors = pd.Series(go_labels, index=data.columns).map(go_lut)

    # Plot the heatmap
    sb.set(font_scale=0.4)
    sb.clustermap(data, row_cluster=True, col_cluster=True,
                            cmap="RdBu_r", xticklabels=False, yticklabels=True, center=0, vmin=-1, vmax=1,
                            row_colors=row_colors, col_colors=col_colors, cbar_pos=(0.1, 0.2, 0.02, 0.6))
    plt.title(file_path)
    plt.savefig("heatmap.pdf")

# This function reads in a correlation table of genes
# And a separate table of categorical corresponding info
# Plots a network diagram of all correlations above a given cutoff
def network(file_path, cutoff, gene_list):
    # Importing my depmap correlations & reformat data
    data = pd.read_csv(file_path, index_col=0)
    links = data.stack().reset_index()
    links.columns = ['var1', 'var2', 'value']

    # Filter the data based on cutoff and remove self-correlation
    links_filtered = links.loc[(links['value'] > cutoff) & (links['var1'] != links['var2'])]

    # Graph the diagram
    G = nx.from_pandas_edgelist(links_filtered, 'var1', 'var2', ['var1', 'var2', 'value'])
    pos = graphviz_layout(G, prog='neato')

    # Make a list to specify edge color
    edge_weight = []
    for edge in G.edges:
        weight = float(G.edges[edge]['value']) / max(links_filtered['value']) * 4
        edge_weight.append(weight)

    # Import the categories for color scheme
    # Reorder gene list to assign color to each node
    gene_list = pd.read_csv(gene_list)
    categ = gene_list.set_index('Gene')
    categ = categ.reindex(G.nodes())

    # Transform categorical column in a numerical value
    categ['Category'] = pd.Categorical(categ['Category'])
    color_map = categ['Category'].cat.codes

    # Specify colors/fonts/title for graph
    nx.draw(G,
            pos=pos,
            with_labels=True, node_color=color_map, cmap=plt.cm.tab20, node_size=200, alpha=0.6,
            edge_color='lightgrey', width=edge_weight, linewidths=1, font_size=7)
    plt.savefig("network.pdf")



