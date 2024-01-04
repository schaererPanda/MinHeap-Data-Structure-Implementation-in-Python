# Name: Steven Schaerer
# OSU Email: schaeres@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 5
# Due Date: May 30 by 11:59pm
# Description: Assignment 5, MinHeap Implementation


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """
        Adds a new object to MinHeap
        """
        def percolate_up(heap: MinHeap, child_index: int):
            """Percolates up the node to its correct position (index)"""
            while child_index > 0:
                parent_index = (child_index - 1) // 2
                if heap._heap.get_at_index(child_index) < heap._heap.get_at_index(parent_index):
                    temp = heap._heap.get_at_index(child_index)  # swap values, use set_at_index method
                    heap._heap.set_at_index(child_index, heap._heap.get_at_index(parent_index))
                    heap._heap.set_at_index(parent_index, temp)
                    child_index = parent_index
                else:  # already at the right location
                    break

        self._heap.append(node)  # Add new node to the end of the heap
        percolate_up(self, self._heap.length() - 1)

    def is_empty(self) -> bool:
        """
        Returns True if heap is empty, else returns False.
        """
        if self._heap.is_empty():
            return True
        else:
            return False

    def get_min(self) -> object:
        """
        Returns an object with the minimum key, without removing it from the heap.
        """
        if self.is_empty():
            raise MinHeapException("Empty")
        else:
            return self._heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        Returns an object with the minimum key, and removes it from the heap.
        """
        if self._heap.is_empty():
            raise MinHeapException("Empty Heap Error")

        min_element = self._heap.get_at_index(0)  # root
        last_index = self._heap.length() - 1  # last element index
        last_element = self._heap.get_at_index(last_index)  # last element
        self._heap.set_at_index(0, last_element)  # set root equal to last element
        self._heap.remove_at_index(last_index)  # remove last element

        if not self._heap.is_empty():
            _percolate_down(self._heap, 0)

        return min_element

    def build_heap(self, da: DynamicArray) -> None:
        """
        Recieves a DynamicArray with objects in any order, and builds a proper MinHeap from them
        """
        self._heap = DynamicArray()  # initialize new da instance
        for i in range(da.length()):
            self._heap.append(da.get_at_index(i))  # append da elements to self._heap
        for i in range(self._heap.length() // 2, -1, -1):  # iterate through each parent
            _percolate_down(self._heap, i)

    def size(self) -> int:
        """
        Returns the number of items currently stored in the heap
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        Clears the contents of the heap
        """
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    """
    Recieves a DynamicArray and sorts its content in a non-ascending order, using the Heapsort algorithm.  Sorts array
    in place, without creating any data structures and does not return anything.
    """
    heap = MinHeap()
    heap.build_heap(da)

    for i in range(da.length() - 1, -1, -1):  # iterate in reverse over array starting at last element
        da.set_at_index(i, heap.remove_min())  # replace i with smallest element

def heapify(da: DynamicArray, n: int, i: int):
    """Turn DynamicArray into a heap"""
    smallest = i
    left = 2 * i + 1  # L child
    right = 2 * i + 2  # R child

    if left < n and da.get_at_index(left) < da.get_at_index(smallest):  # if L child in bounds and value < parent
        smallest = left
    if right < n and da.get_at_index(right) < da.get_at_index(smallest):  # if R child in bounds and value < smallest
        smallest = right

    if smallest != i:
        da.set_at_index(i, smallest)  # swap values
        heapify(da, n, smallest)

def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
    Percolate value down to correct position (index)
    """
    child_i_L = 2 * parent + 1  # left child
    child_i_R = 2 * parent + 2  # right child
    length = da.length()

    while child_i_L < length:  # while L child index within bounds
        min_child_index = child_i_L  # min value set to L child
        if child_i_R < length:  # check R child in bounds
            if da.get_at_index(child_i_R) < da.get_at_index(child_i_L):  # if R child < L child
                min_child_index = child_i_R  # change min to R child
        if da.get_at_index(parent) > da.get_at_index(min_child_index):
            temp = da.get_at_index(parent)  # store parent value
            da.set_at_index(parent, da.get_at_index(min_child_index))  # set parent to min
            da.set_at_index(min_child_index, temp)  # set child to parent
        else:
            break

        parent = min_child_index  # update parent index
        child_i_L = 2 * parent + 1  # reset children
        child_i_R = 2 * parent + 2

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
