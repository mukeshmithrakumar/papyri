<p align="center"><img src="https://raw.githubusercontent.com/mukeshmithrakumar/papyri-docs/master/images/cover.png"/></p>


<h2>Inspiration</h2>


I am a Machine Learning, I work in a industry that is growing fast and evolving in a rapid pace that no human can keep pace with. This has been my life for the past three years, I am sure you would be able to relate.

"You subscribe to some journals or follow some twitter channels, for example, I follow the arXiv twitter channel and everyday you get around 20-30 notification on new papers being published, even if not everything is related to what you do, some papers may hold solutions to problems you have been wrestling with but how would you know that without going through the paper. The abstract only provides so much, so what do you do, you bookmark and you hope you'll read the 200 research papers you bookmarked in the last month and you never get the time."

That was my problem and for anyone who would love to be on top of the latest research, this is for you, an app that will summarize a research paper and if you have any doubts from the paper, you can talk with a chatbot and it will be able to provide you with answers.


<h2>What it does</h2>


I was only able to finish the first release, what the app does now is it searches arXiv based on your keyword and presents only one result that matches your query and is the latest paper published. But you can also customize the results, get any paper you want and you click a button and a summarizer behind the screen summarizes the paper for you.

<img src="https://raw.githubusercontent.com/mukeshmithrakumar/papyri-docs/master/images/aws_summarizer_demo.gif"/>

(If the demo isn't visible, take a look at the next tab)

In the second release, I am planning to integrate this with a ChatBot so for whatever paper you summarize, a ChatBot will be ready to answer any questions you have on the paper.

In the third release, I am planning to extend this as an Alexa Skill. Imagine,

"You have a busy life, I mean we all do, and let's say you have a problem at work, something I was recently struggling with was on Time Series Clustering for millions of records, try googling to find a latest paper, read the abstract, look for any open source implementation, its gonna be a while before you solve that problem. So, let's say you are driving for work and you remember about this and you ask the Papyri Bot in Alexa to search for any latest papers on Time Series Clustering and it would present you with the latest research papers and reads out the title for you, you then select some papers and ask questions about the papers and the bot responds, based on the response, you ask the bot to look for any implementation of the paper and the bot which is integrated with papers with code and github finds you some open source implementation and you ask it to mail you the links."

Before you get to office, you potentially have some solutions you can try out.


<h2>How I built it</h2>


Below is the architecture I built, note that this is only the Summarizer Architecture and I am still working on the ChatBot and the CI/CD architecture:

<img src="https://raw.githubusercontent.com/mukeshmithrakumar/papyri-docs/master/images/aws_summarizer_architecture.png"/>

The Elastic Beanstalk Container serves my frontend to the user and it also does the searching of arXiv based on user query and then when the user selects a PDF to summarize, the PDF meta like the title and url is posted from JavaScript to the API Gateway which then initiates the Lambda Function to extract and clean the data and the clean data gets stored in a clean text bucket and a successful execution returns a 200 which is received by JavaScript which then passes some meta information to the Flask and then Flask invokes the Mphasis Text Summarizer endpoint in SageMaker for prediction of the cleaned text. The cleaned text is then stored in the browser and rendered to the user and after the session ends the summary text along with user rating of the summary, paper title and url gets sent to another the bucket as JSON, which then invokes a SNS and the Lambda function extracts the meta data and stores it in the AuroraDB. I am exploring the usage of graph databases since I think it will be beneficial for the chatbot so AuroraDB is just a placeholder for now.

The Elastic Beanstalk is load balanced with a minimum of 2 instances and a max of 4 instances, with t2.small (1vCPUs, 2GiB) and t2.medium (2vCPUs, 4GiB) instances. The instances will increase by 1 if the CPU utilization increases by more than 70% and decreases by 1 if it goes below 20%. In the 2 instances, 1 is a spot instance and another one is an on demand instance with high availability.

All of the API calls and the Meta data is being monitored using CloudWatch.


<h2>Challenges I ran into</h2>


I've built packages before but I've never worked with Flask or AWS before and I had the usual challenges of balancing what I need to learn with all the resources out there because of the deadline.

I relied on AWS LinkedIn course (details in the [Blog](https://github.com/mukeshmithrakumar/papyri-docs/blob/master/docs/BLOG.md)), and [AWS Events](https://www.youtube.com/channel/UCdoadna9HFHsxXWhafhNvKw), [Amazon Web Services](https://www.youtube.com/channel/UCd6MoB9NC6uYN2grvUNT-Zg) and [AWS Online Tech Talks](https://www.youtube.com/user/AWSwebinars) YouTube channels.

Surprisingly the AWS documentation was pretty good too, initially I felt overwhelmed with the amount of information in the docs but if you follow a course and try it with your project you can pick things up pretty fast.

There was also a lot of minor issues you run into like learning how to write aws configs and haha getting your favicon to show up in EBS. You are used to working locally and now you have to think in terms of the cloud architecture, like building a CI/CD pipeline is really easy locally but setting it up with AWS is still a challenge and its for good reasons. Basically if you want to have like a one click deployment, you would have to run a combination of shell scripts or change how you create your resources or use CloudFormation YAML templates, which I haven't really got into just yet.

I also ran into small integration issues, not while building but while thinking about the architecture. I think it was because I haven't really gone in depth into AWS and understood the nuances. I think with all the courses and videos I spent about 20-30hrs learning AWS and Flask and I had to re-watch some content and re-read documentation multiple times while working on the architecture and deploying it.

Other than that, it was pretty easy working with AWS, I could have finished the ChatBot as well if I didn't slack off a week because of the stay at home. Working from home has made me really lazy.

For a detailed discussion, take a look at the [Blog](https://github.com/mukeshmithrakumar/papyri-docs/blob/master/docs/BLOG.md)


<h2>Accomplishments that I'm proud of</h2>


I would have been happy about finishing the app if I had completed the ChatBot on time ;).

I did a small alpha test with some of my friends and colleagues and they seem to like the app and find it useful and they also gave me some recommendations so I am happy they find it useful.

I think I would be little bit proud when I get the app to market, when I have my first paid user. For now, I think winning the competition would be a good start, will help me with AWS credits and the money I need to take this to market.


<h2>What I learned</h2>


This is a technical challenge so I learned a lot on the technical side. AWS and Flask are the two main topics. I won't say I perfectly understand these two, I know what I know and I know what I need to learn.

While going through other AWS architectures, I learned that designing AWS architectures isn't easy, you can build something easily but designing a scalable product which runs smoothly is a lot challenging because scaling isn't just about having more users or increasing the instances. It's also about bringing in employees to your organization and they need a lot of tools to function and good architectures should fulfill those requirements too and that's something I was completely oblivious as a Machine Learning Engineer.


<h2>What's next for Papyri</h2>


- I have to improve the summarizer. I am planning to talk with Mphasis about using custom models and retraining on my dataset. The text cleaner can definitely be better and that would increase model performance as well so may be using AWS Textractor to extract data and a better cleaner.

- Get the website domain name registered.

- Do another alpha test with a larger sample size and get user feedback.

- Below are two services I am thinking of adding which might change in terms of functionalities based on the alpha test feedback:
    1. The Chatbot
    2. An Alexa Skill component to the app

- Before these two I would like to finish the CI/CD pipeline, set up AWS budgets, cost and usage reports.

- I am also going to work on the following recommendations I've got from the small alpha test I ran:
    - Expand the search beyond arXiv
    - Have a functionality so the user can upload custom PDFs and get summaries.
    - Decrease the latency of summarization.

- Change from open access to a sign-on app with a one month trial which then either goes into a subscription model or per usage model, need to think more about it. This is also one thing I would like to delve little deeper with the alpha test.

- Do some social media marketing and put the app into beta.
