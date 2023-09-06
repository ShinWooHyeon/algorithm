import sys
full_sentence=""
for sentence in sys.stdin: # ctrl+D 입력까지 모든 줄을 입력 받는다
    full_sentence+=sentence
 
result_sentence=full_sentence.split() # 다중 공백 제거 및 단어 별 리스트화 # 이미 공백은 제거된 상태

hr = '-' * 80
word_list = []
sentece=''
for word in result_sentence:
    if word =='<br>': #확인한 단어가 br이므로 지금까지 기록해둔 단어들을 출력한다 프린트 후 자동으로 개행되니까
        sentence = ' '.join(word_list)
        word_list=[]
        print(sentence)
    elif word == '<hr>':
        if word_list != []:
            sentence = ' '.join(word_list) 
            word_list=[]
            print(sentence)
        print(hr) #hr은 첫줄이든 첫줄 아니든 무조건 출력하니까

    else:
        word_list.append(word)
        sentence = ' '.join(word_list)
        if len(sentence) > 80:
            next_word = word_list.pop(-1)
            sentence = ' '.join(word_list)
            print(sentence)
            word_list=[next_word]
        
# while문 다돌면 마지막 문장이 있을거임
sentence= ' '.join(word_list)
print(sentence)