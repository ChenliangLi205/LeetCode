import time

T1 = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
T2 = ['abcd', 'cxt', 'mn', 'bd', 'xy']
T3 = ["abc", "a", "b", ""]
T4 = ["cdbbfebebafbefc","ecbeaeddcce","aefeeddafccaedafddd","cbe","ececca","adcfdbdffcebfedadcb","edbfadcecbebfee","eabcb",
      "bdfedaedbaeacf","faabafbbbefdea","deccfdffacbebdefbfa","ffdf","fdbeabbec","cbcfeedaf","ecdbfdebbebffbbbb","ebee",
      "cfcdcbcfdacbdaaebfef","dafabedfa","babbdfcc","eadeafdbcdbbaefbbbbdc","faabad","eeeaecdbbacbedbaeabd","acfa",
      "eaaafeb","acef","dccaccfffedaabefccead","bacdbfe","fdfdafaa","bacecdff","cfadccadfdabbdcdaec","acbdfffdbcdfffbdbec",
      "afbcfefc","facaacffccecfff","af","aedcddabdddfdeafabfd","fafbfeacffbbbceebaedc","aabbbabddcadadda","eccca","fcafbdfb",
      "ffdadaeaebedec","ccfc","efaed","eebbb","dcafccfbbdfbddcfbefb","aaeeb","fcdd","ccccb","ddebebfdcdbaaf","beeeb",
      "edbfdabdcfb","cacfbf","bceacbdababbfca","ffb","fcba","bdfedbaafebbffcefece","bf","dbfbeabcecffdbcc","dccebefccbecf",
      "aaebfacdaaabfbcfacd","cb","edbbbfcdbefeabcfd","daabdcbadccfeffafa","cfafbcdfbdabfadddddff","cbfd","bcaa","dffbfebffedc",
      "ebcbfbaeadbbdfcaa","dcedebbcdfffabbac","dbedacddcec","badedda","beeeaaffcdadbdecaddc","dcdbcdbffeddcfea","dedbdecbca",
      "cbecacdcfcdcfbfeebdda","bebbacebbfacfbbbed","dc","cdddaedbfeaeebdbef","accbbd","bbafead","dcfba","efac","ffce","cfa","bac",
      "bdfdfecccfeadeafedee","eedddbefdaefbcbf","acedbeadaedfcdffebea","cc","cffbeebdedfdbf","fdeacddefadbdecbe","ccccedafdbedaeeb",
      "cfafddadadcfdbdfb","aadbbedecd","cadeffaaffdcaeeefdfbf","adcaaefbffdfaadedbbb","cbeebfeeddcfd","abfaaecdffbdfafe","fccbbae",
      "cefdee","cfdbfbabacafecc"]


def solution(words):
    if len(words) < 2:
        return 0
    words.sort(reverse=True, key=lambda x: len(x))

    def match(s1, s2):
        for char in s2:
            if char in s1:
                return False
        return True

    max_len = 0
    i = 0
    while i < len(words)-1:
        j = i + 1
        max_ = len(words[i]) * len(words[j])
        if max_ <= max_len:
            return max_len
        while j < len(words):
            w1, w2 = words[i], words[j]
            if not match(w1, w2):
                j += 1
                continue
            if len(w1) * len(w2) >= max_len:
                if j - i <= 2:
                    return len(w1) * len(w2)
                else:
                    max_len = len(w1) * len(w2)
                    break
            elif j-i <= 2:
                return max_len
            else:
                break
        i += 1
    return max_len


if __name__ == '__main__':
    t1 = time.time()
    print(solution(T4))
    print(time.time()-t1)
