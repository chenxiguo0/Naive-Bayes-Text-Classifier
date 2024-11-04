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
#### (E): Documents containing 'system': [('3', 1), ('5653', 1), ('1127', 1), ('3319', 3), ('8935', 1), ('2552', 2), ('16515', 1), ('14398', 1), ('16638', 1), ('8772', 2)]
    The search has ignored case sensitivity, ensuring that both "system" and "System" yield results.
#### (F): Documents containing 'compatibility': [('14398', 1), ('8772', 1)]
    Like the previous query, case insensitivity was also secured here. In my codes, I avoided stemming 'compatibility' because after stemming it's altered and couldn't be found by searching.
#### (G): Documents containing both 'system' and 'compatibility': [('14398', 1)]
    The intersection of results from the two individual queries successfully yielded documents that contain both terms.

