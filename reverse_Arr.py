def reverseList(arr, start, end):
    while start < end: # for as long as element before is less than element after continue the while loop
        arr[start], arr[end] = arr[end], arr[start] #swapping
        start += 1 #goes to next element
        end -= 1 #comes down below element


arr = [1, 2, 3, 4, 5]
print(arr)
reverseList(arr, 0, 4) //calling the reverse list function
print("Reversed list is: ")
print(arr)