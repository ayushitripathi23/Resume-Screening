# Resume-Screening

Today the major problem being faced across the industry is how to acquire the right talent, using minimal
resources over the internet and in minimal time. There are three major challenges that are required to be
overcome, to bring efficiencies to the complete process, which are:
• Separating the right candidates from the bulk
• Making sense of candidate’s Resume
• Knowing that candidates can do before company the job hires them

**Approach Used: Content Based Filtering**

The principle of a content-based recommendation is to suggest items that have similar
content information to the corresponding users, like Prospect. Considering this is the case
of document similarity identification, we have gone with this where Job Description
provided by the employer is matched with the content of resumes in the space and the top n
matching resumes are recommended to the recruiter. The model takes the cleansed resume
data and job description, and the computes the cosine similarity between the job description
and CVs.
