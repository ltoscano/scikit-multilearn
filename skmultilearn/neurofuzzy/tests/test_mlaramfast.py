import unittest

from skmultilearn.neurofuzzy.MLARAMfast import MLARAM
from skmultilearn.tests.classifier_basetest import ClassifierBaseTest
from sklearn.datasets import make_multilabel_classification
from sklearn.cross_validation import train_test_split
from sklearn.utils.estimator_checks import check_estimator

class MLARAMTest(ClassifierBaseTest):
    #def test_if_sparse_classification_works_on_non_dense_base_classifier(self):
    #    classifier = (classifier = SVC(), require_dense = [False, True])
    #    self.assertClassifierWorksWithSparsity(classifier, 'sparse')

    #def test_if_dense_classification_works_on_non_dense_base_classifier(self):
    #    classifier = MLARAM(require_dense =  True)

    #    self.assertClassifierWorksWithSparsity(classifier, 'dense')

    #def test_if_sparse_classification_works_on_dense_base_classifier(self):
    #    classifier = ClassifierChain(classifier = GaussianNB(), require_dense = [True, True])

    #    self.assertClassifierWorksWithSparsity(classifier, 'sparse')

    def test_if_dense_classification_works_on_dense_base_classifier(self):
        classifier = MLARAM(require_dense =  True)

        self.assertClassifierWorksWithSparsity(classifier, 'dense')

if __name__ == '__main__':
    unittest.main()
