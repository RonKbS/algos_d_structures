from listed_books import listed_books


def bubble_sort_alphabetically():
    def swap(i, j):
        listed_books[i], listed_books[j] = listed_books[j], listed_books[i]

    n = len(listed_books)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        # for-loop below implies largest-values are sorted first, as it moves them towards the end
        for i in range(1, n-x):
            if listed_books[i - 1].split(',')[1] > listed_books[i].split(',')[1]:
                # put (i - 1) after i 
                swap(i, i-1)
                swapped = True

    print(listed_books)



# 0.173s
# with_inbuilt_sort()

# 138.356 seconds || 145.888 seconds
bubble_sort_alphabetically()