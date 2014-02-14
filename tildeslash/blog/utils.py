# -*- coding: utf-8 -*-
import re
import unicodedata


# FIXME: these patterns works for English/Chinese mixed content, but not tested among other languages
WORD_COUNT_SPLIT_PATTERN = re.compile(u'[\s\u4e00-\u9fff]')
ASIAN_CHAR_PATTERN = re.compile(u'[\u4e00-\u9fff]')
ENDING_CHAR_CATEGORIES = ('Po', 'Cc', 'Zs')


def word_count(content):
    return len(re.split(WORD_COUNT_SPLIT_PATTERN, content))


def strip_content(content, length=100):
    index = 0
    count = 0
    for c in content:
        if count >= length:
            if unicodedata.category(c) in ENDING_CHAR_CATEGORIES:
                break
        else:
            if re.match(ASIAN_CHAR_PATTERN, c):
                count += 2
            else:
                count += 1
        index += 1
    return content[:index]