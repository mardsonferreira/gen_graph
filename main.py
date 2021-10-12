import sys
import os
from graphviz import Graph

###
# The function responsible for load data into the graph
###

def read_input_data(data):
    graph = {'nodes':set(), 'edges':[]}
    
    f = open(data, 'r')

    lines = f.readlines()
    for line in lines:
        row = line.split(' ')
        e1 = int(row[0])
        e2 = int(row[1])
        
        if e1 < e2:
            graph['edges'].append({'e1': e1, 'e2': e2 })
        else:
            graph['edges'].append({'e1': e2, 'e2': e1 }) 
        
        graph['nodes'].add(e1)
        graph['nodes'].add(e2)

    sort_edges = sorted(graph['edges'], key=lambda k: k['e1'])

    graph['edges'] = sort_edges

    return graph

###
# Function responsible for saving and rendering the source code
###

def draw_graph(graph, title="", view=False):
    dot = Graph(comment=title)

    for node in graph['nodes']:
	    dot.node(str(node), str(node))

    for edge in graph['edges']:
	    e1 =  edge['e1']
	    e2 =  edge['e2']	
	    dot.edge(str(e1), str(e2))

    dot.render('graphs/{}.gv'.format(title), view=view) 

###
# Get data from cmd
###

data = sys.argv[1]

base = os.path.basename(data)

filename, file_extension = os.path.splitext(base)

graph = read_input_data(data)

draw_graph(graph, filename, True)