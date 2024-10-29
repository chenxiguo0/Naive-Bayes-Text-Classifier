import numpy as np
import pandas as pd
from nb.nb import NaiveBayes  

def test_nb_class():
    data = {
        'author': ['n', 'n', 'n', 'p','p'],
        'text': [
            'just plain boring',
            'entirely predictable and lacks energy',
            'no surprises and very few laughs',
            'very powerful',
            'the most fun film of the summer'
        ]
    }
    df = pd.DataFrame(data)
    
    nb = NaiveBayes(alpha=1.0)  
    nb.train(df)  

    # Expected priors and likelihoods based on manual calculations
    expected_priors = [0.6, 0.4]  
    expected_likelihoods = [
            [2/34, 2/34, 2/34, 2/34, 2/34, 3/34, 2/34, 2/34, 2/34, 2/34, 2/34, 2/34, 2/34, 
             1/34, 1/34, 1/34, 1/34, 1/34, 1/34, 1/34],  
            [1/29, 1/29, 1/29, 1/29, 1/29, 1/29, 1/29, 1/29, 1/29, 1/29, 2/29, 1/29, 1/29, 
             2/29, 3/29, 2/29, 2/29, 2/29, 2/29, 2/29]   
        ]
    
    # Assuming expected_likelihoods and nb.likelihoods are numpy arrays
    sorted_expected_likelihoods = [np.sort(np.array(expected_likelihood)) for expected_likelihood in expected_likelihoods]
    sorted_computed_likelihoods = [np.sort(nb.likelihoods[i]) for i in range(nb.likelihoods.shape[0])]

    # Test if the priors match expected values
    assert np.allclose(nb.priors, expected_priors, rtol=1e-2)
    
    # Test if the likelihoods match expected values
    #assert np.allclose(nb.likelihoods, expected_likelihoods, rtol=1e-2)
    for i in range(len(sorted_expected_likelihoods)):
        assert np.array_equal(sorted_computed_likelihoods[i], sorted_expected_likelihoods[i]), f"Likelihoods for author {i} do not match!"


    # Check that the sum of likelihoods for each class equals 1
    for i in range(nb.likelihoods.shape[0]):
        assert abs(sum(nb.likelihoods[i]) - 1) < 1e-2

# pytest tests/

