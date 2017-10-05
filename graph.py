
class Graph():
	def __init__(self, initial_node = None):
		self.nodes = {}
		if initial_node != None:
			self.nodes[initial_node.name] = initial_node


	def get_node_by_name(self, name):
		self.nodes.get(name)

	def add_node(self, new_node):
		self.nodes[new_node.name] = new_node
		for (n_name, n_dist) in new_node.neighbours.iteritems():
			node_to_update = self.nodes.get(n_name)
			if node_to_update == None:
				node_to_update = Node(n_name, [(new_node.name, n_dist)])
				self.nodes[n_name] = node_to_update
			node_to_update.add_neighbour(new_node.name, n_dist)
		return new_node

	def add_link(self, node1_name, node2_name, dist):
		node1 = self.nodes.get(node1_name, None)
		if node1 == None:
			node1 = self.add_node( Node(node1_name, [(node2_name, dist)]) )
		node2 = self.nodes.get(node2_name, None)
		if node2 == None:
			node2 = self.add_node( Node(node2_name, [(node1_name, dist)]) )

		node1.add_neighbour(node2.name, dist)
		node2.add_neighbour(node1.name, dist)
		
	def __repr__(self):
		str_out = 'GRAPH:\n'
		for n in self.nodes.values():
			str_out += str(n)
		return str_out


class Node():
	def __init__(self, name, neighbours=[]):
		self.name = name
		self.neighbours = {}
		# neighbours is a array of tuples with (neighbour_name, neighbour_dist)
		for (neighbour_name, neighbour_dist) in neighbours:
			self.neighbours[neighbour_name] = neighbour_dist

	def __repr__(self):
		str_out = ''
		str_out += 'Node name: {}\n'.format(self.name)
		for (key, value) in self.neighbours.iteritems():
			str_out += '    -> {} dist: {}\n'.format(key, value)
		return str_out

	def add_neighbour(self, node_name, node_dist):
		self.neighbours[node_name] = node_dist