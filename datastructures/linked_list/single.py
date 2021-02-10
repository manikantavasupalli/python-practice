"""
Description:
------------
We need a structure class to define each link.
We need functionality class that have a list of methods that impliment the all functions such as add remove seach etc
"""


class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next


class LinkedList:
	def __init__(self):
		self.head = None

	def print(self):
		if self.head == None:
			print("Linked list is empty. Please try append values before printing them")
			return

		itr = self.head
		llist = ''
		while itr:
			llist += str(itr.data) + " => " if itr.next else str(itr.data)
			itr = itr.next
		print(llist)

	def get_length(self):
		count = 0
		itr = self.head
		while itr:
			count+= 1
			itr = itr.next
		return count
	
	def insert_at_begin(self, data):
		'''
		Just create a link. So Linked list contains only one node
		'''
		node = Node(data, self.head)
		self.head = node
		
	def insert_at(self, data, index):
		'''
		when ll is empty just add
		otherwise, traverse till index - 1,
			prelink->Newlink->nextline
		'''
		if index <0 or index > self.get_length():
			raise Exception("Invalid Index")

		if index == 0:
			self.insert_at_begin(data)
			return
		itr = self.head
		count = 0
		while itr:
			if count == index -1:
				node = Node(data, itr.next)
				itr.next = node
			itr = itr.next
			count += 1

	def append(self, data):
		'''
		when ll is empty
		'''
		if self.head == None:
			self.insert_at_begin(data)
			return
		itr = self.head
		while itr.next:
			itr = itr.next
		itr.next = Node(data, None)


	def remove(self, index):
		'''
		at zero, make its next as None and move the head to the next link
		at index, traverse till index-1 and make its next as next.next
		'''
		if index < 0 or index > self.get_length():
			raise Exception("InvalidI index")
			return
		if index == 0:
			self.head  =  self.head.next
			return

		itr = self.head
		count = 0
		while itr:
			if count == index -1:
				itr.next = itr.next.next
			count +=1
			itr = itr.next

	def insert_values(self, val_list):
		for item in val_list:
			self.append(item)

	def insert_after_value(self, data_after, data_to_insert):
		'''
		Find the search value position
		prepare the node with given data and the current link's next
		'''	
		itr = self.head
		while itr:
			if itr.data == data_after:
				node = Node(data_to_insert, itr.next)
				itr.next = node
				break
			itr = itr.next

	def remove_by_value(self, data):
    	# Remove first node that contains data
		itr = self.head
		count = 0
		found = False
		while itr:
			if data == itr.data:
				found = True
				break
			itr = itr.next
			count += 1
		if found:
			self.remove(count)
		else:
			print("Failed to remove "+ str(data))



if __name__ == "__main__":
	ll = LinkedList()
	ll.insert_values(["banana","mango","grapes","orange"])
	print(ll.get_length())
	ll.print()
	ll.insert_after_value("mango","apple") # insert apple after mango
	ll.print()
	ll.remove_by_value("orange") # remove orange from linked list
	ll.print()
	ll.remove_by_value("figs")
	ll.print()
	ll.insert_at_begin("mani")
	ll.print()
	ll.remove_by_value("banana")
	ll.remove_by_value("mango")
	ll.remove_by_value("apple")
	ll.remove_by_value("grapes")
	ll.print()
