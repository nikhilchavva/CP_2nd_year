# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")

def fun_applycaesarcipher(msg, shift):
	n=len(msg)
	result=""
	if(shift!=0):
		for i in range(n):
			orascii=ord(msg[i])
			if(orascii==32):
				ascii=orascii
			else:
				ascii=orascii+shift
				if(ascii>90 and ascii<97 and orascii<91):
					ascii=ascii-90+64
				elif(ascii<65):
					ascii=91-(65-ascii)
				elif(ascii>90 and ascii<97 and orascii>96):
					ascii=123-(97-ascii)
				elif(ascii>122):
					ascii=ascii-122+96
			result+=chr(ascii)
		
	return result



