- [AWS Essential Training for Developers](https://www.linkedin.com/learning/aws-essential-training-for-developers) - 130 mins
- [AWS: Deploying and Provisioning](https://www.linkedin.com/learning/aws-deploying-and-provisioning) - 120 mins
- [AWS for Developers: Deploying Your Application to the Cloud](https://www.linkedin.com/learning/aws-for-developers-deploying-your-application-to-the-cloud) - 50 mins
- [AWS API Gateway with HTTP, Lambda, DynamoDB, and iOS](https://www.linkedin.com/learning/aws-api-gateway-with-http-lambda-dynamodb-and-ios) - 90 mins
- [Learning Amazon Web Services Lambda](https://www.linkedin.com/learning/learning-amazon-web-services-lambda-2) - 70 mins
- [Building Dynamic Websites using AWS Lambdas](https://www.linkedin.com/learning/building-dynamic-websites-using-aws-lambdas) - 50 mins
- [Amazon Web Services Machine Learning Essential Training](https://www.linkedin.com/learning/amazon-web-services-machine-learning-essential-training) - 190 mins
- [Building Intelligent Chatbots on AWS](https://www.linkedin.com/learning/building-intelligent-chatbots-on-aws) - 70 mins
- [Amazon Web Services: Data Services](https://www.linkedin.com/learning/amazon-web-services-data-services) - 270 mins
- [Full Stack Web Development with Flask](https://www.linkedin.com/learning/full-stack-web-development-with-flask) - 260 mins


- [AWS Elastic Beanstalk under the Hood](https://www.youtube.com/watch?v=U06-QLd4FL4)
- [Deploy your code, scale, and lower cloud costs using Elastic Beanstalk](https://www.youtube.com/watch?v=o4clRJuH9xU)
- [Introduction to AWS Lambda & Serverless Applications](https://www.youtube.com/watch?v=EBSdyoO3goc)
- [Deep Dive Into Lambda Layers and the Lambda Runtime API](https://www.youtube.com/watch?v=gCQHulp3aVo)
- [I didn’t know Amazon API Gateway did that](https://www.youtube.com/watch?v=yfJZc3sJZ8E)
- [Building microservices with AWS Lambda](https://www.youtube.com/watch?v=TOn0xhev0Uk)
- [Setup Local Lambda Development Environment Using SAM - Serverless Application Model](https://www.youtube.com/watch?v=bih5b3C1nqc)
- [Authoring and Deploying Serverless Applications with AWS SAM](https://www.youtube.com/watch?v=MSsMOtLZXKc)
- [GitHub to AWS Lambda: Developing, Testing, and Deploying Server](https://www.youtube.com/watch?v=lYYLGBdFXqM)
- [Local Testing and Deployment Best Practices for Serverless Applications](https://www.youtube.com/watch?v=QRSc1dL-I4U)
- [Amazon CI/CD Practices for Software Development Teams](https://www.youtube.com/watch?v=3HKbXz0RwSg)
- [How to Do Continuous Integration and Continuous Deployment with AWS Lambda and AWS CodePipeline](https://www.youtube.com/watch?v=P7i01eqmzrs)


<h1>Game Plan</h1>

1. ✅ Write pdf_extract (March 7th)
2. ⬜️ Write text_summarizer / explore AWS summarizer (March 14th)
3. ⬜️ Write question_answer (March 21st)
4. ⬜️ Write bot / explore AWS bot (March 28th)
5. ⬜️ Build app and deploy using AWS (April 4th)
6. ⬜️ Record Demo and Do the write up (April 11th)


<h1>Idea</h1>

My model is going to take in research papers and start with a layout document detector, and then its going to use one of the services in AWS to detect if there are any tables, and then its going to take the text in the layouts and summarize the research paper based on each paragraph. It's basically a summarizer for research papers. I can also extend this for emails and other types of documents.

I'll build the document layout recognition using the ICDAR 2019 solutions. For the tables in the document, I can use the AWS solution and I can also use the text summarizer for the text in the documents. Augment as much as you can for the base architecture with AWS services.


<h2>To Do</h2>

- Rewrite some of the extract code to JavaScript cause when you search for a paper, you don't need to send the request to the server, you can just render the results using JavaScript and then only when the user selects the paper, then send the link and the paper details to the server so it can be downloaded in the server and converted to text before calling the inference engine to summarize the text.

- Create a Alexa Skill where the person can search using keywords. For example:
"Alexa, what are the new research papers related to Machine Learning that was published today"
Alexa will extract Machine Learning and today and start with.
"There are about 30 papers that was published today, do you want me to read it?"
"No, what papers focus on Hardware acceleration among the 30 papers?"
Alexa will now look for hardware acceleration keyword in the paper and
"I found 1 paper that mentions hardware acceleration"
"Could you give me a quick summary on it"
Alexa will start the summary or abstract
"Huh, what is the name of the algorithm again?"
"SLIDE, stands for Sub-LInear Deep learning Engine"
The user can ask further questions or ask to see if there are any code for that and Alexa can search in GitHub or Papers with Code and
"Yes I found some implementation for the code"
"Could you please send the details to my mail"
Alexa sends then paper url, summary and the chat details with link to the paper.

- Write the JavaScript so that the search results are loaded async and not everything at once.
