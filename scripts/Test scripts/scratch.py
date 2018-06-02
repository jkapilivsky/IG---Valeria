def isEnglish(characters):
    try:
        characters.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

print(isEnglish('slabiky, ale liší se podle významu'))
print(isEnglish('English'))
print(isEnglish('ގެ ފުރަތަމަ ދެ އަކުރު ކަ'))
print(isEnglish('how about this one : 通 asfަ'))
print(isEnglish('?fd4))45s&'))

