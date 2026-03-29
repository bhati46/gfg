#User function Template for python3
class Solution:
	def removeVowels(self, s):
		# code here
		r=""
		x="aeiou"
		for i in s:
		    if i not in x:
		        r+=i
		return r