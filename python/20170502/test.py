#coding = gbk
import List
def main():	
	print("start main()")
	mylist = List.List()
	for i in range(0,10):
		mylist.Insert(i)
	print ("show me the list node\n")
	mylist.Print()
	print('\n mylist size:',mylist.GetSize())
	print("\n delete number 1 element\n")
	mylist.Remove(1)
	print("show the list after delete\n")
	mylist.Print()
	print("\n the size of list after delete %s" mylist.GetSize())
main()
