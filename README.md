# Movie-Review-Sentiment-Analysis
This code uses logistic regression to judge whether a movie review is positive or negative. 

Dict.txt : Contains a vocabulary of words and their indexes. We are considering words present only in this vocab.

Feature.py:
It takes in 8 input arguments. Run it using below command.

python feature.py train_data.tsv valid_data.tsv test_data.tsv dict.txt formatted_train.tsv formatted_valid.tsv formatted_test.tsv 1

The last parameter is the model to be considered. I am converting raw features into sparse feature vector. Model 1 uses value 1 for a word if it is atleast present once in the sentence and present in vocab. Otherwise ignored if not present in vocab.

Model 2 counts frequency of each word in review and if >3 then gives 0 weight to that word otherwise word 1.

After getting formatted output. We run lr.py using below command

python lr.py formatted_train.tsv formatted_valid.tsv formatted_test.tsv dict.txt train_out.labels test_out.labels metrics_out.txt 60

It takes 8 input arguments. the last one is the number of training epochs. 

