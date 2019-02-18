### [Challenge Name: Binary Search Tree : Lowest Common Ancestor](/challenges/binary-search-tree-lowest-common-ancestor)


You are given pointer to the root of the binary search tree and two values $v1$ and $v2$. You need to return the lowest common ancestor ([LCA](https://en.wikipedia.org/wiki/Lowest_common_ancestor)) of $v1$ and $v2$ in the binary search tree.  


![image](https://s3.amazonaws.com/hr-assets/0/1529959649-81b68736f7-lcaexample.png)  
[//]: # "![image](https://s3.amazonaws.com/hr-assets/0/1502911253-5a96d423eb-lca.png)"

In the diagram above, the lowest common ancestor of the nodes $4$ and $6$ is the node $3$.  Node $3$ is the lowest node which has nodes $4$ and $6$ as descendants.

**Function Description**  

Complete the function *lca* in the editor below.  It should return a pointer to the lowest common ancestor node of the two values given.  

lca has the following parameters:  
-  root: a pointer to the root node of a binary search tree  
-  v1: a node.data value  
-  v2: a node.data value  
