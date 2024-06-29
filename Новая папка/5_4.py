# class Node:
#     def __init__(self, data, prev=None):
#         self.data = data
#         self.prev = prev
#
#
# class WeatherSteck:
#     def __init__(self):
#         self.top = None
#         self.size = 0
#         self.min = None
#
#     def add_temperatyre(self, item):
#         node = Node(item)
#
#         if self.size == 0:
#             self.top = node
#             self.min = [item, self.size + 1]
#         else:
#             node.prev = self.top
#             self.top = node
#             if node.data < self.min[0]:
#                 self.min = [node.data, self.size + 1]
#         self.size += 1
#
#     def get_min(self):
#         return f'min = {self.min[0]}, in {self.min[1]} node'
#
#
# stack = WeatherSteck()
# stack.add_temperatyre(11)
# stack.add_temperatyre(23)
# stack.add_temperatyre(1)
# stack.add_temperatyre(34)
# stack.add_temperatyre(-7)
# stack.add_temperatyre(5)
# stack.add_temperatyre(3)
# stack.add_temperatyre(55)
# print(stack.get_min())

#
# class Node:
#     def __init__(self, data, status='New', prev=None):
#         self.data = data
#         self.prev = prev
#         self.status = status
#
#
# class OrderList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0
#
#     def add_order(self, item):
#         node = Node(item)
#         if self.size == 0:
#             self.head = node
#         else:
#             self.tail.prev = node
#         self.tail = node
#         self.size += 1
#
#     def peek(self, number):
#         if self.size == 0 or number > self.size:
#             return None
#         if number == 1:
#             return self.head.status
#         if number == self.size:
#             return self.tail.status
#         else:
#             target_link = self.head
#             for i in range(number - 1):
#                 target_link = target_link.prev
#             return target_link.status
#
#     def change_status(self, new_status, position):
#         if self.size == 0 or position > self.size:
#             return "There is nothing"
#         if position == 1:
#             self.head.status = new_status
#         if position == self.size:
#             self.tail.status = new_status
#         else:
#             target_link = self.head
#             for i in range(position - 1):
#                 target_link = target_link.prev
#             target_link.status = new_status
#
#
# lst = OrderList()
# lst.add_order(1)
# lst.add_order(2)
# lst.add_order(3)
# lst.add_order(4)
# lst.add_order(5)
# lst.add_order(6)
# lst.add_order(7)
# lst.add_order(8)
# lst.add_order(9)
# print(lst.peek(5))
# lst.change_status("sent", 1)
# lst.change_status("sent", 5)
# lst.change_status("sent", 7)
# lst.change_status("sent", 9)
#
#
# print(lst.peek(5))
# print(lst.peek(1))
# print(lst.peek(9))
