# Sentimet_Analysis_From_Image
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
