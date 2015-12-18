
中文汉字匹配：
pattern=re.compile(u"[\u4e00-\u9fa5]")
words="中文"
re.match(pattern, str(words).decode('utf8'))

中文标点符号匹配：
#省略号……及......、感叹号！、问号？、顿号、、句号。、中括号
pattern=re.compile(u"((…{2})|(.{6})|[！？、。【】])+")
words='……！？、。【】'
re.match(pattern,words.decode('utf8'))