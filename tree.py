from typing import List


class Node:
	nodes: List = []
	push_right_count = 0

	def add_node(self, other):
		self.nodes.append(other)

	def traverse(self, node=None):
		# tree = "root"
		print(root)

		for node in self.nodes:
			if isinstance(node, Node):
				self.push_right_count += 1
				self.traverse(node)
			else:
				print("\t" * self.push_right_count + repr(node))
				self.push_right_count -= 1


class BinaryOperation(Node):
	def __repr__(self):
		return repr(f"BinaryOperation(left={repr(self.left)}, right={repr(self.right)}, op={repr(self.operator)})")

	def __init__(self, left, right, operator):
		self.left = left
		self.right = right
		self.operator = operator

	

class UnaryOperation(Node):
	def __repr__(self):
		return repr(f"UnaryOperator(op={repr(self.operator)}, obj={repr(self.obj)})")

	def __init__(self, operator, obj):
		self.operator = operator
		self.obj = obj

root = Node()

root.add_node(BinaryOperation(1, BinaryOperation(2, UnaryOperation('+', 'a'), '*'), '+'))
# root.add_node(UnaryOperation('+', 'a'))
root.traverse()
# root.visualize_code_tree()
# root.visualize_tree()
