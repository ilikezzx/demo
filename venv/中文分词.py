import os

sentence = '人类失去联想,世界将会怎样'
wordList=[',','人类','失去','联想','世界','会','会怎样','将会','将','怎样','人']

# 前向判定
def forward(sentence,maxLen):
    sentenceLen=len(sentence)
    ansParticiple = []

    beforeIndex = 0 # 初始未匹配位置
    while beforeIndex < sentenceLen:
        j=min(beforeIndex+maxLen, sentenceLen)  # 防止字符串过长复杂度过大，设置每个单词最大长度
        for endj in range(j,beforeIndex,-1):
            words = sentence[beforeIndex:endj]
            if words in wordList:               # 依次判定，直到有单词满足条件
                ansParticiple.append(words)
                beforeIndex = endj
                break

    return ' | '.join(ansParticiple)


def backward(sentence,maxLen):
    sentenceLen=len(sentence)
    ansParticiple = []

    beforeIndex = sentenceLen -1 # 初始未匹配位置
    while beforeIndex >= 0:
        j=max(beforeIndex-maxLen+1, 0)  # 防止字符串过长复杂度过大，设置每个单词最大长度

        for endj in range(j,beforeIndex+1):
            words = sentence[endj:beforeIndex+1]
            if words in wordList:               # 依次判定，直到有单词满足条件
                ansParticiple.append(words)
                beforeIndex = endj - 1
                break

    ansParticiple.reverse()
    ansParticipleList = ansParticiple # 解决颠倒出现None的问题
    return ' | '.join(ansParticipleList)


if __name__ == '__main__':
    ansParticiple1 = forward(sentence=sentence,maxLen=3)
    ansParticiple2 = backward(sentence=sentence,maxLen=3)
    print("正向分词结果:",ansParticiple1)
    print("逆向分词结果:",ansParticiple2)