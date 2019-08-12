from listed_books import listed_books


def insertion_sort_alphabetically():
    for i in range(len(listed_books)):
        cursor = listed_books[i]
        position = i
        
        while position > 0 and listed_books[position - 1].split(',')[1] > cursor.split(',')[1]:
            # move the book down the list
            listed_books[position] = listed_books[position - 1]
            position -= 1

        # do final swap
        listed_books[position] = cursor


    print(listed_books)



# 0.173s
# with_inbuilt_sort()

# 66.718 seconds
insertion_sort_alphabetically()
