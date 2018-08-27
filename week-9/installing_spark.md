## Installing Spark

1. Download Apache Spark here

  http://spark.apache.org/downloads.html

2. Unzip the Spark zip file and move the folder to your home directory

3. Install Java Development Kit 8:

  Go [here](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
to install Java Development Kit 8. DO NOT install JDK 10, as this causes compatibility issues
with Spark

4. Change .bash_profile settings

  Now you need to change some variable settings in
your bash_profile. In your terminal, type "atom ~./bash_profile". Add these lines:

  export JAVA_HOME="$(/usr/libexec/java_home -v 1.8)"

  export SPARK_HOME=~/spark-2.3.1-bin-hadoop2.7

  export PATH=$SPARK_HOME/bin:$PATH

  export PYSPARK_PYTHON=python3

5. Install pyspark with PyPi

  Type "pip install pyspark" in your terminal

6. Test to see if your installation worked!

  Open a python session and run the following code

  ```python
  import pyspark
  sc = pyspark.SparkContext('local[*]')
  rdd = sc.parallelize(range(1,20),4)

  def double(number):
    return number *2

  multiply_rdd = rdd.map(double)
  print(multiply_rdd.collect())
  ```
