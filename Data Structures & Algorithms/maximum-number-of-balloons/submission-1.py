class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

    #Solution if we have mix of unicode , upper and lower case characters
        count = {}
        for c in text:
            count[c] = count.get(c,0)+1
        return min(
            count.get('b',0),
            count.get('a',0),
            count.get('l',0)//2,
            count.get('o',0)//2,
            count.get('n',0)
        )
    '''
    #solution if all characters in text is lowercase alphabets
        count = [0] * 26
        for c in text:
            count[ord(c)-ord('a')] +=1
        return min(
            count[ord('b')-ord('a')],
            count[ord('a')-ord('a')],
            count[ord('l')-ord('a')]//2,
            count[ord('o')-ord('a')]//2,
            count[ord('n')-ord('a')]
        )
'''