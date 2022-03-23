def get_words(file):
    with open(file, 'r')as f:
        dict_list = f.readlines()
    for index in range(len(dict_list)):
        dict_list[index] = dict_list[index][:-1]
    return dict_list

def show_words(word_list):
    word_per_row = 20
    count = 0
    for word in word_list:
        if count < word_per_row:
            print(word, end=' ')
            count = count+1
        else:
            print(word)
            count = 0

def start_new_game():
    dataset = get_words('dataset.txt')
    valid_word_list = dataset
    green = ['', '', '', '', '']
    yellow = []
    black = []
    print("=================================")
    print("Start a new game, choose a word:")
    show_words(valid_word_list)
    while(True):
        word = ''
        result = ''
        while len(word) != 5:
            word = input('\nYou choose the word: ')
        while len(result) != 5:
            result = input('Result is (Green:G, Yellow:Y, Black:B):')
            
        if result.upper()=='GGGGG':
            break
        #print('38')
        for index in range(5):
            result_char = result[index].upper()
            word_char = word[index].upper()
            if result_char == 'G':
                green[index] = word_char
            elif result_char == 'Y':
                yellow.append(word_char)
            elif result_char == 'B':
                black.append(word_char)
            else:
                print('error')
        #print(green)
        #print(yellow)
        #print(black)
        #print()
        for index in range(5):
            if green[index]!='':
                temp = []
                for word in valid_word_list:
                    if word[index].upper()==green[index]:
                        temp.append(word)
                valid_word_list = temp
        #print(valid_word_list)
        for char in yellow:
            temp = []
            for word in valid_word_list:
                if char in word.upper():
                    temp.append(word)
            valid_word_list = temp
        #print(valid_word_list)
        for char in black:
            temp = []
            for word in valid_word_list:
                if char not in word.upper():
                    temp.append(word)
            valid_word_list = temp
        print("Avalible words are:")
        show_words(valid_word_list)

if __name__=="__main__":
    
    while(True):
        start_new_game()
        
        
    import os
    os.system("PAUSE")
