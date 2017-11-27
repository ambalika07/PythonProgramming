import re
import os
from itertools import groupby

def tokenize(text):
    """Makes a list of words in text and separates the words from punctuation.

    Args:
        text (string): A text string. An example would be a file.read() string.

    Returns:
        A list of words in text. Words are seperated from punctuation.
    """

    # these are all using re to clean text before we split it
    # separate quote marks from enclosed text
    text = re.sub('"', ' " ', text)
    # separate single quote marks from enclosed text
    text = re.sub("(\s+|^)'", " ' ", text)
    text = re.sub("'(\s+|$)", " ' ", text)
    # seperate parentheses from enclosed text
    text = re.sub('\((.*?)\)', ' ( \\ 1 ) ', text, flags = re.DOTALL)
    text = re.sub('\(', ' ( ', text)
    text = re.sub('\)', ' ) ', text)
    # seperate square brackets from enclosed text
    text = re.sub('\[', ' [ ', text)
    text = re.sub('\]', ' ] ', text)
    # seperate embedded dashes and ellipses from surrounding text
    text = re.sub('([.-]{ 2,})', ' \\1 ', text)
    # remove underscores from beginning and end of words
    text = re.sub('(\W|^)_(.)', '\\1 \\2', text)
    text = re.sub('(.)_(\W|$)', '\\1 \\2', text)
    # seperate any word final punctuation characters from text
    text = re.sub('(\w+)(\W+)(\s|$)', '\\1 \\2 \\3', text)
    # insert a period in place of two or more newlines
    # this way we will consider a paragraph break the end of a sentence.
    text = re.sub('\W?\n{2,}', ' . ', text)

    # finally! strip the whitespaces and use .split to return a list of words.
    token_list = text.strip().split()
    token_list = [x[0] for x in groupby(token_list)]  # removing cons dups
    return token_list


def index_file(filename):
    """Makes a dictionary or words with thier positions in the file.

    Args:
        filename (string): The fullpath to the file to read.

    Returns:
        tokens (dict): A dictionary of {token}:
            [list of positions where it occurs in the file]
        sentence_bounds (list): A list of positions of end of sentence
            punctuation in the fle.
    """

    sentence_final_punc = ['.', '?', '!']

    tokens = {} # tokens dictionary
    position = 0
    sentence_bounds = []

    # open file
    # use .read to return a string of contents
    with open(filename) as f:
        text = f.read()

    # tokenize will return a list of each token in file text
    for token in tokenize(text):
        if token in sentence_final_punc:
            sentence_bounds.append(position)
        if re.match('\W+$', token):
            continue
        # adds the token to the dictionary if it is not already a key
        if token not in tokens:
            tokens[token] = []
        # adds the position to the list of postions for this key
        tokens[token].append(position)
        # increment the position counter
        position += 1

    # return tokens dictionary and the sentence bound positions list
    return tokens, sentence_bounds


# YOUR CODE GOES HERE
# ----------------------------------------------------------------------------

def index_directory(path):
    """the file.

    Args:
        filename (string): The fullpath to the file to read.

    Returns:
        tokens (dict): A dictionary of {token}:
            [list of positions where it occurs in the file]
        sentence_bounds (list): A list of positions of end of sentence
            punctuation in the fle.
    """
    doc_num= 0
    tokens={}
    documents={}
    for root, directories, files in os.walk(path):
        for filename in files:
            filepath = os.path.join(root, filename)
            
            current_tokens, bounds = index_file(filepath)
            documents[doc_num]={'path':filepath  , 'bounds':bounds }
            
            for token in current_tokens:
                
                if not token in tokens:
                    tokens[token]=[]
                    
                tokens[token].extend([(doc_num, pos) for pos in current_tokens[token]])
            doc_num=doc_num+1

    # return tokens dictionary and the sentence bound positions list
    return documents, tokens


