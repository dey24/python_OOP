# Function to print all sub strings
def subString(str, n):
    # Pick starting point in outer loop
    # and lengths of different strings for
    # a given starting point
    for i in range(n):
        for len in range(i + 1, n + 1):
            print(str[i: len]);


# Driver program to test above function
str = input("Enter The String: ")
subString(str, len(str));

