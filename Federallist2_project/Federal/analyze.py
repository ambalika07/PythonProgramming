
def tokens_freq(all_tokens):
    """Returns a count of how many times a token occurs across all documents.

    Args:
        all_tokens (dict): tokens output from index.index_dir

    Returns:
        token_frequency (dict): A dictionary of {token: count}, where count
            is the count of all the occurences of token in a directory of files.
        """
    token_frequency={}
    for atoken in all_tokens:
        value=all_tokens[atoken]
        token_frequency[atoken]=len(value)
        
        
    return token_frequency
            
            


def token_most_occuring_file(token_name, all_documents, all_tokens):
    """Returns the path to the file that has the most occurances of token_name.

    Args:
        token_name (string): the token to lookup
        all_documents (dictionary): documents output from index.index_dir
        all_tokens (dictionary): tokens output from index.index_dir

    Returns:
        file_path (string): The path to the file in the directory where the
            input token_name occurs the most.
    """
    
    if not token_name in all_tokens:
        return "Token not present"
    
    value=all_tokens[token_name]
    occ_frequency={}
    max_occ_documents=[]
    max_occurence=0
    for occ in value:
        if occ[0] in occ_frequency:
            occ_frequency[occ[0]] = occ_frequency[occ[0]] +1
        else:
            occ_frequency[occ[0]] =1
        if max_occurence < occ_frequency[occ[0]]:
            max_occurence=occ_frequency[occ[0]]
            max_occ_documents=[]
            max_occ_documents.append(all_documents[occ[0]]['path'])
        elif max_occurence == occ_frequency[occ[0]]:
            max_occ_documents.append(all_documents[occ[0]]['path'])        
            
    
    return max_occ_documents

    
                             
                         
                         
                         
        
        
    
    