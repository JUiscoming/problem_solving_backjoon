# Complexity

Complexity: 알고리즘의 성능을 나타내는 척도

## Time complexity: 알고리즘을 위해 필요한 **연산의 횟수**
- Big-O 표기법으로 시간 복잡도를 표현함. 가장 빠르게 증가하는 항만을 고려함.  
    |Big-O 표기|명칭|
    |--------|---|
    |O(1)|상수 시간|
    |O(logN)|로그 시간|
    |O(N)|선형 시간|
    |O(NlogN)|로그 선형 시간|
    |O(N^2)|이차 시간|
    |O(N^3)|삼차 시간|
    |O(N^K)|다항 시간|
    |O(2^N)|지수 시간|
- 시간 복잡도에서의 **연산**은 프로그래밍 언어에서 지원하는 사칙 연산, 비교 연산 등과 같은 기본 연산을 의미함.

O(N)인 알고리즘 예시:
```python
array = [3, 5, 1, 2, 4] # N = 5
summation = 0

for value in array:
    summation += value

print(summation)
```

O(N^2)인 알고리즘 예시:
```python
array = [3, 5, 1, 2, 4]

tmp = 0
for i in array:
    for j in array:
        tmp += i * j

print(tmp)
```

### 코딩 테스트에서 사용 가능한 시간 복잡도의 상한은 일반적으로 **O(N^3)**
- 코딩 테스트 문제에서 시간 제한은 일반적으로 1~5초 정도이다.
- 일반적으로 CPU의 clock은 1~3GHz이므로 초당 수행 가능한 명령어 수는 1G/s = 10^9/s로 가정할 수 있다.
- N = 1,000일 때, O(N^3)의 알고리즘의 경우 10^9번의 연산이 요구되고, 약 1초가 소요되므로 오답 판정을 받을 수 있다.
- 입력 크기에 대한 시간 복잡도 상한 예시  
    |입력 크기|시간 복잡도 상한|
    |----|----|
    |N = 500|O(N^3)|
    |N = 2,000|O(N^2)|
    |N = 100,000|O(NlogN)|
    |N = 10,000,000|O(N)|

## Space complexity: 알고리즘을 위해 필요한 **메모리**
- Time complexity와 동일하게, Big-O 표기법으로 시간 복잡도를 표현함. 가장 빠르게 증가하는 항만을 고려함. 

- C언어 integer 배열 기준으로 사용되는 메모리 예시
    |배열|메모리 크기|
    |---|---|
    |int a[1000]|4 KB|
    |int a[1000000]|4 MB|
    |int a[2000][2000]|16 MB|
- 코딩 테스트에서는 보통 메모리 사용량을 128 ~ 512 MB 정도로 제한함. 즉, 데이터 갯수가 1,000만 이상으로 넘어가지 않도록 알고리즘 설계가 필요함.