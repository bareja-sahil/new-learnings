class Notebooks:

    def __init__(self, title, author, likes):
        self.title = title
        self.author = author
        self.likes = likes

    def __str__(self):
        return f"Notebook {self.author}-{self.title}=likes:{self.likes}"

    def __repr__(self):
        return self.__str__()


def compare_likes(a, b):
    if a.likes < b.likes:
        return 'lesser'
    elif a.likes == b.likes:
        return 'equal'
    else:
        return 'greater'


def compare_titles(a, b):
    if a.title < b.title:
        return 'lesser'
    elif a.title == b.title:
        return 'equal'
    else:
        return 'greater'


a1 = Notebooks("x1 book", "A1 Writer", 200)
b1 = Notebooks("B1 book", "B1 Writer", 321)
c1 = Notebooks("C1 book", "C1 Writer", 211)
d1 = Notebooks("D1 book", "D1 Writer", 112)
e1 = Notebooks("E1 book", "E1 Writer", 60)

books_list = [a1, b1, c1, d1, e1]


def merge(left, right, compare_func):
    i = 0
    j = 0
    new_list = []
    while i < len(left) and j < len(right):
        if compare_func(left[i], right[j]) == 'lesser':
            new_list.append(left[i])
            i += 1
        elif compare_func(left[i], right[j]) == 'greater':
            new_list.append(right[j])
            j += 1
        else:
            new_list.append(left[i])
            i += 1
    return new_list + left[i:] + right[j:]


def merge_sort(books_list, compare_func):
    if len(books_list) <= 1:
        return books_list
    mid = len(books_list) // 2
    left = merge_sort(books_list[:mid], compare_func)
    right = merge_sort(books_list[mid:], compare_func)
    return merge(left, right, compare_func)


print(merge_sort(books_list=books_list, compare_func=compare_likes))
print(merge_sort(books_list=books_list, compare_func=compare_titles))
