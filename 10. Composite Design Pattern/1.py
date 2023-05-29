# composite design pattern allows you to treat individual objects and groups of objects uniformly by creating a tree-like structure
# it enables clients to work with individual objects and compositions of objects in a consistent manner
# the key idea is that both individual objects and composition of objects are treated as a single entity

from abc import ABC, abstractmethod

# Component (abstract base class)
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

# Leaf
class Leaf(Component):
    def operation(self):
        print("Leaf operation")

# Composite
class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def operation(self):
        print("Composite operation")
        for child in self._children:
            child.operation()

# Usage
leaf1 = Leaf()
leaf2 = Leaf()

composite1 = Composite()
composite1.add(leaf1)
composite1.add(leaf2)

leaf3 = Leaf()

composite2 = Composite()
composite2.add(leaf3)
composite2.add(composite1)

composite2.operation()
