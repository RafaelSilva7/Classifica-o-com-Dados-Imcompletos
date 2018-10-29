import weka.core.jvm as jvm 
jvm.start(packages=True)

from weka.classifiers import Classifier 

from weka.core.converters import Loader, Saver
print("Load operation") 
loader = Loader(classname="weka.core.converters.ArffLoader") 
data = loader.load_file("./Dataset/hepatitis.arff") 

#import weka.core.converters as converters 
#print("Load operation") 
#data = converters.load_any_file("./final_small_test.arff") 
#data.class_is_last() 
print(data) 

#Filter function 
from weka.filters import Filter 
print("Filter operation") 
remove = Filter(classname="weka.filters.unsupervised.attribute.RemoveUseless", options=["-M", "99.0"]) 
remove.inputformat(data) 
filtered = remove.filter(data) 
print(filtered)

#EM imputation function 
em = Filter(classname="weka.filters.unsupervised.attribute.ReplaceMissingValues") 
em.inputformat(filtered) 
em_imputed = em.filter(filtered) 
print(em_imputed) 
#weka.filters.unsupervised.attribute.EMImputation -N -1 -E 1.0E-4 -Q 1.0E-8 
#Saver arff to csv 
saver = Saver(classname="weka.core.converters.CSVSaver") 
saver.save_file(em_imputed, "./Dataset/hepatitis.csv") 
saver.save_file(filtered, "./Dataset/hepatitis_removed_useless.csv") 
#saver.save_file(data, "./Dataset/hepatitis_weka.csv") 

#converters.save_any_file("./final_small_em.csv") 
#converters.save_any_file("/some/where/else/iris.csv") 
#converters.save_any_file("/some/where/else/iris.csv") 


#cls =Classifier(classname="weka.classifiers.trees.J48") 




#print(cls) 
jvm.stop() 