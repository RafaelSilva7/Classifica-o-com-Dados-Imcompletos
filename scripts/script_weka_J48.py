import weka.core.jvm as jvm
import weka.core.converters as conv
from weka.classifiers import Evaluation, Classifier
from weka.core.classes import Random
import weka.plot.classifiers as plcls
import os

jvm.start(packages=True)
data = conv.load_any_file("Dataset/test.arff")
#print(data)

data.class_is_last()
cls = Classifier(classname="weka.classifiers.trees.J48", options=["-C", "0.3"])
evl = Evaluation(data)
evl.crossvalidate_model(cls, data, 15, Random(1))

#print(evl.summary("=== J48 on anneal (stats) === Rafael Manja", False))
#print(evl.matrix("Matriz do Rafael"))
plcls.plot_classifier_errors(evl.predictions, absolute=False, wait=True)
jvm.stop()