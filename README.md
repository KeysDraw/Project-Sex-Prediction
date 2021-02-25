# Project-Sex-Prediction

Use a decision tree and feed it some data about sizes from males and females, then give it some sample data to be evaluated by it.
Use multiple models, for the sake of trying out, try to find sample values that make that different models ouput different results.

## GaussianProcessClassifier
    -Abr. GP(C)
    -designed to solve regression and probabilistic classification problems
    -User manual: https://scikit-learn.org/stable/modules/gaussian_process.html#gaussian-process

## RandomForestClassifier
    -Abr. RF(C)
    -Builds multiple decision trees (->Forest) and merges them together. By merging RandomForests this achieves reduced variance in the results.
    -User manual: https://scikit-learn.org/stable/modules/ensemble.html#forest

## DecisionTreeClassifier
    -Abr. DT(C)
    -Creates a DecisionTree with option 'YES'/'NO', tries out the different result options on the dataset, improves the more data is feeded to the DT
    -User manual: https://scikit-learn.org/stable/modules/tree.html#tree

## NearestNeighboursClassifier
    -Abr. NN(C)
    -doesn't construct an internal module, stores instances of training data; becomes slow with bigger datasets
    -finds distances between a query and all examples in the data, selects the specified number of examples(K) closest to the query and...
        *in case of classification:
            -takes a majority vote on the most frequent label.
        *in case of regression:
            -averages the labels.
    -User manual: https://scikit-learn.org/stable/modules/neighbors.html#classification