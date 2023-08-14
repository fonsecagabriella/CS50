import nltk
import sys
import os
import string
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1

def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """

    mapping_files = {} #start dict to return


    for file in os.listdir(directory): # for each file in the folder
        file_path = os.path.join(directory, file) # full path for the file
        file_name = os.path.splitext(file)[0] #treat file name to remove .txt

        #print(file_name)

        with open(file_path, 'r') as file: #read content of the file
            file_content = file.read()

            #saves to dictionary
            mapping_files[file_name] = file_content

    return mapping_files


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """

    words =  nltk.word_tokenize(document.lower()) # convert sentence to lower case and split it to list of words using tokenize

    # filter out punctuation
    words = [ word for word in words if word not in string.punctuation ]

    # filter out English stopwords
    words = [ word for word in words if word not in nltk.corpus.stopwords.words("english")]

    return words


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """

    all_words = {} #create dict that will store all words and the documents in order which they appear

    # term frequency
    #for document in documents:
    #    for word in documents[document]:
    #        if word in all_words:
    #            all_words[word] += 1
    #        else:
    #            all_words[word] = 1


    for document in documents: #iterates over all documents
        for word in documents[document]: # for each word in a given document
            if word in all_words: #checks if word is already in all words
                all_words[word] +=1  #if so, add the current document as the set in in the word appears
            else:
                all_words[word] = 1# if not, adds word to the all_words dict, initialise the set and adds current document


    # calculate idf by checking the len of set for each word
    idfs = {}

    for word in all_words:
        # idf = log (total_documents / num_documents_containing_word )
        x = len(documents) / all_words[word]
        idfs[word] = math.log(x)

    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the `n` top
    files that match the query, ranked according to tf-idf.
    """


    tf_idf_list = [] # create list to store tf_idf of a file + sum of all tf_idfs of words in that file

    for file in files:
        tf_idf = 0 #starts the value of tf_idf for this file
        for word in query: # iterates over all words in a file
            if word in files[file]: # if the word is in the given query
                tf_idf += files[file].count(word) * idfs[word] # calculate their tf_idf by multiplying how many times word appears in doc by their idf

        if not tf_idf == 0: #if words didn't appear in the file, don't add file to the list
            tf_idf_list.append((file, tf_idf)) # adds file and total tf_idf to the list

    sorted_tf_idf = sorted(tf_idf_list, key=lambda x: x[1]) #sorted the list based on the value j of tupple tf_idf_list(i, j)

    #print(tf_idf_list)
    return [filenames[0] for filenames in sorted_tf_idf[:n]] #return the n first values in the sorted list



def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    #print(f"query: {query}")
    #print(f"sentences: {sentences}")
    #print(f"idfs: {idfs}")
    #print(f"n: {n}")


    sentence_idf_qtf = {} #create a dict to store tupple (idf, qtf) for each sentence

    for sentence in sentences: #for each word in query
        for word in query: # for each sentence in sentences
            if word in sentences[sentence]: # if query word is in the sentence
                if sentence in sentence_idf_qtf: # check if query word is already in the dict to return, # if so, update their values
                    new_idf = sentence_idf_qtf[sentence][0] + idfs[word] #update value of idf
                    new_qtf = sentence_idf_qtf[sentence][1] + 1 #update value of qtf
                    sentence_idf_qtf[sentence] = (new_idf, new_qtf)

                else: # if not, create new entry in the dic
                    sentence_idf_qtf[sentence] = (idfs[word], sentences[sentence].count(word))

        if sentence in sentence_idf_qtf: #updates value of qtf, by dividing the frequency by lenght of sentence
            new_qtf = sentence_idf_qtf[sentence][1] / len(sentence)
            sentence_idf_qtf[sentence] = (sentence_idf_qtf[sentence][0], new_qtf)

    #sorted the list based first on value of idf then on value of qtf
    sorted_sentence_idf_qtf = sorted(sentence_idf_qtf.items(), key=lambda sentence:(sentence[1][0], sentence[1][1]), reverse=True)

    #print(f"SORTED: {sorted_sentence_idf_qtf}")

    # returnt the first n sentences
    return [s[0] for s in sorted_sentence_idf_qtf[:n]]



if __name__ == "__main__":
    main()
