# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 08:16:54 2023

@author: lovro
"""

import matplotlib.pyplot as plt
import networkx as nx

G = nx.complete_graph(5)

nx.draw(G)
