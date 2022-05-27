# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as f:

        #lines = f.readlines(), stripping all non-characters
        lines = [line.strip() for line in f]
        
    return lines


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    
    # empty list to populate count of each word with
    word_count_list = []
    
    #separation each line into separate word
    line_words = [li.split() for li in text]

    #Joining words in each line into one single word list
    word_list = [word for line_word in line_words for word in line_word]
    
    #Taking count of each word and append count to the word_count_list
    for word in word_list:
        word_count = word_list.count(word)
        word_count_list.append(word_count)
        
    #zipping with word names and return as dictionary  
    return dict(zip(word_list,word_count_list))