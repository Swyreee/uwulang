from typing import List


class Node:
	def __repr__(self):
		return repr("RootNode")

	nodes: List = []
	push_right_count = 0

	def add_node(self, other):
		self.nodes.append(other)

	def traverse(self):
		print("root")
		for node in self.nodes:
			node.walk()

	def walk(self, depth=1):
		raise Exception("Do not!")


class MathNode(Node):
	def __repr__(self):
		return repr(f"MathNode(left={repr(self.left)}, right={repr(self.right)}, op={repr(self.op)})")

	def walk(self, depth=1):
		indent = '\t' * depth


		if isinstance(self.left, MathNode):
			self.left.walk(depth + 1)
		else:
			print(indent + repr(self.left))

		print(indent + '\t' + self.op)

		if isinstance(self.right, MathNode):
			self.right.walk(depth + 1)
		else:
			print(indent + repr(self.right))

	def __init__(self, _left, _op, _right):
		self.left = _left
		self.right = _right
		self.op = _op

root = Node()

test_node1 = MathNode(1, '+', 2)
test_node2 = MathNode(3, '+', 4)
test_node3 = MathNode(MathNode(5, '+', 6), '+', MathNode(7, '+', 8))
test_node4 = MathNode(MathNode(MathNode(9, '+', 10), '+', 11), '*', 12)

root.add_node(test_node1)
root.add_node(test_node2)
root.add_node(test_node3)
root.add_node(test_node4)

print(root.nodes)
root.traverse()
