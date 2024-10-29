from collections import deque


def pearson_is_seller(name):
    return name[-1] == 'm'


def wide_search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        pearson = search_queue.popleft()
        if pearson in searched:
            if pearson_is_seller(pearson):
                print(f'pearson {pearson} is seller!')
                return True
            else:
                search_queue += graph[pearson]
                searched.append(pearson)
    return false


wide_search('you')
