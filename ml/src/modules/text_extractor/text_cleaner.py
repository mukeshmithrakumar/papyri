import re
import unicodedata


def join_text(raw_text):
    """Function to Join paragraphs together"""
    joined_text = []
    line = ''
    for i in range(len(raw_text)):
        if (len(raw_text[i]) > 1) and (raw_text[i][-1] == '\n'):
            line += raw_text[i]
        if (raw_text[i] == '\n'):
            joined_text.append(line)
            line = ''
    return joined_text


def remove_non_ascii(word):
    """Remove non-ASCII characters from list of tokenized words"""
    return unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')


def remove_punctuation(word):
    """Remove punctuation from list of tokenized words"""
    return re.sub(r'[^\w\s]', '', word)


def cleaner(text_path):
    with open(text_path, 'r', encoding='utf-8') as file:
        _text = file.readlines()
    file.close()

    # Call the function to join the paragraph texts together.
    raw_text = join_text(_text)

    for line in range(len(raw_text)):

        # Remove numbers
        raw_text[line] = re.sub(r'[0-9]', ' ', raw_text[line])

        # Remove non asciii characters
        raw_text[line] = ' '.join(map(remove_non_ascii, raw_text[line].split()))

        # Remove punctuation
        raw_text[line] = ' '.join(map(remove_punctuation, raw_text[line].split()))

        # Remove extra whitespace
        raw_text[line] = re.sub(r'\s+', ' ', raw_text[line])

        # Remove extra whitespace
        raw_text[line] = raw_text[line].lstrip()

        # Find abstract line number
        abstract_string = 'abstract'
        if re.match(abstract_string, raw_text[line], flags=re.IGNORECASE):
            top = line

        # Find reference line number
        reference_string = 'references'
        if re.match(reference_string, raw_text[line], flags=re.IGNORECASE):
            bottom = line

    return list(filter(None, raw_text[top:bottom]))
