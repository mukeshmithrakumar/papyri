<h1>Building your first Machine Learning Web Application</h1>

<h2>Intro</h2>
As a Machine Learning Consultant, I had the privilege of working on different projects.
Clients often have different requests, they sometimes want just a package they can use as a swappable backend, but sometimes they want either a web application or a mobile application and in the beginning I tried to do everything by myself but I simply wasn't able to get things done on time because of the learning curve. This was because I wanted to learn something new with every project both on the Machine Learning side and the Software Engineering side so things became tough to manage so I hired two engineers to help me whenever I needed to build either a mobile or a web application. But I still wanted to learn how to do it by myself so I learned full stack web development and built my own website (Website link), this is version 2.0. There were a lot of resources on how
to build web applications but not so much when you want to build a web application with a python backend, deployed in AWS which uses their services and uses Machine Learning. I knew I was asking a lot but this is a summary/tips, pretty much everything that I thought a Machine Learning Engineer with a Python background would need to learn and build a Web Application.


<h2>Steps</h2>

I started with the Machine Learning Part because I was familiar with it and the main component of my app would be the machine learning components I wanted to build this and then build the flask app around it. This was the first time I was building a flask app so I wanted to make sure I atleast knew some basic requirements to get the flask app to work.

Also, I have taken some software engineering courses, if you are interested (Link for coursera course). And I have built python packages before so I wanted to have a modular / object oriented approach so if I need to swap things out I would easily be able to. Specially the machine learning components. So below is how I laid out the structure. Btw the easiest first step in following a object oriented approach is to take some time to come up with how to format things (I need to
change the word format). Below is a few software principles I used to start the project, btw I use this in my work a lot so I highly recommend taking a course on software engineering.

- Write User Story
- (Write all the steps)
- Then I spent time on designing my architecture, it takes multiple tries and some time so make sure you think through it and as to what to think, that's a long post by itself so, look into the (Software Engineering Course).

Below is my architecture for Machine Learning (Insert Image).

- Note that some design choices I made are because I want to reuse some components for a different project.

- Before starting I would spend some time on creating the correct folders and python files that you think would be needed, Spend some time naming them, you don't have to write any code, just name then and draw how the files will interact with one another.

Below is a cleaned out sketch of mine. Note that the initial version was really a rough sketch, this one looks much nicer ;)

(Insert Image of all my python files and which talks with which)

- Btw this is one of the object oriented approaches, story cards, there are softwares that does it, but I still prefer handwriting things so I can you know, cross things off and stuff.

- Next I wanted to know the interface, how is my backend going to interface with my front end. For example, below is a sketch of the web app I wanted to build. So, when someone made the search, I wrote the python file that scrapes it but how is it going to return the results. You basically need something to talk to. That interface is what Flask is for. Note that this is my first time using flask so below are some links that I used to learn about flask and to get started with Flask.

- (Flask Links)


- Btw when you are learning a library, spend time depending on how much time you would spend writing code on it. So, if you wanna build a web app or a dynamic web site using JavaScript, you gotta spend some time. Take a look at (JavaScript in 30 days). But if you are probably going to write a function to extract text from pdf like I did, spend an hour looking for things and learning the library. For Flask, I looked for 1 hour videos and a bunch of blogs to get different views of Flask, to see what's possible I both looked at easy and advanced Flask stuff. But didn't really wanna spend a day or a week learning Flask, though I am sure you can do it. But, I just don't want you to spend time learning way more than what you need cause specially me, I forget what I don't use.

I didn't want to go deep, just enough to understand what's going on. I didn't need to go deep because I was already familiar with the basics of web development. I just wanted to know how it works, how to structure the flask folders and have an idea how it might interact with python backend and javascript front end. I also know I would have to rewrite some python at the end to make it work. Which is not really ideal but since I am learning how to build using Flask, I am fine with breaking things.

- (This is how I set up the Flask folders)

- I will be hosting the app in AWS. Just because I am used to working with Google Cloud and I want to learn how AWS works. So since this was the first time I was working with AWS services other than the EC2 instances. I also needed to learn how to set up a web app using AWS and what services they offer to make things easy and best to set up. So below are some links that I used to learn about the AWS services.

- (AWS useful links)

- Now, I spent some time building an initial cloud architecture for my app.

(Cloud architecture Image)

- Now that I have an idea of how my end product will look like, i got back to the ML components. Note that when you are building the Machine Learning component, you essentially would have different architectures for training and inference and to do the inference you can just write API calls from the flask app to get the predictions so, I designed an initial architecture for that.

(Training inference Machine Learning Architecture)

- Note that in the training machine learning architecture there are a lot of services I can use for example to tune my architecture, monitor performance, set up a system so I can get the ratings of the summaries and chats and store it and use that to tune my model later. Below is an architecture for that and some services I am thinking of using.

(Updated Machine Learning Training Architecture)

- I know the architecture can be optimized and is not a best version, that is because my goal isn't to build the best first version but to build a minimum viable version that I can get to the hands of the users as fast as I can and then based on the feedback I can iterate and improve so that is why you may see some components are from the AWS Machine Learning API, I am using some of the services but my plan is to swap it out at some later point so it would give me better customizability and would let me innovate on the components. That is also why I prefer a modular approach.

- Note that my architecture will keep evolving since I am essentially building things while learning but I never build before I am confident the architecture is
1. Scalable
2. Interchangeable
3. (Write the three main things to build a software)

so even if it takes some time to learn these stuff, please do, you will save a lot of time in the end rewriting things, spending a lot of money and ultimately build an app that can scale.

Speaking of money, since I am using some paid services, I need to make an initial rough cost of acquisition of a new customer, so below is a calculation for that.

(Cost Calculation)

- Note that when you are working with clients. This is something you definitely have to spend time on.

- Then tests, I can't stress this enough, please write unit and integration test at the least. If you see my folder structure, when I created the files, I also made sure to create test files and before I start writing another module, I spend time testing the current one and then all those will go under unit_test when I finally check all the individual components in my Machine Learning Side. Then do similar tests for my app and finally do an integration testing to see if both the components work the way they should.

- I also took a mixed approach where I built the scrapper and then the front end to get a feel for how these two works together and build things in a combined modular approach. Since the front end is pretty simple, I chose to finish that and then build a component of the back end, build the interface, test it and then move to the next component.












<h2>Machine Learning Components</h2>


<h3>Text Extractor</h3>

- Make sure you have a logger and save the log files, it'll be helpful in future (Write about why logging is helpful)

__arXiv Scrapper__

Found a nice library called [arxiv](https://github.com/lukasschwab/arxiv.py) to scrape arxiv papers. I am not installing it, borrowed the script and modified  it to my need. Didn't need some of the extra bells and whistles and modified it to fit my need.

- I can use [this](https://github.com/Mahdisadjadi/arxivscraper) to add a time component where you can scrape from certain date to date

__pdf extractor__

Tried PyPDF2 and it was crap. And don't install pdfminer, nor pdfminer.six, the correct version is [pdfminer3](https://github.com/gwk/pdfminer3) but this sometimes might get installed in the wrong folder so, I just took the pdf2txt.py script that comes with it. You can find it in Scripts under the Anaconda env folder you are using. I will also highly recommend using anaconda to manage your packages cause when I tried to install pdfminer instead of pdfminer3 by accident, pdfminer tried to remove tensorflow 2 so before installing, make sure you look at which packages will be installed, upgraded or removed before saying yes to install a new package and you can only do this if you are installing using conda and not pip3. Note that I also tried slate3k but the extraction is not good at all even though they say it is from pdfminer.

- The extract_text from pdfminer3 wasn't there so I thought I'll just copy the files and modify it. The reason it the I/O cost of reading the files and saving it to the s3 bucket. And since the text size is pretty small, I can just keep things in memory and process it.

- From stack overflow:

Best thing for text extraction from PDFs is [TET](https://www.pdflib.com/), the text extraction toolkit. TET is part of the PDFlib.com family of products. But PDFlib TET can be evaluated without a license, but will only process PDF documents with up to 10 pages and 1 MB size unless a valid license key is applied. For some other solutions, which are pretty good, take a look at [this](https://stackoverflow.com/questions/3650957/how-to-extract-text-from-a-pdf)


__Notes__

I want to start with an easy solution, that is why I am going with a pdf extractor route, in the later versions, I am thinking of removing this and doing some layout analysis and extracting text from that.






<h3>Text Summarizer</h3>




<h3>Question Answering</h3>



<h3>Chatbot</h3>



<h3>Train</h3>




<h3>Inference</h3>



<h2>Flask App</h2>









<h2>AWS Components</h2>
