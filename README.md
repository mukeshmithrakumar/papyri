<h1>Software Development Life Cycle</h1>



<h2>Requirement Gathering</h2>





<h2>Design</h2>

- The app takes an image (Front End)
- Localize all the handwritten text, tables and diagrams in scanned documents/image (Text localization runs locally)
- Digitize/Classify handwritten text, tables and diagrams (Text recognition, runs locally/cloud)

I'll start with summarizing research papers and then move to handwriting for Mithra and since for the research papers I am going to rely on AWS, i'll try to minimize how much.

<h3>OCR Ideas</h3>

The base version will have something to detect the _orientation_, then may be a _filter_ ([Morphological Transformations](https://docs.opencv.org/trunk/d9/d61/tutorial_py_morphological_ops.html)), then something to _localize text_ and then after it localizes the text a _classifier_ to recognize the handwritten words or think of it as digitizing the handwritten text. The written letters will be correctly classified.

If I have issues with the digitized document, meaning some words don't make sense I can try to build a text localizer that can create a bounding box ([blackhat operator](https://www.pyimagesearch.com/2017/07/31/bank-check-ocr-opencv-python-part-ii/)) around the words so that it can help in not only classifying the letters but also properly recognizing the word. I can have like a dictionary where you pattern match the word and remove any spelling errors and help in increasing the performance.

The model for the bank will have a language classification model before sending the localized text into the recognition model to classify between English, Tamil and Sinhala. And then one of the three language packages will get activated and either English, Tamil or Sinhala text is classified. Finally, I would also like to have a Tamil to English and Sinhala to English Translation module.

When we are reading, we often glance over words, we don't need to see every letter to know a word so why not build something like that. Look into the words, see if you can guess it, guess it, see if it makes sense or use the context to guess the word (like a bidirectional LSTM) and then move on, kinda like an auto fill in keyboard.

To localize text, I can have like a SSD or some object detection model tuned to detect bounding boxes but the problem is I need bounding boxes with varying shapes. So a segmentation would be more suitable. I need to see what other techniques were used in classical computer vision for this purpose. I can also look into just a region proposal network, it will have a lower overhead and I could also get labels like, text, diagram, formula and the sort. Then I can invoke the correct model based on that.

So, let's say you have detected the bounding box and localized the text. How to classify the text, MLP will work if you are able to localize as a per letter basis, if not I can think of a combined CNN RNN approach that takes in the bounding box, or I think just a RNN with a CNN inside would be better, for example, you break the image into small slices, send each slice through a LSTM, the CNN inside it classifies the slice and pass it to the next block, and you use that prediction with the next slice to determine what the word can be, if its too small, you try to use the next RNN block, if its not, you use a dictionary to predict the word. After it predicts a sentence I can have a roll back system which reads what it predicted and checks if it makes sense.





<h3>Challenges</h3>



<h3>Solutions</h3>



<h3>OCR Pipeline</h3>




<h2>Implementation or coding</h2>

<h2>Testing</h2>

<h2>Deployment</h2>

<h2>Maintenance</h2>
