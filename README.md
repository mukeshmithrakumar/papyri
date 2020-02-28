<h1>Game Plan</h1>

1. Write pdf_extract (March 7th)
2. Write text_summarizer / explore AWS summarizer (March 14th)
3. Write question_answer (March 21st)
4. Write bot / explore AWS bot (March 28th)
5. Build app and deploy using AWS (April 4th)
6. Record Demo and Do the write up (April 11th)


<h1>Idea</h1>

My model is going to take in research papers and start with a layout document detector, and then its going to use one of the services in AWS to detect if there are any tables, and then its going to take the text in the layouts and summarize the research paper based on each paragraph. It's basically a summarizer for research papers. I can also extend this for emails and other types of documents.

I'll build the document layout recognition using the ICDAR 2019 solutions. For the tables in the document, I can use the AWS solution and I can also use the text summarizer for the text in the documents. Augment as much as you can for the base architecture with AWS services.



<h1>Pipeline</h1>



<img src="./images/general_architecture.jpg">

- Text Extractor
    - arxiv_scrape: Search for arXiv papers
    - pdf2text: Convert pdf to text
- Text Summarizer: Summarizes the text that was recognized from the layout.
- Q&A System: Send the recognized text to a Question Answering System.
- Chatbot: That behaves as a interface for question answering
- Mobile App: A simple app, where you can access arxiv papers, search for it and then it will summarize the paper, give out a summary and an interactive chatbot which will answer any questions you might have after reading the summary.

- If I am going to use arxiv to find research papers to summarize, those research papers are in pdf format so why not just take the pdf and extract text out of it by either directly extracting the text or converting it into a word format, that way I can skip the text recognition as well and jump straight into summarizing and the rest of the pipeline.

Below is the initial Papyri Architecture:

<img src="./images/papyri_architecture.jpg">

See if I can write the pdf extractor in JavaScript so it runs in the browser and streams the data to the aws to do summarization.


<h2>Text Extractor</h2>



<h2>Text Summarization</h2>






<h2>Q&A System</h2>




<h2>Chatbot</h2>




<h2>To Do</h2>

- Rewrite some of the extract code to JavaScript cause when you search for a paper, you don't need to send the request to
the server, you can just render the results using JavaScript and then only when the user selects the paper, then
send the link and the paper details to the server so it can be downloaded in the server and converted to text before
calling the inference engine to summarize the text.
