from listed_books import listed_books


def with_inbuilt_sort():
    # uses Timsort algorithm, derived from merge and insertion
    # this is implemented in hand-optimized C
    listed_books.sort(key=lambda x: x.split(',')[1])
    print(listed_books)

with_inbuilt_sort()
