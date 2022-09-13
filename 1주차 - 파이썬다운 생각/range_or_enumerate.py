### range 보다는 enumerate를 사용하자
from random import randint
random_bits = 0
for i in range(64):
    if randint(0, 1):
        random_bits |= 1 << i
### 내장 함수 range는 정수 집합을 순회(iterate)하는 루프를 실행할 때 유용하다.

### 문자열의 리스트 같은 순회할 자료 구조가 있을 때는 직접 루프를 실행할 수 있다.
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print('%s is delicious' % flavor)

## 종종 리스트를 순회하거나 리스트의 현재 아이템의 인덱스를 알고 싶은 경우가 있다.
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('%d: %s' % (i + 1, flavor))

### 내장 함후 enumerate를 사용하면 더 읽기 편하게 만들 수 있다. enumerate는 지연 제너레이터(lazy generator)로 이터레이터를 감싼다. 이 제너레이터는 이터레이터에서 루프 인덱스와 다음 값을 한 쌍으로 가져와 넘겨준다.
for i, flavor in enumerate(flavor_list):
    print('%d: %s' % (i + 1, flavor))

## enumerate로 세기 시작할 숫자를 지정하면 코드를 더 짧게 만들 수 있다.
for i, flavor in enumerate(flavor_list, 1):
    print('%d: %s' % (i, flavor))