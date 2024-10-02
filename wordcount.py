#문장을 입력으로 받고, 각 단어가 반복 되는 숫자를 출력한다

sentence = input()
words = sentence.split()

wc = {}
for x in words:
	if x in wc:
		wc[x]+=1
	else:
		wc[x]=1

print(wc)
