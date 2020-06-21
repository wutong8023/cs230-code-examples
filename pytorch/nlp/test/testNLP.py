import unittest
import nlp


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # Print all the available datasets
        print([dataset.id for dataset in nlp.list_datasets()])

        # Load a dataset and print the first examples in the training set
        squad_dataset = nlp.load_dataset('squad')
        print(squad_dataset['train'][0])

        # List all the available metrics
        print([metric.id for metric in nlp.list_metrics()])

        # Load a metric
        squad_metric = nlp.load_metric('squad')
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
