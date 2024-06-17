# Importing the required libraries
import pytesseract  
from transformers import pipeline  
from PIL import Image  

# Define a class for sentiment analysis
class Sentiment_analysis:
    """
    A class to perform sentiment analysis on text extracted from an image using Tesseract OCR and Hugging Face's transformers pipeline.

    Attributes
    ----------
    Texts : str
        The text extracted from the image.
    Sentiment : str
        The sentiment label of the extracted text.
    Sentiment_accuracy : float
        The accuracy score of the sentiment analysis.

    Methods
    -------
    __init__(self, image)
        Initializes the Sentiment_analysis class with an image.
    Analysis(self)
        Extracts text from the image using Tesseract OCR and performs sentiment analysis on the text.
    """
    
    Texts = str()  # Class attribute to hold extracted text from the image
    Sentiment = None  # Class attribute to hold sentiment label
    Sentiment_accuracy = None  # Class attribute to hold sentiment score

    def __init__(self, image) -> None:
        # Initialize the class with an image
        self.i = image

    def Analysis(self) -> list:
        '''Function Docstring'''
        # Create a sentiment analysis pipeline
        Analyzer = pipeline("sentiment-analysis")
        
        # Specify the path to the Tesseract executable
        pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
        
        # Extract text from the image using Tesseract OCR
        self.Texts = pytesseract.image_to_string(self.i)
        
        # Perform sentiment analysis on the extracted text
        result = Analyzer(self.Texts)
        
        # Store the sentiment label and accuracy score
        self.Sentiment, self.Sentiment_accuracy = result[0]['label'], result[0]['score']

# Define a function to run the sentiment analysis
def Run() -> str:
    '''Function Docstring'''
    # Loop to continuously ask for image paths
    while ask := input('Enter an image path :'):
        # Open the image from the given path
        pic = Image.open(ask)
        
        # Create an instance of Sentiment_analysis with the image
        sample = Sentiment_analysis(pic)
        
        # Perform the analysis
        sample.Analysis()
        
        # Print the results
        print(f'\n\n\nResult for {ask.split("/")[-1]} :\nSentiment : {sample.Sentiment}\nAccuracy : {sample.Sentiment_accuracy*100:0.2f}%')

# Run the function to start the sentiment analysis
Run()
