import networkx as nx 
  
# import matplotlib library 
import matplotlib.pyplot as plt 
  
# generation of a sample graph 
G = nx.Graph() 
G.add_edges_from([('râmu','šapāru'),
                  ('râmu','našû'),
                  ('râmu','mātu'),
                  ('râmu','alāku'),
                  ('râmu','ṣītu'),
                  ('râmu','šarru'),
                  ('râmu','birtu'),
                  ('râmu','târu'),
                  ('râmu','māru'),
                  ('râmu','libbu'),
                  ('râmu','ROYALTY'),
                  ('šapāru','māru')] )
  
# Defining ego as large and red 
# while alters are in lavender 
# Let 'A' be the ego 
ego = 'râmu'
pos = nx.spring_layout(G) 
nx.draw(G, pos, node_color = "lavender",  
        node_size = 800, with_labels = True) 
  
options = {"node_size": 1200, "node_color": "r"} 
nx.draw_networkx_nodes(G, pos, nodelist=[ego], **options) 
plt.show() 