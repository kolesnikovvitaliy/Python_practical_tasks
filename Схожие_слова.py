def схожие_слова(word, lst, vowels):
    word_index = [i for i, ltr in enumerate(word) if ltr in vowels]
    return "\n".join([lst[j] for j in range(len(lst)) if word_index == [i for i, ltr in enumerate(lst[j]) if ltr in vowels]])
    
vowels = 'ауоыиэяюёе'
word = input()
lst = [input() for _ in range(int(input()))]
print(схожие_слова(word, lst, vowels))