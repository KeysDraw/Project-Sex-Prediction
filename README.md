# Project-Sex-Prediction

Use a decision tree and feed it some data about sizes from males and females, then you give it some sample data to be evaluated by it.
Use multiple models, for the sake of trying out, try to find sample values that make that different models ouput different results.

## GaussianProcessClassifier
    -Abr. GP(C)
    -designed to solve regression and probabilistic classification problems

### Advantages
* The prediction interpolates the observations (at least for regular kernels)
* The prediction is probabilistic so that one can compute empirical confidence intervals and decide based on those if one should refit (online fitting, adaptive fitting) the prediction in some region of interest.