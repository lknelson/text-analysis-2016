##Digital Humanities at Berkeley Summer Institute
##15-19 August 2016
##Computational Text Analysis Course

###Instructors: Laura Nelson and Teddy Roland	

##Overview
Scholars across multiple disciplines are finding themselves face-to-face with massive amounts of digitized data. In the humanities and many social science disciplines, this data is often in the form of unstructured text. This course will introduce students to cutting edge ways of structuring and analyzing digitized text-as-data, and will do so by exploring questions fundamental to the humanities. The ultimate goal is to encourage students to think about novel ways they can apply these techniques to their own data and research questions, and to provide the skills necessary to apply the methods in their own research. We will use the open source (and free!) programming language Python. We will also provide demonstration corpora.


##Prerequisites
Students must have basic computer skills, must be familiar with their computer’s file system, and should be comfortable entering commands in a command line environment.
Your time in this workshop will be much more productive if you come in with some basic knowledge of Python. Students are strongly encouraged to complete [this brief tutorial](https://www.codeschool.com/courses/try-python) to learn the basic syntax of the Python programming language.

####Please read the following to get a sense of what we'll be doing:
1. Ted Underwood. [Seven ways humanists are using computers to understand text](https://tedunderwood.com/2015/06/04/seven-ways-humanists-are-using-computers-to-understand-text/)
2. H. Andrew Schwartz and Lyle H. Ungar (2015). [Data-Driven Content Analysis of Social Media: A Systematic Overview of Automated Methods](http://wwbp.org/papers/dataDriven2015.pdf)


####Software Required
Please download and install [Anaconda for Python 3.5](https://www.continuum.io/downloads) on your laptops before coming to the workshop. If you have difficulties installing, please come early to class the first day for help.


##Tentative Schedule

####Day 1

- **Overview of text analysis methods, or why use computers to analyze text?**
    * How do we analyze text?
    * Demonstration of some exciting things you can do with digitized text-as-data
    * Overview of the next five days: What we hope you will get out of this workshop

- **Jump Right In: TextBlob and NLTK**
    * Introduction to TextBlob/NLTK
    * Text processing
    * Counting words
    * Counting tagged words

####Day 2
####Take a Step Back: Working with Texts in Python
- **Python Basics**
    * Variables
    * Lists
- **Working with Texts**
    * What is a string? (compare to floats and integers)
    * Text formats: strings, lists, and dataframes 		
- **Dataframes**
    * The Pandas dataframe	
    * Metadata
    * Subsetting and splicing dataframes using metadata
- **Dictionary Methods and Comparing Texts (may move this to Day 3 if needed)**
    * What are dictionary methods?
    * Dictionary analysis using LIWC
    * Demonstration with several applications

####Day 3	
- **Discriminating Words**
    * Methods for finding discriminating words
    * Demonstration on 2 categories
    * Demonstration on >2 categories
- **Time Permitting: Ad Hoc Stylometry: Authorship & Poetic Style**

####Day 4	
- **Text Similarity and Classification using scikit-learn**
    * Texts as Geometry
      * Distance Measures: cosine, euclidean
    * Unsupervised Methods: hierarchical, KMeans 
    * Supervised Machine Learning: Logistic Regression

####Day 5
- **Topic Modeling**
    * What are topic models?
    * Python demonstration (or MALLET demonstration?)
    * Topic Analysis / Visualization
