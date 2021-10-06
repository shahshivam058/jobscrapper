import csv

def save_jobs(jobs):
    with open("jobs.csv",mode="w")as file:
        writer = csv.writer(file)
        writer.writerow(["title","company","location","link"])
        for job in jobs:
            writer.writerow(list(job.values()))
        return
