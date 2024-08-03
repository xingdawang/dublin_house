import osmnx as ox
import time

def get_node_id(location, G):
	lng, lat = location
	node = ox.distance.nearest_nodes(G, lng, lat, return_dist=False)
	return (lng, lat, node)