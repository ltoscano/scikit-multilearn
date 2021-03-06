import unittest

from skmultilearn.ensemble.rakeld import RakelD
from skmultilearn.problem_transform.lp import LabelPowerset
from skmultilearn.tests.classifier_basetest import ClassifierBaseTest
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.datasets import make_multilabel_classification
from sklearn.cross_validation import train_test_split
from sklearn.utils.estimator_checks import check_estimator


class RakelDTest(ClassifierBaseTest):

    def get_labelpowerset_with_svc(self):
        return LabelPowerset(classifier=SVC(), require_dense=[False, True])

    def get_labelpowerset_with_nb(self):
        return LabelPowerset(classifier=GaussianNB(), require_dense=[True, True])

    def test_if_sparse_classification_works_on_non_dense_base_classifier(self):
        classifier = RakelD(
            classifier=self.get_labelpowerset_with_svc(), labelset_size=3)

        self.assertClassifierWorksWithSparsity(classifier, 'sparse')

    def test_if_dense_classification_works_on_non_dense_base_classifier(self):
        classifier = RakelD(
            classifier=self.get_labelpowerset_with_svc(), labelset_size=3)

        self.assertClassifierWorksWithSparsity(classifier, 'dense')

    def test_if_sparse_classification_works_on_dense_base_classifier(self):
        classifier = RakelD(
            classifier=self.get_labelpowerset_with_nb(), labelset_size=3)

        self.assertClassifierWorksWithSparsity(classifier, 'sparse')

    def test_if_dense_classification_works_on_dense_base_classifier(self):
        classifier = RakelD(
            classifier=self.get_labelpowerset_with_nb(), labelset_size=3)

        self.assertClassifierWorksWithSparsity(classifier, 'dense')

    def test_if_works_with_cross_validation(self):
        classifier = RakelD(
            classifier=self.get_labelpowerset_with_nb(), labelset_size=3)

        self.assertClassifierWorksWithCV(classifier)

if __name__ == '__main__':
    unittest.main()
