def is_vowel_character(c) -> bool:
	return c == 'o' or c == 'e' or c == 'u' or c == 'a' or c == 'i'

def count_vowel_character():
	t = int(input())
	for _ in range(0, t):
		count = 0
		s = input()
		s = s.lower()
		for i in range(0, len(s)):
			count += 1 if is_vowel_character(s[i]) else 0
		print(count)

if __name__ == '__main__':
	count_vowel_character()