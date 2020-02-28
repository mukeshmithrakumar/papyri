<h1>Software Development Life Cycle</h1>



<h2>Requirement Gathering</h2>

- What problem does this solve?
Deposit check written in Sinhala, Tamil and English on mobile.

- Who’s going to use it and why?
Bank Customers

- What sort of data input/output is needed?
Take a screen shot of the check

- Will you need to integrate with other tools or APIs?
Will need to be integrated with the banks existing system.

- How will you handle security/privacy?
Security will be similar to how the bank currently maintains check deposits.

The actual OCR service uses OpenCV and TensorFlow, both written in C++ and with complicated library dependencies; so security exploits are a real concern.

We initially explored three options to solve the problem:
1. Using Google's Firebase ML Kit and the Vision API for OCR
2. Purchasing commercial OCR software
3. Build everything from scratch.

The Google's Vision API already had tamil but sinhala wasn't there so if we chose that, we would have to train it and then the cost of each API call itself will be a lot for the company because of the customer base and sometimes you might have to take multiple screen shots of the check before it could be deposited, requiring calling the API multiple times. Then it also won't be possible to improve the model or experiment but since this would just be a feature the bank wanted to offer, they weren't too big on experimenting in future.

Commercial OCR for Sinhala and Tamil didn't exist but could be bought and trained, this would be a good option but depending on our use case it will have to be added as a part of a pipeline and not the sole model so we had this idea in the back burner.

Finally, building from scratch.

<h2>Design</h2>






<h3>Challenges</h3>



<h3>Solutions</h3>

- Remember how when you try to scan a check on the phone you get a bounding box and you need to have the check fit that, atleast one or two corners. I can try to use a similar technique and based on the bounding box on mobile I will essentially have a down-scaled image and I might be able to guess where something might start, like the first line or something.

<img src="./images/sample_check.jpg">

- If you look at the above check, I can easily find the date, pay to the order of location and the dollars based on the prints. I will have the exact location of those and also I can use simple pattern matching in my localizer, when I am looking for the Date, I could simply say, start at this pixel and look for the String that matches "Date" and find everything from that point till the end of "___" line.



<h3>OCR Pipeline</h3>




<h2>Implementation or coding</h2>

<h2>Testing</h2>

<h2>Deployment</h2>

<h2>Maintenance</h2>
