# bermann

A unit-testing library for PySpark.

Currently, Spark, and PySpark in particular, has little support for testing Spark job logic, particularly in a unit-test environment. If you want to test even the simplest RDD operations, you have to spin up a local Spark instance and run your code on that. This is overkill, and once you have a decent suite of Spark tests, really gets in the way of speedy tests.

### Where does Bermann come in?

Bermann essentially replicates Spark constructs, such as RDDs, DataFrames, etc, so that you can test your methods rapidly in pure Python, without needing to spin up an entire Spark cluster.

### Setup

Clone the repo, create a virtualenv, install the requirements, and you're good to go!

```bash
virtualenv bin/env
source bin/env/bin/activate
python setup.py install
```

Setuptools should mean you can install directly from GitHub, by putting the following in your requirements file:

```bash
git+git://github.com/oli-hall/bermann.git@<release version>#egg=bermann
```

### Testing

Bermann currently comes with unit-tests covering all the functions implemented so far. To run them, run:

```bash
> python -m unittest discover -p *_test.py
```

The next step will be to hook up coverage to these, and run them with a cleaner command, possibly through SetupTools' built-in test runner.

Ultimately, it'd be really ace to have this run integration tests against Spark itself, where it can run the same commands in Spark and in Bermann, ensuring that the output is the same. This not only would ensure that Bermann performs as expected, but would also catch updates/changes in Spark's behaviour.   

### Requirements

This has been tested with Python 2.7, but should be Python 3 compatible. More thorough testing will follow. It uses the `pyspark` and `py4j` Python libs, but requires no external services to run (that'd be kinda contrary to the spirit of the library!).

### Usage 

Currently, the library consists of only RDD/SparkContext support, but more will be coming soon, never worry! 

#### RDD

To use the Bermann RDD, import the RDD class, and initialise it with the starting state (a list). Then apply RDD operations as per Spark:

```python
> from bermann import SparkContext
>
> sc = SparkContext() 
>
> rdd = sc.parallelize([1, 2, 3])
> rdd.count()
3
> rdd.map(lambda x: x * x).collect()
[1, 4, 9]
```

This means if you have methods that take RDDs and modify them, you can now test them by creating Bermann RDDs in your tests, and pass those into the methods to be tested. Then, simply assert that the contents of the RDD are as expected at the end. Similarly, if you have a pre-existing Spark test class, that spins up a SparkContext for use in methods/jobs, replace this with the Bermann equivalent and everything should work fine!

#### DataFrame

DataFrames are currently in development, there will be an update soon with more.

### Where does the name come from?

The library is named after Max Bermann, a Hungarian engineer who first discovered that [spark testing](https://en.wikipedia.org/wiki/Spark_testing) could reliably classify ferrous material. 
