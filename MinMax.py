***
Task:

다음 프로그램을 작성하십시오
- 사용자로부터 숫자 목록을 입력받습니다. (사용자가 10 25 5 18 3과 같이 숫자를 공백으로 구분하여 입력한다고 가정할 수 있습니다.)
- 목록에서 가장 작은 숫자와 가장 큰 숫자를 찾습니다.
- 가장 작은 숫자와 가장 큰 숫자를 출력합니다.
***

inp = input()
new = inp.split()
conv = [int(x) for x in new]
conv.sort()
print("Smallest: "+conv[0])
print("Largest: "+conv[-1])
