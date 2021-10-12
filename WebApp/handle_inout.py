import NERutils
import NERnetwork
import argparse
import numpy as np
from datetime import datetime
from keras.callbacks import EarlyStopping
import subprocess
import shlex
from keras.models import model_from_json

def load_test():
    word_dir = 'words.pl'
    vector_dir = 'vectors.npy'
    train_dir = 'data/train_sample.txt'
    dev_dir = 'data/dev_sample.txt'
    test_dir = 'data/test_sample.txt'
    test_file= 'token_test.txt'
    print( 'Loading data...')
    input_train, output_train, input_dev, output_dev, input_test, output_test, alphabet_tag, max_length = \
        NERutils.create_data(word_dir, vector_dir, train_dir, dev_dir, test_file)
    # Load nermodel saved
    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("savenermodel.h5")
    print("Loaded model from disk")

    print('Testing model...')
    predict_x=loaded_model.predict(input_test, batch_size=512) 
    answer=np.argmax(predict_x, axis=-1)
    #answer = loaded_model.predict_classes(input_test, batch_size=512)
    print("input", input_test)
    print(input_test.shape)

    print("output", output_test)
    print("output_train", output_train)
    print(output_train.shape)
    print("output_dev", output_dev)
    print(output_dev.shape)
    print("answer", answer)

    NERutils.predict_to_file(answer, output_test, alphabet_tag, 'out.txt',test_file)
    text_output=""
    list_word_test=NERutils.create_wordtest(test_file)
    #for i in range(len(list_word_test)):
    #    for j in range(len(list_word_test[i])):
    #        if (list_word_test[i][j]=="phi_trường") or (list_word_test[i][j]=="hoa"):
    #            text_output+=list_word_test[i][j] +" "
    #        else:
    #            temp_text = list_word_test[i][j]
    #            temp_arr = temp_text.split("_")
    #            if (len(temp_arr) < 3):
    #                temp_text = temp_text.replace("_", " ")
    #            text_output += temp_text + " "

    #print(text_output)
    #return text_output
    phone_list = ['iphone' , 'samsung', 'pixel', 'navo', 'huawei', 'mate', 'enjoy', 'vertu', 'vivo', 'xiaomi', 'redmi', 'mi', 'infinix', 'hot9', 'hot10', 'zero']
    for i in range(len(list_word_test)):
        for j in range(len(list_word_test[i])):
            temp_text = list_word_test[i][j]
            temp_arr = temp_text.split("_")
            if (len(temp_arr) > 2):
                text_output += temp_text + ", "
            elif (len(temp_arr) == 2):
                if (temp_arr[0].lower() in phone_list):
                    text_output += temp_text + ", "
                
    last_char_index = text_output.rfind(",")
    text_output = text_output[:last_char_index]
    print(text_output)
    return text_output


'''
# evaluate loaded model on test data
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
score = loaded_model.evaluate(input_test,output_test, verbose=0)
print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1] * 100))

# evaluate loaded model on test data, ADAM
loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
score = loaded_model.evaluate(input_test,output_test, verbose=0)
print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1] * 100))

'''
# Colourise - colours text in shell. Returns plain if colour doesn't exist.
def colourise(colour, text):
    if colour == "black":
        return "\033[1;30m" + str(text) + "\033[1;m"
    if colour == "red":
        return "\033[1;31m" + str(text) + "\033[1;m"
    if colour == "green":
        return "\033[1;32m" + str(text) + "\033[1;m"
    if colour == "yellow":
        return "\033[1;33m" + str(text) + "\033[1;m"
    if colour == "blue":
        return "\033[1;34m" + str(text) + "\033[1;m"
    if colour == "magenta":
        return "\033[1;35m" + str(text) + "\033[1;m"
    if colour == "cyan":
        return "\033[1;36m" + str(text) + "\033[1;m"
    if colour == "gray":
        return "\033[1;37m" + str(text) + "\033[1;m"
    return str(text)

# Highlight - highlights text in shell. Returns plain if colour doesn't exist.
def highlight(colour, text):
    if colour == "black":
        return "\033[1;40m" + str(text) + "\033[1;m"
    if colour == "red":
        return "\033[1;41m" + str(text) + "\033[1;m"
    if colour == "green":
        return "\033[1;42m" + str(text) + "\033[1;m"
    if colour == "yellow":
        return "\033[1;43m" + str(text) + "\033[1;m"
    if colour == "blue":
        return "\033[1;44m" + str(text) + "\033[1;m"
    if colour == "magenta":
        return "\033[1;45m" + str(text) + "\033[1;m"
    if colour == "cyan":
        return "\033[1;46m" + str(text) + "\033[1;m"
    if colour == "gray":
        return "\033[1;47m" + str(text) + "\033[1;m"
    return str(text)

