#remove duplicate characters
s = "programming"
result = ""

for ch in s:
    if ch not in result:
        result += ch

print(result)

#first non-repeating characrter
s = "swiss"

for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break

#reverse words
s = "Python is easy"
words = s.split()
words.reverse()
print(" ".join(words))

#counting vowels and consonants
s = "education"
vowels = "aeiou"
v = c = 0

for ch in s.lower():
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1

print("Vowels:", v, "Consonants:", c)

#palindrome
s = '123321'
#s = s.replace(" ", "").lower()

print(s == s[::-1])

#duplicate without set
arr = [1,2,3,2,4,1]
dup = []

for i in arr:
    if arr.count(i) > 1 and i not in dup:
        dup.append(i)

print(dup)

#character frequency
s = "banana"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(dict(sorted(freq.items(), key=lambda x: -x[1])))
