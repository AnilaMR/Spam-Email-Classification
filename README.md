# Spam-Email-Classification

Overview

This repository contains a spam email classification model that identifies whether an email is spam or not. The model is trained using a dataset of email messages, and it leverages natural language processing techniques to make predictions.

Repository Contents

1.mail_data.csv: The dataset used for training and testing the model. Contains the email dataset with two columns - label and message. The label column indicates whether the email is spam or ham (not spam), and the message column contains the email text.

2.model.py: A Python script containing the final trained model and functions for loading the model, preprocessing input data, and making predictions.

3.spam classifier.ipynb: A comprehensive notebook that walks through the steps of:
                        Data loading and exploration,
                        Data preprocessing (cleaning, tokenization, vectorization),
                        Model training and tuning,
                        Model evaluation and testing,
                        Making predictions with the trained model
