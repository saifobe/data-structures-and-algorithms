import pytest
from linked_list.linked_list import LinkedList
from linked_list.node import Node




def test_empty_linked_list():
    linked_list = LinkedList()
    assert linked_list.head == None


def test_insert_linked_list():
    linked_list = LinkedList()
    linked_list.insert(5)
    assert linked_list.head.value == 5


def test_insert_multiple_linked_list():
    linked_list = LinkedList()
    linked_list.insert(5)
    linked_list.insert(10)
    linked_list.insert(15)
    assert linked_list.head.value == 15
    assert linked_list.head.next.value == 10
    assert linked_list.head.next.next.value == 5


def test_find_existing_value():
    linked_list = LinkedList()
    linked_list.insert(5)
    linked_list.insert(10)
    linked_list.insert(15)
    assert linked_list.includes(10) == True


def test_find_non_existing_value():
    linked_list = LinkedList()
    linked_list.insert(5)
    linked_list.insert(10)
    linked_list.insert(15)
    assert linked_list.includes(20) == False


def test_to_string():
    linked_list = LinkedList()
    linked_list.insert(5)
    linked_list.insert(10)
    linked_list.insert(15)
    assert linked_list.to_string() == "{ 15 } -> { 10 } -> { 5 } -> NULL"



def test_append_linked_list():
    linked_list = LinkedList()
    linked_list.append(5)
    assert linked_list.head.value == 5


def test_append_multiple_linked_list():
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(15)
    assert linked_list.head.value == 5
    assert linked_list.head.next.value == 10
    assert linked_list.head.next.next.value == 15

def test_kth_from_end_greater_than_length():
    ll = LinkedList()
    ll.head = Node(1)
    with pytest.raises(Exception):
        ll.kth_from_end(2)


def test_kth_from_end_same_length():
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    assert ll.kth_from_end(0) == 2


def test_kth_from_end_not_positive_integer():
    ll = LinkedList()
    ll.head = Node(1)
    with pytest.raises(Exception):
        ll.kth_from_end(-1)


def test_kth_from_end_size_1():
    ll = LinkedList()
    ll.head = Node(1)
    assert ll.kth_from_end(0) == 1


def test_kth_from_end_happy_path():
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(3)
    ll.head.next.next.next = Node(4)
    assert ll.kth_from_end(2) == 2



def test_zipLists1():
    linked_list1 = LinkedList()
    linked_list1.append(1)
    linked_list1.append(3)
    linked_list1.append(2)
    linked_list2 = LinkedList()
    linked_list2.append(5)
    linked_list2.append(9)
    linked_list2.append(4)
    zipList = linked_list1.zipLists(linked_list1, linked_list2)
    assert zipList.to_string() == "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> NULL"

def test_zipLists2():
    linked_list1 = LinkedList()
    linked_list1.append(1)
    linked_list1.append(3)
    linked_list2 = LinkedList()
    linked_list2.append(5)
    linked_list2.append(9)
    linked_list2.append(4)
    zipList = linked_list1.zipLists(linked_list1, linked_list2)
    assert zipList.to_string() == "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 4 } -> NULL"

def test_zipLists3():
    linked_list1 = LinkedList()
    linked_list1.append(1)
    linked_list1.append(3)
    linked_list1.append(2)
    linked_list2 = LinkedList()
    linked_list2.append(5)
    linked_list2.append(9)
    zipList = linked_list1.zipLists(linked_list1, linked_list2)
    assert zipList.to_string() == "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> NULL"

def test_zipLists_one_list_is_null():
    linked_list1 = LinkedList()
    linked_list1.append(1)
    linked_list1.append(3)
    linked_list1.append(2)
    linked_list2 = LinkedList()
    zipList = linked_list1.zipLists(linked_list1, linked_list2)
    assert zipList.to_string() == "{ 1 } -> { 3 } -> { 2 } -> NULL"

def test_zipLists_both_lists_are_null():
    linked_list1 = LinkedList()
    linked_list2 = LinkedList()
    zipList = linked_list1.zipLists(linked_list1, linked_list2)
    assert zipList.to_string() == "NULL"


    
   
    

