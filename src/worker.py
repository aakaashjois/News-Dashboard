import dispy, random
import parsing
cluster = dispy.JobCluster(parsing.parse)
jobs = []
lines = None
with open('../data.csv', 'r') as f:
    lines = f.readlines()

for line in lines:
    url, location, category = line.split(',')
    job = cluster.submit(url)
    jobs.append(job)
# cluster.wait() # waits for all scheduled jobs to finish
for job in jobs:
    print(job()) # waits for job to finish and returns results
    
    
cluster.print_status()
