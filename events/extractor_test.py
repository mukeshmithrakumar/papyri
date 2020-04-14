import unittest

from extractor.lambda_handler import Extract, Clean


class TestExtract(unittest.TestCase):

    def test_extract_text(self):
        pass

    def test_download_url(self):
        pass

    def test_slugify(self):
        obj = {"title": "Lecture Notes: Optimization for Machine Learning",
               "authors": "Elad Hazan",
               "date": "2019-09-08",
               "url": "http://arxiv.org/abs/1909.03550v1"
               }

        true_title = "Lecture_Notes_Optimization_for_Machine_Learning"
        self.assertEqual(Extract().slugify(obj), true_title)

    def test_text_extract(self):
        obj = {"title": "Lecture Notes: Optimization for Machine Learning",
               "authors": "Elad Hazan",
               "date": "2019-09-08",
               "url": "http://arxiv.org/abs/1909.03550v1"
               }

        raw_text = Extract().text_extract(obj)


class TestClean(unittest.TestCase):

    def test_remove_non_ascii(self):
        pass

    def test_remove_punctuation(self):
        pass

    def test_clean_text(self):
        obj = {"title": "Lecture Notes: Optimization for Machine Learning",
               "authors": "Elad Hazan",
               "date": "2019-09-08",
               "url": "http://arxiv.org/abs/1909.03550v1"
               }

        # raw_text = Extract().text_extract(obj)
        raw_text = """lecture notes:

9.1 Review: relevant concepts from linear algebra . . . . . . . . .
9.2 Motivation: matrix completion and recommendation systems
9.3 The Frank-Wolfe method . . . . . . . . . . . . . . . . . . . .
9.4 Projections vs. linear optimization . . . . . . . . . . . . . . .
9.5 Exercises
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.6 Bibliographic Remarks . . . . . . . . . . . . . . . . . . . . . .

Notation

We use the following mathematical notation in this writeup:

• d-dimensional Euclidean space is denoted Rd.
• Vectors are denoted by boldface lower-case letters such as x ∈ Rd. Co-
ordinates of vectors are denoted by underscore notation xi or regular
brackets x(i).

• Matrices are denoted by boldface upper-case letters such as X ∈ Rm×n.

Their coordinates by X(i, j), or Xij.

• Functions are denoted by lower case letters f : Rd (cid:55)→ R.
• The k-th diﬀerential of function f is denoted by ∇kf ∈ Rdk . The

gradient is denoted without the superscript, as ∇f .
• We use the mathcal macro for sets, such as K ⊆ Rd.
• We denote the gradient at point xt as ∇xt, or simply ∇t.
• We denote the global or local optima of functions by x(cid:63).
• We denote distance to optimality for iterative algorithms by ht =

f (xt) − f (x(cid:63)).

• Euclidean distance to optimality is denoted dt = (cid:107)xt − x(cid:63)(cid:107).

The machine learning approach to solving problems is to have an au-
tomated mechanism for learning an algorithm. Consider the problem of
classifying images into two categories: those containing cars and those con-
taining chairs (assuming there are only two types of images in the world).
In ML we train (teach) a machine to achieve the desired functionality. The
same machine can potentially solve any algorithmic task, and diﬀers from
task to task only by a set of parameters that determine the functionality of
the machine. This is much like the wires in a computer chip determine its"""

        with open('raw_text.txt', 'w', encoding='utf-8') as fp:
            fp.write(raw_text)
        fp.close()

        raw_text_path = "raw_text.txt"

        clean_text_list = Clean().clean_text(raw_text_path)

        # Save Cleaned Text Data
        true_title = "clean_test_text"
        text = true_title + '.txt'
        with open(text, "w") as file:
            file.writelines("%s\n" % line for line in clean_text_list)
        file.close()


if __name__ == "__main__":
    unittest.main()
