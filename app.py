import torch
from model import Sentiment
from flask import request
import flask
import os
from flask import Flask, render_template, request
from tensorflow import keras
import random


# Tokenizer / model
from transformers import BertTokenizer, BertForSequenceClassification, AdamW

tokenizer = BertTokenizer.from_pretrained("model/")
model = BertForSequenceClassification.from_pretrained("model/")

import os
import tensorflow as tf


from transformers import BertTokenizer, BertForSequenceClassification
import torch
import smtplib

import model

import torch
from transformers import BertForQuestionAnswering
import os
import tensorflow as tf

import torch
from transformers import BertTokenizer, BertForSequenceClassification, AdamW


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", pred="Please ask a question!")


@app.route("/predict", methods=["POST"])
def prediction():
    data = [request.form["question"]]

    name = [request.form["name"]]

    answer = model.Sentiment(data[0])

    return render_template(
        "predict.html",
        pred=f"{name} ...I think the answer is {answer} !?",
    )


if __name__ == "__main__":

    app.run(debug=True)
