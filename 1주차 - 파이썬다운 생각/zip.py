## 파이썬에서 관련 객체로 구성된 리스트를 많이 사용하는 사실은 쉽게 알 수 있다.
## 리스트 컴프리헨션을 사용하면 소스 리스트(source list)에 표현식을 적용하여 파생 리스트(derived list)를 쉽게 얻을 수 있다.
names = ['Cecilia', "Lise", 'Marie']
letters = [len(n) for n in names]

## 파생 리스트의 아이템과 소스 리스트의 아이템은 서로의 인덱스로 연관되어 있다. 따라서 두 리스트를 병렬로 순회하려면 소스 리스트인 names의 길이만큼 순회하면 된다.
longest_name = None
max_letters = 0
for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count
print(longest_name)

### names와 letters를 인덱스로 접근하면 코드를 읽기 어려워진다. enumerate를 이용하면 좀더 나아진다.
longest_name = None
max_letters = 0
for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count
print(longest_name)

### 위 코드를 좀 더 명료하게 하는 내장 함수 zip을 제공한다. 파이썬 3에서 zip은 지연 제너레이터로 이터레이터 두 개 이상을 감싼다. zip 제너레이터는 각 이터레이터로부터 다음 값을 담은 튜플을 얻어온다.
longest_name = None
max_letters = 0
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count
print(longest_name)

## 내장함수 zip을 사용할 때는 두가지 문제가 있다.
## 첫 번째는 파이썬 2에서 제공하는 zip이 제너레이터가 아니라는 점이다. 제공한 이터레이터를 완전히 순회해서 zip으로 생성한 모든 튜플을 반환한다. 이 과정에서 메모리를 많이 사용하여 프로그램이 망가지는 원인이 되기도 한다.
## 파이썬 2에서 매우 큰 이터레이터를 zip으로 묶어서 사용하려고 한다면 내장 모듈 itertools에 있는 izip을 사용해야 한다.
## 두 번째는 입력 이터레이터들의 길이가 다르면 zip이 이상하게 동작한다. 예를 들어 names에 다른 이름이 추가했지만 letters의 카운터를 업데이트하지않았다면 zip의 실행 결과는 예상치 못한 결과가 출력된다.
longest_name = None
max_letters = 0
names.append('Rosalind')
for name, count in zip(names, letters):
    print(name)
## >>> Cecilia
## >>> Lise
## >>> Marie
### Rosalind가 결과에 없다. zip은 감싼 이터레이터가 끝날 때까지 튜플을 계속 넘겨준다. 이 방식은 이터레이터의 길이가 같을 때는 제대로 동작한다.
