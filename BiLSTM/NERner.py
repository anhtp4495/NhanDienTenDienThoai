import NERutils
import NERnetwork
import argparse
import numpy as np
from datetime import datetime
from keras.callbacks import EarlyStopping
import subprocess
import shlex
from keras.models import model_from_json

from os import chdir, getcwd
wd=getcwd()



parser = argparse.ArgumentParser()
parser.add_argument("--word_dir", help="word surface dict directory")
parser.add_argument("--vector_dir", help="word vector dict directory")
parser.add_argument("--train_dir", help="training directory")
parser.add_argument("--dev_dir", help="development directory")
parser.add_argument("--test_dir", help="testing directory")
parser.add_argument("--num_lstm_layer", help="number of lstm layer")
parser.add_argument("--num_hidden_node", help="number of hidden node")
parser.add_argument("--dropout", help="dropout number: between 0 and 1")
parser.add_argument("--batch_size", help="batch size for training")
parser.add_argument("--patience", help="patience")
args = parser.parse_args()


'''
word_dir = args.word_dir
vector_dir = args.vector_dir
train_dir = args.train_dir
dev_dir = args.dev_dir
test_dir = args.test_dir
num_lstm_layer = int(args.num_lstm_layer)
num_hidden_node = int(args.num_hidden_node)
dropout = float(args.dropout)
batch_size = int(args.batch_size)
patience = int(args.patience)

'''
word_dir = 'words.pl'
vector_dir = 'vectors.npy'
train_dir = 'data/train.txt'
dev_dir = 'data/dev.txt'
test_dir = 'data/test.txt'
num_lstm_layer = 2
num_hidden_node = 10
dropout = 0.2
batch_size = 512
patience = 10

startTime = datetime.now()

print( 'Loading data...')
input_train, output_train, input_dev, output_dev, input_test, output_test, alphabet_tag, max_length = \
    NERutils.create_data(word_dir, vector_dir, train_dir, dev_dir, test_dir)
print( 'Building model...')
time_step, input_length = np.shape(input_train)[1:]
output_length = np.shape(output_train)[2]
ner_model = NERnetwork.building_ner(num_lstm_layer, num_hidden_node, dropout, time_step, input_length, output_length)
print( 'Model summary...')
print( ner_model.summary())
print( 'Training model...')
early_stopping = EarlyStopping(patience=patience)
history = ner_model.fit(input_train, output_train, batch_size=batch_size, epochs=1000,
                        validation_data=(input_dev, output_dev), callbacks=[early_stopping])
'''
print( 'Testing model...')
answer = ner_model.predict_classes(input_test, batch_size=batch_size)
NERutils.predict_to_file(answer, output_test, alphabet_tag, 'out.txt')
input = open('out.txt')
#p1 = subprocess.Popen(["perl","vie-ner-lstm-master/conlleval.pl"], stdin=input)
#p1.wait()
'''
# evaluate the nermodel
scores = ner_model.evaluate(input_train, output_train, verbose=0)
print("%s: %.2f%%" % (ner_model.metrics_names[1], scores[1]*100))

endTime = datetime.now()
print( "Running time: ")
print (endTime - startTime)


#Save nermodel
# serialize nermodel to JSON
model_json = ner_model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
ner_model.save_weights("save_Nermodel.h5")
print("Saved model to disk")



'''
#Load nermodel saved
# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("savenermodel.h5")
print("Loaded model from disk")


# evaluate loaded model on test data
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
score = loaded_model.evaluate(X, Y, verbose=0)
print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1] * 100))

'''

