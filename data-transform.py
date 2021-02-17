customer_df # Pandas DataFrame with customer data

split_email = customer_df.email.str.split("@", expand=True)

customer_df = customer_df.assign(  
    username=split_email[0],  domain=split_email[1],
    )


#spark

import pyspark.sqlspark = pyspark.sql.SparkSession.builder.getOrCreate()
spark.read.jdbc("jdbc:postgresql://localhost:5432/pagila","customer",                
properties={"user":"repl","password":"password"})


customer_df 
# PySpark DataFrame with customer data
ratings_df 
# PySpark DataFrame with ratings data
# Groupby ratings
ratings_per_customer = ratings_df.groupBy("customer_id").mean("rating")
# Join on customer ID
customer_df.join(ratings_per_customer,  
                customer_df.customer_id==ratings_per_customer.customer_id)
