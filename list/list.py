# 파이썬 리스트의 장점
# 1. 스택과 큐에서 사용가능한 모든 연산을 함께 제공한다
# 2. 다양한 기능을 제공하면서도 O(1)에 실행 가능한 연산들도 몇가지 있다

# 리스트의 선언방법
a = list()
b = []
c = [1, 2, 3]
# append 함수는 list에 마지막에 추가하는 함수이다
c.append(4)
# insert 함수는 해당 인덱스에 해당값을 추가하는 함수이다
c.insert(3, 5)
# 한개의 리스트에 여러가지 자료형을 담을수도 있다
c.insert(4, '안뇽')
# 슬라이싱이라는 기능을 제공하여 특정 범위 내의 값을 매우 편리하게 가져올수있다
# 슬라이싱의 리턴값은 리스트형태이다
# ↓는 c라는 리스트에서 1번부터 3번 이전 까지의 요소들을 가지고 온다
c[1:3]
# c[1:] 일경우는 1번부터 마지막까지
# c[:4] 일경우는 시작부터 4번 까지
# c[2:10:2] 일경우는 2에서 10번까지 2단계씩 c[2]->c[4]..... 이런식으로

# 존재하지 않는 인덱스를 조회 할경우 INDEXERROR가 발생할수있으니
# 다음과같이 try 구문으로 예외처리를 해줘야한다
try:
    print(a[100])
except IndexError:
    print('존재하지않는 인덱스')

# 리스트로 요소를 삭제하는 방법
# 1. 인덱스로 삭제하기
del c[1]
# 2. 값을 삭제하기
c.remove(2)
# 3. pop함수를 이용해도 삭제가 되기는 하나 , 삭제될값을 리턴한다
c.pop(3)

# 파이썬의 모든 자료형 (정수형도) 객체로 되어있다
# 리스트는 객체로 되어있는 모든 자료형을 포인터로 연결한다
# 그렇기 때문에 제각기 다양한 타입을 동시에 리스트에서 관리하는것이 가능하다

