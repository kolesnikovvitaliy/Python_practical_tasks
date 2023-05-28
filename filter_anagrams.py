def filter_anagrams(word, anagrams):
    return [i for i in anagrams if sorted(i) == sorted(word)]
#print(filter_anagrams('abcd', ['ajcd']))
print(filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))
#if sorted(i) == sorted(j[0]):


