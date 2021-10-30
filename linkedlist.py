class Node:
    """
    An object for storing a single node in a linked list

    Attributes:
        data: Data stored in node
        next_node: Reference to next node in linked list
    """

    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return "<Node data: %s>" % self.data

class Linkedoist:
    """
    Linear data structure that stores values in nodes. The list maintains a reference to the first node, also called head. Each node points to the next node in the list

    Attributes:
        head: The head node of the list
    """

    def __init__(self):
        self.head = None
        # Maintaining a count attribute allows for len() to be implemented in
        # constant time
        self.__count = 0

    def is_empty(self):
        """
        Determines if the linked list is empty
        Takes O(1) time
        """

        return self.head is None

    def node_at_index(self,index):
      if index == 0:
        return self.head
      else:
        pos = 0
        current = self.head
        while pos < index:
          current = current.next_node
          pos += 1
        return current
    def size(slef):
      current = slef.head
      count = 0
      while current:
        current = current.next_node
        count += 1
      return count

    def __len__(self):
        """
        Returns the length of the linked list
        Takesn O(1) time
        """

        return self.__count

    def add(self,data):
      New_node = Node(data)
      New_node.next_node = self.head
      self.head = New_node
