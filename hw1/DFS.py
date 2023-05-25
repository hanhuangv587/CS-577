#\question
#Implement depth-first search in either C, C++, C\#, Java, Python, or Rust. Given an undirected graph with $n$ nodes and $m$ edges, your code #should run in $O(n + m)$ time. Remember to submit a makefile along with your code, just as with the first coding question.\\
#
#\textbf{Input:} the first line contains an integer $t$, indicating the number of instances that follows. For each instance, the first line #contains an integer $n$, indicating the number of nodes in the graph. Each of the following $n$ lines contains several space-separated #strings, where the first string $s$ represents the name of a node, and the following strings represent the names of nodes that are adjacent #to node $s$.
#
#The input order of the nodes is important as it will be used as the tie-breaker. For example, consider two consecutive lines of an instance:
#\begin{verbatim}
#0, F
#B, C, a
#\end{verbatim}
#Note that the tie break priority would be 0 $<$ F $<$ B $<$ C $<$ a.\\
#
#\textbf{Input constraints:}
#\begin{itemize}
#    \item $1 \leq t \leq 1000$
#    \item $1 \leq n \leq 100$
#    \item Strings only contain alphanumeric characters
#    \item Strings are guaranteed to be the names of the nodes in the graph.
#\end{itemize}
#
#\textbf{Output:} for each instance, print the names of nodes visited in depth-first traversal of the graph, \emph{with ties between nodes #visiting the first node in input order}. Start your traversal with the first node in input order. The names of nodes should be #space-separated, and each line should be terminated by a newline.\\
#
#\textbf{Sample:}
#\begin{multicols}{2}
#\textbf{Input:} 
#\begin{verbatim}
#2
#3
#A B
#B A
#C
#9
#1 2 9
#2 1 6 5 3
#4 6
#6 2 4
#5 2
#3 2 7
#7 3
#8 9
#9 1 8
#\end{verbatim}
#\columnbreak
#\textbf{Output:} 
#\begin{verbatim}
#A B C
#1 2 6 4 5 3 7 9 8
#\end{verbatim}
#\end{multicols}
#
#The sample input has two instances. 
#The first instance corresponds to the graph below on the left. 
#The second instance corresponds to the graph below on the right.
#\begin{center}
#\begin{minipage}{0.3\linewidth}
#    \begin{tikzpicture}
#        \GraphInit[vstyle=Normal]
#        \SetGraphUnit{2}
#        \Vertices{circle}{A,B,C}
#        \Edges(A,B)
#    \end{tikzpicture}
#\end{minipage}
#\qquad\qquad
#\begin{minipage}{0.3\linewidth}
#    \begin{tikzpicture}
#        \GraphInit[vstyle=Normal]
#        \SetGraphUnit{2}
#        \Vertices{circle}{5,4,3,2,1,9,8,7,6}
#        \Edges(8,9,1,2,5)
#        \Edges(2,3,7)
#        \Edges(4,6)
#        \Edges(2,6)
#    \end{tikzpicture}
#\end{minipage}

def main():
    # Read the number of instances
    t = int(input())
    # Loop through each instance
    for i in range(t):
        # Read the number of nodes
        n = int(input())
        # Initialize the adjacency list
        adj = {}
        # Loop through each node
        for j in range(n):
            # Read the node and its neighbors
            line = input().split()
            # The first string is the node
            node = line[0]
            # The remaining strings are neighbors
            neighbors = line[1:]
            # reverse neighbors
            neighbors.reverse()
            # Add the node to the adjacency list
            adj[node] = neighbors
        # Call the DFS function
        dfs(adj)

def dfs(adj):
    # Initialize the visited list
    visited = []
    # Initialize the stack
    stack = []
    # Add the first node to the stack
    stack.append(list(adj.keys())[0])
    # While the stack is not empty
    while stack:
        # Pop the top node from the stack
        node = stack.pop()
        # If the node has not been visited
        if node not in visited:
            # Add the node to the visited list
            visited.append(node)
            # Add the neighbors of the node to the stack
            stack.extend(adj[node])
    # Add unvisited nodes to the visited list by input order
    visited.extend([node for node in adj.keys() if node not in visited])
    # Print the visited list
    print(" ".join(visited))

if __name__ == "__main__":
    main()
