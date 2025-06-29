# Python equivalent of ligma.config.js
# Daily algorithm progression following ThePrimeagen's course order

# Course progression - algorithms in learning order
# This follows the structure of "The Last Algorithms Course You'll Need"
COURSE_PROGRESSION = [
    # Week 1: Search & Basic Algorithms
    "LinearSearch",
    "BinarySearchList", 
    "TwoCrystalBalls",
    
    # Week 2: Sorting Fundamentals
    "BubbleSort",
    "InsertionSort",
    
    # Week 3: Data Structures Basics
    "Queue",
    "Stack",
    "ArrayList",
    
    # Week 4: Linked Lists
    "SinglyLinkedList",
    "DoublyLinkedList",
    
    # Week 5: Advanced Sorting
    "MergeSort",
    "QuickSort",
    
    # Week 6: Tree Traversals
    "BTPreOrder",
    "BTInOrder", 
    "BTPostOrder",
    "BTBFS",
    
    # Week 7: Tree Operations
    "CompareBinaryTrees",
    "DFSOnBST",
    
    # Week 8: Graph Algorithms
    "BFSGraphMatrix",
    "DFSGraphList",
    
    # Week 9: Advanced Graph Algorithms
    "Dijkstra",
    "PrimsList",
    
    # Week 10: Advanced Data Structures
    "Trie",
    "LRU",
    "Map",
]

# For backwards compatibility, keep DSA as an alias
DSA = COURSE_PROGRESSION

# You can customize your starting point
# Set to 0 to start from the beginning, or any index to skip ahead
STARTING_ALGORITHM_INDEX = 0

# Daily practice mode - only generate one algorithm per day
DAILY_MODE = True
