from sklearn import tree
from sklearn import ensemble
from sklearn import gaussian_process
from sklearn import neighbors

dtc = tree.DecisionTreeClassifier()
rfc = ensemble.RandomForestClassifier()
gpc = gaussian_process.GaussianProcessClassifier()
knc = neighbors.KNeighborsClassifier()

# CHALLENGE - create 3 more classifiers...
# 1 
# 2
# 3

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


# CHALLENGE - ...and train them on our data
dtc = dtc.fit(X, Y)
rfc = rfc.fit(X, Y)
gpc = gpc.fit(X, Y)
knc = knc.fit(X, Y)

z = 41

prediction_dtc = dtc.predict([[190, 70, z]])
prediction_rfc = rfc.predict([[190,70,z]])
prediction_gpc = gpc.predict([[190, 70, z]])
prediction_knc = knc.predict([[190,70,z]])

# CHALLENGE compare their reusults and print the best one!

print(prediction_dtc)

print(prediction_rfc)

print(prediction_gpc)

print(prediction_knc)