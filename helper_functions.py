from itertools import combinations, chain, tee


def flatten(list_of_lists):
    """
    목적: 중첩된 list를 평평하게 만들어주고 iterator로 뱐환
    예제:
    a = [[1,2,3],[4,5,6,7],[8,9]]
    list(flatten(a)) -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    return chain.from_iterable(list_of_lists)


def pairwise(iterable):
    """
    목적: 리스트를 연속된 쌍으로 만들어 tuple로 묶은 뒤 iterator 반환
    예제:
    a = [1,2,3,4,5,6]
    list(pairwise(a)) -> [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
    """
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


itertools.__file__