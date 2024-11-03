class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence2 = sentence.split()
        if len(sentence2) == 1:
            return sentence2[0][0] == sentence2[0][-1] 
        for i in range(len(sentence2)-1):
            if sentence2[i][-1] != sentence2[i + 1][0]:
                return False
        if sentence2[-1][-1] != sentence2[0][0]:
            return False
        return True
