class Solution:

	def run(self, n):
		#
		# Write your code below; return type and arguments should be according to the problem\'s requirements
		#
		roman_ms = [1000, 500, 100, 50, 10, 5, 1]
		roman_cs = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

		roman_mprevs = [900, 400, 90, 40, 9, 4, 0]
		roman_cprevs = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV', '']

		n_in_roman_alphabet = ""
		for i in range(len(roman_ms)):
			while n >= roman_ms[i]:
				n_in_roman_alphabet += roman_cs[i]
				n -= roman_ms[i]
			if n >= roman_mprevs[i] and n < roman_ms[i]:
				n_in_roman_alphabet += roman_cprevs[i]
				n -= roman_mprevs[i]
		
		return n_in_roman_alphabet
