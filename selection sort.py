def selection_sort_asc(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


def selection_sort_desc(arr):
    n = len(arr)
    
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        
        arr[i], arr[max_index] = arr[max_index], arr[i]
    
    return arr


def menu_driven_selection_sort():
    print("SELECTION SORT")
    
    length = int(input("\nEnter the number of elements : "))
    arr = []
    for i in range(length):
        num=int(input("Enter element : "))
        arr.append(num)
        
    while True:
        print("\n1. Sort Ascending")
        print("2. Sort Descending")
        print("3. Exit")
        choice = int(input("Enter your choice : "))
        
        if choice == 1:
            sorted_arr = selection_sort_asc(arr)
        elif choice == 2:
            sorted_arr = selection_sort_desc(arr)
        elif choice==3:
            print("Thank You")
            break
        else:
            print("Invalid choice!")
            return
            
        print("\nSorted list : ")
        print(sorted_arr)
    
    
menu_driven_selection_sort()