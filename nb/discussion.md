### Problem 1
#### (A): My codes explicitly extracts the author's name using file_name.split('_')[2]. But professor's code simplifies this with str(f).split('_')[-1][:-4], which may be more robust if filename patterns vary slightly. To improve the efficiency of my workflow, I can try to further breaking down my code into smaller, modular components, which allows me to test each part individually, making it easier to isolate issues without running the entire codebase. I can also implement logging at critical stages to capture intermediate data, which helps track progress and identify any points where the code deviates from expected behavior. When I encounter errors, I should learn to use incremental testing or setting breakpoints more efficiently to focus on specific sections, ensuring a targeted approach to debugging rather than re-running the entire code each time. 
#### (C): (dsan5400) (base) guochenxi@MacBook-Air-4 nb % pytest tests/
    ====================================================== test session starts =======================================================
    platform darwin -- Python 3.11.10, pytest-8.3.3, pluggy-1.5.0
    rootdir: /Users/guochenxi/Desktop/DSAN5400/assignment3/fall-2024-assignment-03-chenxiguo0/nb
    configfile: pytest.ini
    plugins: anyio-4.4.0
    collected 1 item                                                                                                                 

    tests/test_naive_bayes.py .                                                                                                [100%]

    ======================================================= 1 passed in 1.37s ========================================================

### Problem 2
#### (A): They are basically the same but there is one discrepency in the prediction for work indexed 6.
                                custom_predicted_author   sklearn_predicted_author
                  0                        0                         0
                  1                        0                         0
                  2                        0                         0
                  3                        1                         1
                  4                        0                         0
                  5                        0                         0
                  6                        0                         1
                  7                        1                         1
                  8                        1                         1
                  9                        0                         0

### Problem 3
#### (A): Created Naive Bayes: accuracy: 0.8, f1 score: 0.7916666666666666
####        Scikit-Learn Naive Bayes: acccuracy: 0.9, f1 score: 0.898989898989899
#### (B): In prediction for Kennedy's work, two classifiers performed both well and made no mistakes. But they both mistakenly assigned some of Johnson's work to Kennedy, though Scikit-Learn Naive Bayes classifier performed better and made fewer mistakes in this.
