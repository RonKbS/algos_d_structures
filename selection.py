from listed_books import listed_books


def selection_sort_alphabetically():
    for i in range(len(listed_books)):
        minimum = i
        
        for j in range(i+1, len(listed_books)):
            # select smallest value
            if listed_books[j].split(',')[1] < listed_books[minimum].split(',')[1]:
                minimum = j


        # move smallest value to front of sorted
        # list || i.e. swap
        listed_books[minimum], listed_books[i] = listed_books[i], listed_books[minimum]

    print(listed_books)



# 0.173s
# with_inbuilt_sort()

# 129.064 seconds
selection_sort_alphabetically()