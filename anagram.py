#!/usr/bin/env python3


def anagram(s1, s2):
    """Function checks if the words are anagrams, as an input receives 2 arguments, strings.
      Returns 0 if arguments are anagrams and if not return the minimum number of characters that have to be changed
       to become an anagram """

    d1 = {}
    d2 = {}

    for c in s1:
        tmp = d1.get(c, 0)
        d1[c] = tmp + 1

    for g in s2:
        tmp = d2.get(g, 0)
        d2[g] = tmp + 1

    if d1 == d2:
        return '0'

    else:
        for i in d1:
            if i in d2 and i in d1:
                x = d2[i]
                d2[i] -= d1[i]
                d1[i] -= x

    tmp1 = [d1[i] for i in d1]
    tmp2 = [d2[i] for i in d2]
    res_tmp = tmp1 + tmp2
    q = sum(res_tmp)
    return q


m = anagram('anaconda', 'anaconca')
print(m)