#\question{\bf{HelloWorld Program Details}}
#%\paragraph

#The input will start with a positive integer, giving the number of instances that follow. For each instance, there will be a string. For each string $s$, the program should output Hello, $s$! on its own line.

#A sample input is the following:
#\begin{verbatim}
#3
#World
#Marc
#Owen
#\end{verbatim}

#The output for the sample input should be the following:
#\begin{verbatim}
#Hello, World!
#Hello, Marc!
#Hello, Owen!
#\end{verbatim}

def main():
    # Read the number of instances
    n = int(input())
    # Loop through each instance
    for i in range(n):
        # Read the string
        s = input()
        # Print the output
        print("Hello, {}!".format(s))

if __name__ == "__main__":
    main()
