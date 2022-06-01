from typing import List



class Tree:
	def __init__(self):
		self.nodes = [RootNode()]

	def add_node(self, other):
		self.nodes.append(other)

	def traverse(self):
		for node in self.nodes:
			node.walk()

	def evaluate(self):
		for node in self.nodes:
			node.evaluate()



class Node:
	def __repr__(self):
		return repr("BasicNode")

	def walk(self):
		print(repr(self))

	def evaluate(self):
		...

	def __init__(self):
		...


class RootNode(Node):
	def __repr__(self):
		return repr("RootNode")


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


class AssignmentNode(Node):
	def __repr__(self):
		return repr(f"AssignmentNode(target={repr(self.target)}, value={repr(self.value)})")

	def walk(self, depth=1):
		indent = '\t' * depth

		if isinstance(self.target, Node):
			raise ValueError("left-hand operand must be a literal")

		print(indent + f"{self.target} = ", end="")

		if isinstance(self.value, Node):
			self.value.walk(depth + 1)
		else:
			print(indent + repr(self.value))

	def __init__(self, _target, _value):
		self.target = _target;
		self.value = _value;

tree = Tree()

test_node1 = MathNode(1, '+', 2)
test_node2 = MathNode(3, '+', 4)
test_node3 = MathNode(MathNode(5, '+', 6), '+', MathNode(7, '+', 8))
test_node4 = MathNode(MathNode(MathNode(9, '+', 10), '+', 11), '*', 12)
test_node5 = AssignmentNode('a', 3)

tree.add_node(test_node1)
tree.add_node(test_node2)
tree.add_node(test_node3)
tree.add_node(test_node4)
tree.add_node(test_node5)

tree.traverse()
tree.evaluate()
