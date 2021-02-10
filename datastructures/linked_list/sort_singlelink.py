class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	
class Linkedlist:
	def __init__(self):
		self.head = None
	
	def pprint(self):
		cur = self.head
		while cur:
			print(cur.data)
			cur = cur.next
	def append(self, value):
		if self.head == None:
			self.head = Node(value)
			return 
		cur = self.head
		while cur.next:
			cur = cur.next
		cur.next = Node(value)

	def mergelistx(self, listx):
		cur = self.head
		while cur.next:
			cur = cur.next
		cur.next = listx.head
		self.pprint()


	def append_list(self, valist):
		for val in valist:
			self.append(val)
	
	def sortthelist(self):
		cura = self.head
		while cura.next:
			cur = self.head
			while cur.next:
				if cur.data > cur.next.data:
					x = cur.data
					cur.data = cur.next.data
					cur.next.data = x
				cur = cur.next
			cura = cura.next


	
if __name__ == "__main__":
	n1 = Node(1)
	ll1 = Linkedlist()
	ll2 = Linkedlist()
	vallistA = [8000,2,5,1,7,2,100,0]
	vallistB = [3,5,2,6,2]
	ll1.append_list(vallistA)
	ll2.append_list(vallistB)
	ll1.pprint()
	ll1.sortthelist()
	ll1.pprint()
	# ll2.pprint()
	# ll1.mergelistx(ll2)
