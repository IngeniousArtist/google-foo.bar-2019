def solution(x):
	z = list(x)
	
	k = []
	for y in z:
		if ord(y)>96 and ord(y)<123:
			i = ord(y)-97
			j = 122-i
			k.append(chr(j))
		else:
			k.append(y)

	s = ''.join(k)
	return s

"""
TESTING
==================
a = solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
print(a)
b = solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
print(b)
"""
