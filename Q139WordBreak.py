import time

T0 = ("catsandog", ["cats", "dog", "sand", "and", "cat"])
T1 = ("applepenapple", ["apple", "pen"])
T2 = ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
      ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
T3 = ("a", ["b"])


def solution(s, wordDict):
    target = len(s)
    accessable = set()
    for word in wordDict:
        if s.startswith(word):
            accessable.add(len(word))
    while len(accessable):
        if target in accessable:
            return True
        newSet = set()
        for word in wordDict:
            for access in accessable:
                if access+len(word) in accessable:
                    continue
                if len(word) <= target-access+1:
                    if s[access: access+len(word)] == word:
                        newSet.add(access+len(word))
        accessable = newSet
    return False


if __name__ == '__main__':
    t1 = time.time()
    head = solution(*T3)
    print(head)
    print(time.time()-t1)
