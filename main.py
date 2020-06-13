from indeed import extract_indeed_pages,extract_indeed_jobs,get_jobs
from stackoverflow import get_last_page,get_so_jobs
from save import save_jobs

indeed_jobs = get_jobs()
so_jobs = get_so_jobs()
jobs = so_jobs + indeed_jobs
save_jobs(jobs)