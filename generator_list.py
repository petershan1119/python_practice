def index_words(text):
    """
    Source: 파이썬 코딩의 기술: Better Way 16: 리스트를 반환하는 대신 제너레이터를 고려하자
    문제: 1) 코드가 복잡 및 리스트에 추가하는 값 (index + 1)이 중요하게 안보여; 2) 반환하기 전에 모든 결과 리스트에 저장
    """
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
        return result

address = 'Four score and seven years ago...'
result = index_words(address)


def index_words_iter(text):
    """
    제너레이터 이용 함수
    """
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


def index_file(handle):
    """
    파일에서 한줄씩 읽어서 한단어씩 출력하는 제너레이터
    """
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset
