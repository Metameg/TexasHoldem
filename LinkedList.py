
class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.next = None

   def get_data(self):
      return self.dataval

class SLinkedList:
   def __init__(self):
      self.head = None

   def add_node(self, newdata):
      NewNode = Node(newdata)
      if self.head is None:
         self.head = NewNode
         return
      last = self.head
      while(last.next):
         last = last.next
      last.next = NewNode

   def RemoveNode(self, Removekey):
      HeadVal = self.head
         
      if (HeadVal is not None):
         if (HeadVal.dataval == Removekey):
            self.head = HeadVal.next
            HeadVal = None
            return
      while (HeadVal is not None):
         if HeadVal.dataval == Removekey:
            break
         prev = HeadVal
         HeadVal = HeadVal.next

      if (HeadVal == None):
         return

      prev.next = HeadVal.next
      HeadVal = None

   def insert(self, middle_node, newdata):
      if middle_node is None:
         print("The mentioned node is absent")
         return

      NewNode = Node(newdata)
      NewNode.next = middle_node.next
      middle_node.next = NewNode


   def get_node(self, player):
      node = self.head
      while node.get_data() != player:
         node = node.next()
         if node is None:
               return None
      return node

   def list_print(self):
      printval = self.head
      while printval is not None:
         print (printval.dataval)
         printval = printval.next

   def get_nth_node(self, n):
      count = 0
      current = self.head
      while current:
         if count == n:
            return current.dataval
         count += 1
         current = current.next

   def iterate_from(self, list_item):
      while list_item is not None:

         yield list_item
         list_item = list_item.next
         