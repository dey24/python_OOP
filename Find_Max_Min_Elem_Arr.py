def getMinMax(arr):
    n = len(arr)
    if(n % 2 == 0):  #checking the length if it is even or not
        mx = max(arr[0], arr[1])   # taking two values from the first two indexes and comparing as to which one is the max
        mn = min(arr[0], arr[1])   # taking two values from the first two indexes and comparing as to which one is the min

        i = 2  #setting starting index to 2
    else:
        mx = mn = arr[0]  # if arr has odd number of elements, then initialize the first element as minimum and maximum

    while(i < n-1):   # for as long as iterator i is less than n-1.
        if arr[i] < arr[i+1]:    #comparing elements of a pair.
            mx = max(mx, arr[i + 1])    # setting value for mx as the max of mx and arr[i+1]
            mn = min(mn, arr[i])    # setting value for mn as the min of min and arr[i]
        else:
            mx = max(mx, arr[i])    # setting value for mx as the max of mx and arr[i]
            mn = min(mn, arr[i+1])   # setting value for mn as the min of mn and arr[i+1]

        i += 2    #incrementing the iterator by 2 as two elements are processed in a loop
    return (mx, mn)

if __name__ == '__main__':
    arr = [1000, 11, 445, 1, 330, 300]
    mx, mn = getMinMax(arr)    #calling the func and storing the result in mx, mn vars
    print("Max elem: ", mx)
    print("Min elem: ", mn)