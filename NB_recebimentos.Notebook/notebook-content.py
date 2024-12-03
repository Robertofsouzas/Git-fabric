# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "de9f799b-526e-47c4-a089-6e5d02494b63",
# META       "default_lakehouse_name": "lh_financeiro",
# META       "default_lakehouse_workspace_id": "56b5a6d9-9336-489b-bfd4-751ff3b0d20b"
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql import functions as F
from pyspark.sql import types as T

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

path= "Files/Basedados/Recebimentos.csv"
df = spark.read.options(header=True, sep = ";").csv(path)
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_typed = df.select(
   "cliente",
   "uf",
   F.col("plano_contas_id").cast("int"),
   F.to_date("data","dd/MM/yyyy").alias("data"),
   F.regexp_replace(
    F.regexp_replace("valor_recebido","[^0-9\\,]", ""),
    ",", ".").cast(T.DecimalType(10,2)).alias("valor_recebido")

)
display(df_typed)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_typed.write.mode("overwrite").saveAsTable("fato_recebimentos")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
