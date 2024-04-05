# Re-run this cell
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# Start coding here...
# Add as many cells as you like...

# Finding schools with the best math scores
best_math_schools = schools[schools["average_math"] >= 640][["school_name", "average_math"]].sort_values("average_math" ,ascending = False)

# Identifying the top 10 performing schools
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]

top_10_schools = schools.sort_values("total_SAT", ascending = False)[["school_name", "total_SAT"]].head(10)

# Locating the NYC borough with the largest standard deviation in SAT performance
# 1) Grouping the data by borough
# 2) Filtering for the largest standard deviation
# 3) Renaming columns

boroughs = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)
largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]
largest_std_dev = largest_std_dev.rename(columns = {"count" : "num_schools", "mean" : "average_SAT", "std" : "std_SAT"})

largest_std_dev.reset_index(inplace = True)

print(largest_std_dev)