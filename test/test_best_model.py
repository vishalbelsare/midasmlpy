import numpy as np
import pandas as pd
import midasmlpy.date_functions as datef  # used to handle different frequencies of data and to create lags
import midasmlpy.sparse_group_lasso as sgl  # used to run the sparse group lasso and related functions
import unittest


# load data from xlsx files and create a dataframe

class Test_TestBestModel(unittest.TestCase):
    def setUp(self):
        """Load data and set common variables"""
        Predictors = pd.read_excel('user_guide/predictors-monthly.xlsx').to_numpy()
        Target = pd.read_excel('user_guide/recessions-quarterly.xlsx').to_numpy()
        Y_date = Target[:, 0]
        Y = Target[:, 1]
        X_date = Predictors[:, 0]
        X = Predictors[:, 1:]
        self.degree = 4
        output = datef.data_transform(Y, Y_date, X, X_date, x_lags=3, y_lags=0, horizon=0,
                                      degree=self.degree, standardize=True)

        # Assertions to verify the output matches expected output
        self.y = output['Y']
        self.x = output['X_tilde']

    def test_best_model1(self):
        """Testing binomial model"""
        # Expected output
        expected_alparse = 1.0
        expected_performance = 0.5
        expected_lambda = 0.193669
        expected_b0 = 0.0

        # Call the function
        output = sgl.best_model(x=self.x, y=self.y, group_size=self.degree, nlam=50, pmax=122, intr=False,
                                k_folds=2, disp_flag=False, alpha_values=3, alpha=None)

        # Assertions to verify the output matches expected output
        np.testing.assert_array_almost_equal(output['best_alsparse'], expected_alparse)
        np.testing.assert_array_almost_equal(output['best_performance'], expected_performance)
        np.testing.assert_array_almost_equal(output['best_lambda'], expected_lambda)
        np.testing.assert_array_almost_equal(output['b0'], expected_b0)


    def test_best_model2(self):
        """Testing gaussian model"""
        # Expected output
        expected_alparse = 1.0
        expected_performance = 0.137931
        expected_lambda = 0.387338
        expected_b0 = 0.0

        # Call the function
        output = sgl.best_model(x=self.x, y=self.y, group_size=self.degree, nlam=50, pmax=122, intr=False,
                                k_folds=2, disp_flag=False, alpha_values=3, alpha=None, family='gaussian')

        # Assertions to verify the output matches expected output
        np.testing.assert_array_almost_equal(output['best_alsparse'], expected_alparse)
        np.testing.assert_array_almost_equal(output['best_performance'], expected_performance)
        np.testing.assert_array_almost_equal(output['best_lambda'], expected_lambda)
        np.testing.assert_array_almost_equal(output['b0'], expected_b0)
        


if __name__ == '__main__':
    unittest.main()
