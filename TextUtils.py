def reverse_string(text):
    return text[::-1]

def is_palindrome(text):
    return True if text == text[::-1] else False

def count_vowels(text):
    try:
       return sum([1 for i in text if i in 'aeiouAEIOU' ])
    except Exception as e:
        return e

def remove_spaces(text):
    return text.strip()

def count_words(text):
    try:
        return sum([1 for i in text.split()])
    except Exception as e:
        return e

def capitalize_words(text):
    return text.title()

def get_char_frequency(text):
    try:
        return {i : text.count(i) for i in text}
    except Exception as e:
        return e

def remove_punctuation(text):
    try:
        for i in text:
            if i in r'! @ # $ % ^ & * ( ) - _ = + \ | [ ] { } ; : / ? . >':
                text = text.replace(i,'')
        return  text
    except Exception as e:
        return e

def find_longest_word(text):
    try:
        for i in text.split():
            if len(i) == max([len(i) for i in text.split()]):
                return i
            # break
    except Exception as e:
        return e

def replace_word(text, old, new):
    try:
        return text.replace(old,new)
    except Exception as e:
        return e

def compress_text(text):
    try:
        result = ''
        char = text[0]
        cnt = 1
        text = text.replace(' ', '')

        for i in range(1, len(text)):
            if text[i] == char:
                cnt += 1
            else:
                print(char, cnt)
                result += char + str(cnt)
                char = text[i]
                cnt = 1
        result += char + str(cnt)
        return result
    except Exception as e:
        return e
