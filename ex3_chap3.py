#this method accepts a list of string items and returns them in a sentence like
def sentence_items(my_list):
    my_sentence = ""
    item_counter = len(my_list)
    for item in range(item_counter):
        #when the list gets to the last item, insert the 'and'
        if item == (item_counter - 1): 
            my_sentence += 'and '+my_list[item]
        else:
            my_sentence += my_list[item] + ', '

    #return the created sentence 
    return my_sentence


#testing the function - you can change and add new values to the list to test
print(sentence_items(['apples', 'bananas', 'mangoes', 'plantain', 'cats', 'tofu', 'yummy', 'goo goo gaga']))