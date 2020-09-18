
def calculate_average_length(sentences):
    if len(sentences)==0:
        return 0.0
    sum_sentence=0
    for sentence in sentences:
        length_of_sentence=len(sentence)
        sum_sentence=sum_sentence+length_of_sentence #right side evaluated/calculated first
    return sum_sentence/len(sentences)
        






