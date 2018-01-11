# coding=utf-8
# \b:单词边界,只表示边界不代表空格，使用raw原始字符串
# \B:非单词边界
import re
print(re.match("\\w+\\s\\bve\\b","ho ve r"))
print(re.match(r"\w+\s\bve\s\b","ho ve r"))
print(re.match(r"\w+\Bve\B","hover"))


# <_sre.SRE_Match object; span=(0, 5), match='ho ve'>
# <_sre.SRE_Match object; span=(0, 6), match='ho ve '>
# <_sre.SRE_Match object; span=(0, 4), match='hove'>