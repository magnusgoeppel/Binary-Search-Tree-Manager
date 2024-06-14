# Binary Search Tree Manager

This tool enables the processing of binary search trees, including AVL balance verification, calculation of tree statistics, and performing search operations. It can also be used to check if a specific subtree exists within a larger tree.

## Features

- **AVL Balance Check**: Verifies if the tree meets AVL balance criteria.
- **Tree Statistics**: Calculates and outputs minimum, maximum, and average key values.
- **Search**: Supports simple key search and subtree search.

## Requirements

- Python 3.4 or higher
- Library: `sys`

## Usage

```bash
AVL Tree
Outputs the balance factors of the tree and checks if it is an AVL tree:
python treecheck.py tree.txt 

Simple Search
To check if a node exists in the tree:
python treecheck.py searchtree.txt simple.txt

Subtree Search
To check if a subtree exists in the tree:
python treecheck.py searchtree.txt subtree.txt
```
