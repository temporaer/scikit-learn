from ..base import ClassifierMixin
from .base import BaseMLP
from ..preprocessing import LabelBinarizer


class MLPClassifier(BaseMLP, ClassifierMixin):
    """ Multilayer Perceptron Classifier.

    Uses a neural network with one hidden layer.


    Parameters
    ----------


    Attributes
    ----------

    Notes
    -----

    See also
    --------
    MLPRegressor

    References
    ----------"""

    def fit(self, X, y, max_epochs, shuffle_data):
        self.lb = LabelBinarizer()
        one_hot_labels = self.lb.fit_transform(y)
        super(MLPClassifier, self).fit(
                X, one_hot_labels, max_epochs,
                shuffle_data)
        return self

    def predict(self, X):
        prediction = super(MLPClassifier, self).predict(X)
        return self.lb.inverse_transform(prediction)
