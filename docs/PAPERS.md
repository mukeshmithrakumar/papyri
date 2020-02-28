<h1>Handwritten Optical Character Recognition (OCR): A Comprehensive Systematic Literature Review</h1>

[Paper Link](https://arxiv.org/pdf/2001.00139v1.pdf)

- Optical character recognition is a science that enables to translate various types of documents or images into analyzable, editable and searchable data.

- An OCR system depends mainly, on the extraction of features and discrimination / classification of these features (based on patterns).

- Handwritten OCR as a subfield of OCR is categorized into offline system and online system based on input data. The offline system is a static system in which input data is in the form of scanned images while in online systems nature of input is more dynamic and is based on the movement of pen tip having certain velocity, projection angle, position and locus point. Therefore, online system is considered more complex and advance, as it resolves overlapping problem of input data that is present in the offline system.

- The first OCR machine was built in 1940's, and till 1980, they improved the performance of these machines. From 1980 till 2000, software system for OCR was developed. From 2000 to 2010 the binarization technique was introduced but it had some difficulties because of usage of nonstandard fonts, printing noise and spacing. So in the last decade researchers have used different machine learning approaches including, SVMs. Random Forests, k-Nearest Neighbor and Decision Tree to increase accuracy. Recently, the focus has been on deep learning architectures and using RNNs, CNNs, LSTM networks and etc to digitize handwritten documents.

- SVMs, Kernel Fisher Discriminant Analysis (KFDA) and Kernel Principal Component Analysis (KPCA) are  some of the most significant kernel methods being used in offline handwritten character recognition system.

- One of the most common approach used in OCR to extract shape features is Hough transform.

-  Structural pattern recognition aims to classify objects based on relationship between its pattern structures and usually structures are extracted using pattern primitives.  One of such image primitive that has been used in OCR is Chain Code Histogram (CCH). In research studies of OCR, structural models can be further sub-divided on the basis of context of structure i.e. graphical methods and grammar based methods.

- We explored that some techniques perform better on one script than on another e.g. multilayer perceptron classifier gave better accuracy on Devanagri and Bangla numerals.



<h1>Rosetta: Understanding text in images and videos with machine learning</h1>

[Paper Link](https://engineering.fb.com/ai-research/rosetta-understanding-text-in-images-and-videos-with-machine-learning/)

- We perform text extraction on an image in two independent steps: detection and recognition. In the first step, we detect rectangular regions that potentially contain text. In the second step, we perform text recognition, where, for each of the detected regions, we use a convolutional neural network (CNN) to recognize and transcribe the word in the region.

- For text detection, we adopted an approach based on Faster R-CNN. The Faster R-CNN simultaneously performs detection and recognition. The first step performs word detection based on Faster R-CNN. The second step performs word recognition using a fully convolutional model with CTC loss. The two models are trained independently.

- Our _text detection_ model uses Faster R-CNN but replaces the ResNet convolutional body with a ShuffleNet based architecture for efficiency reasons. ShuffleNet is significantly faster than ResNet and showed comparable accuracy on our data sets. We also modify the anchors in RPN to generate wider proposals, as text words are typically wider than the objects for which the RPN was designed. In particular, we use seven aspect ratios and five sizes, so the RPN generates 35 anchor boxes per region.

- Our _text recognition_ model is a CNN based on the ResNet18 architecture, as this architecture led to good accuracies while still being computationally efficient. To train our model, we cast it as a sequence prediction problem, where the input is the image containing the text to be recognized and the output is the sequence of characters in the word image. We use the [connectionist temporal classification](https://www.cs.toronto.edu/~graves/icml_2006.pdf) (CTC) loss to train our sequence model. Casting the problem as one of sequence prediction allows the system to recognize words of arbitrary length and to recognize out-of-vocabulary words.

- Preserving the spatial location of the characters in the image may not matter for other image classification problems, but it is very important for word recognition. Because of this, we make two modifications to the ResNet18 architecture:

    - We remove the global average pooling layer at the end of the model and replace the fully connected layer with a convolutional layer that can accept inputs of different lengths.

    - We reduce the stride of the last convolutional layers to better preserve the spatial resolution of the features.

- Both changes help obtain good accuracies. Furthermore, we also use long short-term memory (LSTM) units to further improve the accuracy of our models.

<img src="./images/rosetta_architecture.jpg">

- In practice, we observed that low learning rates led to underfit models, while higher learning rates led to model divergence. To address this problem, we draw inspiration from curriculum learning, where one first trains a model with a simple(r) task and increases the difficulty of the problem as training progresses. As a result, we modify our training procedure in two ways:

    - We start training our model using only short words, with up to five characters. Once we have seen all the five-or-fewer-character words, we start training with words of six or fewer characters, then seven or fewer, etc. This significantly simplifies the problem.

    - We use a learning rate scheduling, starting with a very low learning rate to ensure that the model doesn’t diverge, and progressively increase the learning rate during the first few epochs to ensure that the model reaches a good, stable point. Once we have reached this point, we start reducing the learning rate, as is standard practice when learning deep models.

- Our model is not constrained to English text, and we currently support different languages and encodings such as, among others, Arabic and Hindi, in a unified model.

- To train a model that recognizes words in right-to-left order (when necessary) while still being able to recognize words in left-to-right order, we propose a very simple trick: We assume that words in, say, Arabic are actually read left to right, as with some other languages. Then, post-processing, we reverse the predicted characters as if they belonged to a language written right to left. This trick works surprisingly well, allowing us to have a unified model that works for both left-to-right and right-to-left languages.

- Unlike image classification models, which work fairly well on low-resolution images, object detection models typically require higher-resolution images to more accurately perform bounding box regression. For our scenarios, we resize images such that the maximum dimension is 800 pixels while maintaining the aspect ratio. We found that the larger activation maps produced by the text detection model created a bottleneck. In addition to clogging the entire system memory I/O bandwidth, it also left other resources, such as CPU, underutilized. To overcome this, we quantize the weights and activations of the text detection model to 8-bit integers instead of 32-bit float computations without significant loss of accuracy. In theory, this reduces the memory bandwidth requirement by 4x.

- When we first evaluated our quantized model, we encountered a large drop in accuracy and we applied the following techniques to reduce the accuracy gap down to 0.2 percent:

    - Net-aware quantization
    - L2 quantization error minimization
    - Selective quantization

- Motivated by [Rotation Region Proposal Networks](https://arxiv.org/abs/1703.01086), we are working on extending Faster R-CNN with anchors of arbitrary rotations, as well as experimenting with [Spatial Transformer Networks](https://arxiv.org/abs/1506.02025) to learn and correct for arbitrary affine transformations between the detection and recognition stages.



<h1>ICDAR2019: Competition on Recognition of Documents with Complex Layouts</h1>



[Paper Link](https://www.primaresearch.org/www/assets/papers/ICDAR2019_Clausner_RDCL2019.pdf)

- Layout Analysis (Page Segmentation and Region Classification) is a critical step in the recognition workflow. Its performance significantly influences the overall success of a digitization system, not only in terms of OCR accuracy but also in terms of the usefulness of the extracted information (in different use scenarios).

- Text regions metadata hold information about language, font, reading direction, text colour, background colour, logical label (e.g. heading, paragraph, caption, footer, etc.) among others. Moreover, the format offers sophisticated means for expressing reading order and more complex relations between regions. Structured content can be modelled with nested regions (regions within regions). For this competition only nested text was taken into account (table cells, text on images, chart labels etc.).

- Bitonal images are produced using the Sauvola method (window size 20, weight 0.4).

- For the evaluation of OCR results, character-based and word-based measures were used. The former gives a detailed insight into the recognition accuracy of a method while the word-based approach is more realistic in terms of use scenarios such as keyword-based search.

- It must be noted that FineReader and Tesseract have been evaluated with no prior training or knowledge of the dataset.

<img src="./images/segmentation_results.jpg">

<img src="./images/segmentation_classification_results.jpg">

<img src="./images/layout_results.jpg">

- While methods are maturing overall there is still room for improvements. Even the winning method suffers low scores for a few pages. More consistency would be desirable. The DSPH authors are certainly on the right track, they have – by some margin – the lowest standard deviation across the evaluation set (5.7%, the next best being MHS with 9.3%).

- Methods based on neural networks are particularly impacted by the relatively small training set (example set). Data augmentation seems a popular choice to increase the number of training samples. Augmentation approaches include mirroring, cropping, and various image operations. Another option is to use third-party datasets. Following these strategies, both the JBM and the ZLCW methods performed well (e.g. in the Text Regions Only scenario).

_A Brief Description of the DSPH Method_

We propose a document image segmentation method namely the DSPH
(Document Segmentation with Probabilistic Homogeneity) method which
has the following steps:

1. Binarization: a combination of two different configurations of Sauvola’s method is used.
2. Text and non-text classification: we introduce the text homogeneity and classify text and non-text components using a probabilistic map which is computed by exploiting text homogeneity at regional and component layers.
3. Text region extraction: text lines and text blocks are extracted by exploiting text homogeneity at progressively higher layers, and are refined to address versatile text structures such as drop capitals and heterogeneous text blocks. Text paragraphs are subsequently identified through a within text block segmentation based on the analysis of relative locations of the text lines.
4. Non-text structure extraction: by following a seed-grow-extraction (SGE) process separators are first extracted from non-text components. Remaining non-text components are classified heuristically into images, graphics, charts and ‘reverse-video’ text. Similar processes that all follow the SGE paradigm are performed to extract these regions.

_A Brief Description of the MHS Method_

1. Negative/positive image detection
Based on the analysis of background (distribution of dark/white pixel), we identify the input image is a negative or positive image.

2. Binarization
If the input is a positive image, we use the combination of Sauvola and Otsu’s method, otherwise, we apply the Otsu method and then invert them.

3. Text and Non-text classification
The main stage of text and non-text classification in the MHS-2019 system is the Minimum Homogeneity Algorithm (MHA) which was first introduced in 2016 [2]. This algorithm based on the connected component analysis [4] in a statistical approach. In 2017, an essential update in the core of this algorithm, the MLL classification [1] which uses the combination of Multilevel and Multilayer Homogeneity structure is presented. In recent years, we develop some module languages for the core of MHS such as Korean, France, Vietnamese, and Japanese.

4. Text segmentation and Image classification.
In this step, text documents are segmented to get text regions, and non-text elements are classified into different types.

    4.1. Text segmentation
We apply the combination of text line extraction, paragraph segmentation, and adaptive mathematic morphology to get the text region [1]. It should be noted that the segmentation contains two phases. The second phase will be performed in region refinement step.

    4.2. Non-text classification
Based on the properties of non-text elements, we classify them into the negative-text region, line, table, separator, chart, and image [1]. Our system also contains a robust table detection method which was introduced by Tran et al. [3] in 2016.

5. Region refinement and labeling.
Based on the boundary of each region, we extract the rectangular shape of the text and non-text region. In the MHS2019 we add one more segmentation step in the region which was obtained from step 4.1. It will help us to correct some segmentation errors such as split and miss-classification errors (because at this time we look only to the local region instead of all global regions).
All of the identified regions are labeled (heading, page number, etc.) based on its text size and position.

6. Optical Character Recognition
All text regions are then recognized via Tesseract OCR in Computer Vision System Toolbox (Matlab).

Reference:
[1] T. A. Tran, I. S. Na, S. H. Kim, “A Robust System for Document Layout Analysis using Multilevel Homogeneity Structure,” Expert Systems With Applications, vol. 85, pp. 99-113, 2017.

[2] T. A. Tran, I. S. Na, S. H. Kim, “Page Segmentation using Minimum Homogeneity Algorithm and Adaptive Mathematical Morphology,” International Journal on Document Analysis and Recognition, vol. 19, pp. 191-209, 2016.

[3] T. A. Tran, H. T. Tran, I. S. Na, S. H. Kim, G. S. Lee, H. J. Yang, “A Mixture Model using Random Rotation Bounding Box to Detect Table Region in Document Image,” International Journal of Visual Communication and Image Representation, vol. 39, pp. 196-208, 2016.

[4] T. A. Tran, I. S. Na, S. H. Kim, “Separation of Text and Non-text in Document Layout Analysis using a Recursive Filter,” KSII Transaction on Internet and Information Systems, vol. 9, pp. 4072-4091, 2015.
