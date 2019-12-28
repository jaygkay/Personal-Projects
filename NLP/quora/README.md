## Kaggle's Quora Question Pairs 

#### Dataset
For the first personal project of NLP, _Quora Question Pairs_ data is selected.

It is not only a famous real-world-dataset for a NLP Data/AI/ML scientist, but is this challenging dataset to pre-process data, implement whole precedures, and create a model.

dataset to find (https://www.kaggle.com/c/quora-question-pairs)

### Challenges
It takes a week to end up with this first implementation. The most challenging point for me was to deal with multiple input data and gather them on one output.

### Approach
Even though it is the first version of the modeling (multiple inputs and concat them to a typical Deep Neural Network), next analysis will be implemented with other approaches espeically on the modeling.
- divide two inputs
- Tokenizers
- Word Embedding
- Input parameter to be decided
- Model to be built

### 1st version 
At the bottom of the anlaysis, 7 epochs with early-stopping is conducted since the training takes a long time.

However, more epoches without early-stopping will be implemented shortly

### 2nd version 
In the 2nd version of the analysis, finally got the result of 20 epochs trainings.

Howevoer, at the bottom, the loss and accuracy graph shows that the overfitting has happened while training, that's why early-stopping function at the first version stops 3 epoches on training.

In 3rd version, should work on dealing with the overfitting

### 3rd version
0.1 Dropout rate was utilized in 1st and 2nd version. As seen in the greaphs at the bottom, the overfitting has happened.

0.5 Dropout rate was utilized for the belief of removing the overfitting. However, the model still show that similar patterns that the models did in 1st and 2nd version. 

I can conclude that 1st version, which conducted an early-stopping function was the best trial using the parameters and the model that I have utilized through 1st to 3rd versions. 

I need new ways to build up the model. Probably, CNN, RNN, LSTM, or Transformer would work better than the Deep Neural Network that I used.

### 4th version
Simple implementing of XGBoost

### Future work
Future models would be selected for CNN, RNN, LSTM, and Transformer to develop the skill-sets to deal with them and to dive into fiding better solutions out.

