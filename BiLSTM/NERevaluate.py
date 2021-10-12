import conlleval1
#from conlleval import evaluate_conll_file

print(conlleval1.evaluate_conll_file("vie-ner-lstm-master/out.txt"))
# print out the table as above
#evaluate(true_tags, pred_tags, verbose=True)

# calculate overall metrics
#prec, rec, f1 = evaluate(true_tags, pred_tags, verbose=False)
