Testing requirements:

- Python
- Pytest
- Requests
- Time (Built-in Python library)

To run the tests, execute the following command:

```
$ pytest -s
```

-s flag allows us to see the output of the tests in the console. The tests can be run multiple times in a row since each test restores the todo list to its original state.

The tests in the Performance_testing/experiment folder are performance tests. They test the performance of the application by measuring the time taken to either add, update or delete a todo instance as the number of todo instances increases.

The tests in the Performance_testing/unit_tests/todos folder are unit tests adapted from Part A of the project. They are the same tests as Part A except they have been adapted to also measure the time taken to add, update or delete a todo instance.

The results and the plots from Perfmon while the tests were running can be found under the folder Performance_testing/Perfmon_plots.



installation:

```
$ pip install pytest
```
```
$ pip install pytest-random-order
```
```
$ pip install requests
```
