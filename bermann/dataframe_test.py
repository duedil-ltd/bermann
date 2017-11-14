import unittest

from pyspark.sql.types import StructType, StructField, StringType, IntegerType

from bermann.dataframe import DataFrame
from bermann.row import Row
from bermann.spark_context import SparkContext
from bermann.sql import SQLContext


class TestDataFrame(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sc = SparkContext()
        cls.sql = SQLContext(cls.sc)

    @unittest.skip("skipping until DataFrame support complete")
    def test_creation_from_list_of_dicts(self):
        df = self.sql.createDataFrame([
            {'a': 'a', 'b': 123},
            {'a': 'aa', 'b': 456}
        ])

        self.assertEqual(df.count(), 2)

    @unittest.skip("skipping until DataFrame support complete")
    def test_creation_from_rdd_of_rows(self):
        rdd = self.sc.parallelize([
            Row(a='a', b=123),
            Row(a='aa', b=456)
        ])

        df = self.sql.createDataFrame(rdd)

        self.assertEqual(df.count(), 2)

    def test_creation_from_rdd_of_tuples(self):
        input = [
            ('a', 123),
            ('aa', 456)
        ]

        schema = StructType([
            StructField('a', StringType()),
            StructField('b', IntegerType())
        ])

        df = self.sql.createDataFrame(input, schema)

        self.assertEqual(df.count(), 2)

    @unittest.skip("skipping until DataFrame support complete")
    def test_creation_from_rdd_of_tuples_no_schema_raises_exception(self):
        input = [
            ('a', 123),
            ('aa', 456)
        ]

        with self.assertRaises(Exception) as e:
            df = DataFrame(input)
        self.assertEqual(Exception, type(e.exception))

    def test_creation_from_dataframe(self):
        input = [
            {'a': 'a', 'b': 123},
            {'a': 'aa', 'b': 456}
        ]

        schema = StructType([
            StructField('a', StringType()),
            StructField('b', IntegerType())
        ])

        df = self.sql.createDataFrame(input, schema)

        df_2 = self.sql.createDataFrame(df)

        self.assertEqual(df_2.count(), 2)

    def test_schema_attr_returns_pyspark_schema(self):
        input = [
            ('a', 123),
            ('aa', 456)
        ]

        schema = StructType([
            StructField('a', StringType()),
            StructField('b', IntegerType())
        ])

        df = self.sql.createDataFrame(input, schema)

        self.assertEqual(df.schema, schema)

    def test_schema_returns_pyspark_schema(self):
        input = [
            ('a', 123),
            ('aa', 456)
        ]

        schema = StructType([
            StructField('a', StringType()),
            StructField('b', IntegerType())
        ])

        df = self.sql.createDataFrame(input, schema)

        df_schema = df.schema

        self.assertEqual(schema, df_schema)

    #TODO agg

    #TODO alias

    #TODO approxQuantile

    def test_cache_is_noop(self):
        input = [
            ('a', 123),
            ('aa', 456)
        ]

        schema = StructType([
            StructField('a', StringType()),
            StructField('b', IntegerType())
        ])

        df = self.sql.createDataFrame(input, schema)

        cached = df.cache()

        self.assertEqual(df, cached)

    #TODO checkpoint

    #TODO coalesce

    #TODO collect

    #TODO columns

    #TODO corr

    #TODO count

    #TODO cov

    #TODO createGlobalTempView

    #TODO createOrReplaceGlobalTempView

    #TODO createOrReplaceTempView

    #TODO createTempView

    #TODO crossJoin

    #TODO crosstab

    #TODO cube

    #TODO describe

    #TODO distinct

    #TODO drop

    #TODO dropDuplicates

    #TODO drop_duplicates

    #TODO dropna

    #TODO explain

    #TODO fillna

    #TODO filter

    #TODO first

    #TODO foreach

    #TODO foreachPartition

    #TODO freqItems

    #TODO groupBy

    #TODO groupby

    #TODO head

    #TODO hint

    #TODO intersect

    #TODO isLocal

    #TODO isStreaming

    #TODO join

    #TODO limit

    #TODO na

    #TODO orderBy

    #TODO persist

    #TODO printSchema

    #TODO randomSplit

    #TODO rdd

    #TODO registerTempTable

    #TODO repartition

    #TODO replace

    #TODO rollup

    #TODO sample

    #TODO sampleBy

    #TODO select

    #TODO selectExpr

    #TODO show

    #TODO sort

    #TODO sortWithinPartitions

    #TODO stat

    #TODO storageLevel

    #TODO subtract

    #TODO take

    #TODO toDF

    #TODO toJSON

    #TODO toLocalIterator

    #TODO toPandas

    #TODO union

    #TODO unionAll

    #TODO unpersist

    #TODO where

    #TODO withColumn

    #TODO withColumnRenamed

    #TODO withWatermark

    #TODO write

    #TODO writeStream
