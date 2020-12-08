import collections

# 딕셔너리의 선언 방법
a = dict()
a = {}

# 딕셔너리의 초기값 지정 방법
a = {'key1': 'value1', 'key2': 'value2'}
# ↓와같은 방식으로 나중에 별도로 선언할수도있다
a['key3'] = 'value3'

# 리스트에서 존재하지 않는 인덱스를 조회할 경우 IndexError 가 발생하는것처럼
# 딕셔너리에서는 존재하지않는 키를 조회할경웅 KeyError 가 발생한다
# ↓와같은 try 구문으로 예외처리를 할수있따
try:
    print(a['key4'])
except KeyError:
    print('존재하지않는 키입니다 ')

# 예외처리를 하는 방법 외에도 다음과같이 키가 존재하는지 미리 확인해 이후 작업을 진행 할수도있다
if 'KEY4' in a:
    print('존재하는 키')
else:
    print('존재하지않는 키')

# 반복문을 활용하여 딕셔너리에있는 키/값 을 조회 하는 방법
for k,v in a.items():
    print(k,v)

# 딕셔너리의 키를 삭제하는 방법
del a['key1']

# 딕셔너리모듈
# 1. defaultdict 객체
# defaultdict 는 존재하지 않는 키를 조회 할경우 에러메시지를 출력하는 대신
# 디폴트값을 기준으로 해당키에 대한 딕셔너리 아이템을 생성해준다
b = collections.deafultdict(int)
b['A'] = 5
b['B'] = 4
b['C'] += 1
# 원래의 딕셔너리 라면 keyerror 가 발생하겠지만
# defaultdict 객체는 에러없이 디폴트인 0을 기준으로 자동 생성한후에 여기에 1을 더해 최종적으로 1이 만들어진다

# 2. counter 객체
# counter 객체는 아이템에 대한 개수를 계산하여 딕셔너리로 리턴하며 다음과같이 사용한다
c = [1,2,3,4,5,5,5,6,6]
d = collections.Counter(c)
# Counter d = ({5:3, 6:2, 1:1 ,2:2, 3:1, 4:1})
# 가장빈도수 높은 요소를 추출하기위해 d.most_common()을 사용할수있다
# d.most_common(2) -> [(5,3),(6,2)]

# 3. OrderedDict 객체
# 파이썬 3.6 이하 와 대부분의 언어에서는 해시테이블을 이용한 자료형은 입력순서가 유지 되지않는다
# 하지만 파이썬 3.6 이후의 버전 딕셔너리에서는 입력순서가 유지된다
# 그래서 입력순서가 유지된 딕셔너리를 이용하기 위하여 OrderedDict 을 사용한다

collections.OrderedDict({'ban': 3, 'apple': 4, 'pear': 1, 'orange': 2})
# OrderedDict([('ban': 3, 'apple': 4, 'pear': 1, 'orange': 2)])