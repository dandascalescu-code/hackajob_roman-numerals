class Solution:

	def run(self, n):
		#
		# Write your code below; return type and arguments should be according to the problem\'s requirements
		#
		roman_numerals = {
			1000: 'M',
			900: 'CM',
			500: 'D',
			400: 'CD',
			100: 'C',
			90: 'XC',
			50: 'L',
			40: 'XL',
			10: 'X',
			9: 'IX',
			5: 'V',
			4: 'IV',
			1: 'I'
		}

		n_in_roman_alphabet = ""
		for value in roman_numerals.keys():
			while n >= value:
				n_in_roman_alphabet += roman_numerals[value]
				n -= value
		
		return n_in_roman_alphabet
