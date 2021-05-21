import graphviz
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
iris = load_iris()
classifier = DecisionTreeClassifier(max_leaf_nodes=3)
classifier.fit(iris.data, iris.target)
dot_data = tree.export_graphviz(classifier, out_file=None, feature_names=iris.feature_names, class_names=iris.target_names)
graph = graphviz.Source(dot_data)
graph.render("iris")