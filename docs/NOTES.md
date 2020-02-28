
<h1>Notes</h1>


<h2>Intro to OCR</h2>


[Link](https://towardsdatascience.com/a-gentle-introduction-to-ocr-ee1469a201aa)

The text recognition is a two step task:
1. You would need to detect the text

After detecting the line/word level we can choose once again from a large set of solutions, which generally come from three main approaches:

<h3>Classic computer vision techniques</h3>

1. Apply filters to make the characters stand out from the background.
2. Apply contour detection to recognize the characters one by one.
3. Apply image classification to identify the characters.

The challenge is with two, if that is done well then part three can be done with either pattern matching or machine learning.

<h3>Specialized deep learning</h3>

__[EAST](https://arxiv.org/pdf/1704.03155.pdf)__ ( Efficient accurate scene text detector) is a simple yet powerful approach for text detection. Using a specialized network.
Unlike the other methods we’ll discuss, is limited only to text detection (not actual recognition) however it’s robustness make it worth mentioning.
Another advantage is that it was also added to open-CV library (from version 4) so you can easily use it (see tutorial [here](https://www.pyimagesearch.com/2018/08/20/opencv-text-detection-east-text-detector/)).

__CRNN__ (Convolutional-recurrent neural network), suggest a hybrid (or tribrid?) end to end architecture, that is intended to capture words, in a three step approach.
The idea goes as follows: the first level is a standard fully convolutional network. The last layer of the net is defined as feature layer, and divided into “feature columns”. See in the image below how every such feature column is intended to represent a certain section in the text.

<img src="./images/crnn_1.jpg">

Afterwards, the feature columns are fed into a deep-bidirectional LSTM which outputs a sequence, and is intended for finding relations between the characters.

<img src="./images/crnn_2.jpg">

Finally, the third part is a transcription layer. Its goal is to take the messy character sequence, in which some characters are redundant and others are blank, and use probabilistic method to unify and make sense out of it.

This method is called CTC loss, and can be read about [here](https://gab41.lab41.org/speech-recognition-you-down-with-ctc-8d3b558943f0). This layer can be used with/without predefined lexicon, which may facilitate predictions of words.

This paper reaches high (>95%) rates of accuracy with fixed text lexicon, and varying rates of success without it.

<h3>Standard deep learning approach (Detection)</h3>

After detecting the “words” we can apply standard deep learning detection approaches, such as SSD, YOLO and Mask RCNN.


<h2>Bank check OCR with OpenCV and Python</h2>


[Link](https://www.pyimagesearch.com/2017/07/24/bank-check-ocr-with-opencv-and-python-part-i/)

Bank checks used special fonts where a particular symbol consists of multiple parts — this implies that we need to devise a method that can automatically compute the bounding boxes for these symbols and extract them.

However, while our template matching method worked correctly on this particular example image, real-world inputs are likely to be much more noisy, making it harder for us to extract the digits and symbols using simple contour techniques.

In these situations, it would be best to localize each of the digits and characters followed by applying machine learning to obtain higher digit classification accuracy. Methods such as Histogram of Oriented Gradients + Linear SVM and deep learning will obtain better digit and symbol recognition accuracy on real-world images that contain more noise.


<h2>Creating a Modern OCR Pipeline Using Computer Vision and Deep Learning</h2>


[Link](https://blogs.dropbox.com/tech/2017/04/creating-a-modern-ocr-pipeline-using-computer-vision-and-deep-learning/)

For our Word Detector we decided to not use a deep net-based approach. The primary candidates for such approaches were object detection systems, like RCNN, that try to detect the locations (bounding boxes) of objects like dogs, cats, or plants from images. Most images only have perhaps one to five instances of a given object.

However, most documents don’t just have a handful of words — they have hundreds or even thousands of them, i.e., a few orders of magnitude more objects than most neural network-based object detection systems were capable of finding at the time. We were thus not sure that such algorithms would scale up to the level our OCR system needed.

We ended up using a classic computer vision approach named Maximally Stable Extremal Regions ([MSERs](https://en.wikipedia.org/wiki/Maximally_stable_extremal_regions)), using OpenCV’s implementation. The MSER algorithm finds connected regions at different thresholds, or levels, of the image. Essentially, they detect blobs in images, and are thus particularly good for text.

Our Word Detector first detects MSER features in an image, then strings these together into word and line detections. One tricky aspect is that our word deep net accepts fixed size word image inputs. This requires the word detector to thus sometimes include more than one word in a single detection box, or chop a single word in half if it is too long to fit the deep net’s input size. Information on this chopping then has to be propagated through the entire pipeline, so that we can re-assemble it after the deep net has run. Another bit of trickiness is dealing with images with white text on dark backgrounds, as opposed to dark text on white backgrounds, forcing our MSER detector to be able to handle both scenarios.


<h2>An Introduction to Text Summarization using the TextRank Algorithm</h2>


[Link](https://www.analyticsvidhya.com/blog/2018/11/introduction-text-summarization-textrank-python/)

Text summarization can broadly be divided into two categories — _Extractive Summarization_ and _Abstractive Summarization_.

- Extractive Summarization: These methods rely on extracting several parts, such as phrases and sentences, from a piece of text and stack them together to create a summary. Therefore, identifying the right sentences for summarization is of utmost importance in an extractive method.

- Abstractive Summarization: These methods use advanced NLP techniques to generate an entirely new summary. Some parts of this summary may not even appear in the original text.

TextRank is an extractive and unsupervised text summarization technique. Let’s take a look at the flow of the TextRank algorithm that we will be following:

<img src="./images/text_rank.jpg">


<h2>Comprehensive Guide to Text Summarization using Deep Learning in Python</h2>


[Link](https://www.analyticsvidhya.com/blog/2019/06/comprehensive-guide-text-summarization-using-deep-learning-python/)

A potential issue with this encoder-decoder approach is that a neural network needs to be able to compress all the necessary information of a source sentence into a fixed-length vector. This may make it difficult for the neural network to cope with long sentences. The performance of a basic encoder-decoder deteriorates rapidly as the length of an input sentence increases.

So how do we overcome this problem of long sequences? This is where the concept of attention mechanism comes into the picture. It aims to predict a word by looking at a few specific parts of the sequence only, rather than the entire sequence.


<h2>Text Summarization for busy people</h2>


[Link](https://wiki.ubc.ca/Course:CPSC522/Text_Summarization_for_busy_people!)


<h2>Text Summarization with Python</h2>


[Link](https://medium.com/@umerfarooq_26378/text-summarization-in-python-76c0a41f0dc4)

gensim.summarization offers TextRank summarization.

PyTeaser takes any news article and extracts a brief summary from it.

Summaries are created by ranking sentences in a news article according to how relevant they are to the entire text. The top 5 sentences are used to form a “summary”. Each sentence is ranked by using four criteria:
- Relevance to the title
- Relevance to keywords in the article
- The position of the sentence
- Length of the sentence

pytextrank is the Python implementation of TextRank.

















<h2>General</h2>


Document understanding goes over and above OCR, requiring layout analysis, handwritten text recognition, symbolic language interpretation etc., on anything from administrative and historical documents to mixed-type documents such as maps and diagrams. Understanding text in the wild, on the other hand, has already enabled applications such as image-based translation or autonomous navigation.
