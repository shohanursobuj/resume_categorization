import os
import re
import pickle
import json
import PyPDF2
from nltk.corpus import stopwords
import argparse

# Define global variables
stop_words = set(stopwords.words('english'))

def load_model():
    """
    This function loads the model and vectorizer
    :return: model and vectorizer
    """
    model = pickle.load(open('model/xgbmodel.pkl', 'rb'))
    vectorizer = pickle.load(open('model/vectorizer.pkl', 'rb'))
    return model, vectorizer

def pdf_to_text(pdfFileName):
    """
    This function converts a pdf file to text
    :param pdfFileName: pdf file to be converted
    :return: text in the pdf file
    """
    text = ''
    with open(pdfFileName, 'rb') as pdfFileObj:
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        for pageNum in range(len(pdfReader.pages)):
            pageObj = pdfReader.pages[pageNum]
            text += pageObj.extract_text()
    return text

def preprocess(resumeText):
    """
    This function preprocesses the text in the resume
    :param resumeText: text in the resume
    :return: preprocessed text
    """
    resumeText = re.sub('http\S+\s*', ' ', resumeText)  # remove URLs
    resumeText = re.sub('RT|cc', ' ', resumeText)  # remove RT and cc
    resumeText = re.sub('#\S+', '', resumeText)  # remove hashtags
    resumeText = re.sub('\d+', '', resumeText)  # remove digits
    resumeText = re.sub('[^a-zA-Z\s]', '', resumeText)  # remove special characters (excluding whitespace and letters)
    resumeText = re.sub('@\S+', ' ', resumeText)  # remove mentions
    resumeText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', resumeText)  # remove punctuations
    resumeText = re.sub(r'[^\x00-\x7f]', r' ', resumeText)  # remove non-ascii characters
    resumeText = re.sub('\s+', ' ', resumeText)  # remove extra whitespace
    resumeText = resumeText.lower()  # convert to lowercase
    # remove stopwords from resume text
    resumeText = ' '.join(word for word in resumeText.split() if word not in stop_words)
    return resumeText
    
def main(input_dir):
    """
    This function categorizes resumes in the input directory
    :param input_dir: input directory containing resumes
    """
    for filename in os.listdir(input_dir):
        if filename.endswith('.pdf'):
            pdfFileName = os.path.join(input_dir, filename)
            resumeText = pdf_to_text(pdfFileName)
            resumeText = preprocess(resumeText)
            # load model and vectorizer
            model, vectorizer = load_model()
            # vectorize resume text
            resumeText = vectorizer.transform([resumeText])
            # predict using model
            prediction = model.predict(resumeText)
            predicted_label = prediction[0]
            # move resume to appropriate folder use label_dict json file to get label name
            with open('model/labels_dict.json', 'rb') as f:
                labels_dict = json.load(f)
            if str(predicted_label) in labels_dict:
                predicted_category = labels_dict[str(predicted_label)]
                print("Predicted category:", predicted_category)
            else:
                print("Category not found")
            output_dir = os.path.join(input_dir, predicted_category)
            # create directory if it doesn't exist
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            # move file to output directory
            os.rename(pdfFileName, os.path.join(output_dir, filename))
            print(filename, prediction)

            # create a csv file with filename and predicted category add a header if file doesn't exist
            csv_file = 'categorized_resumes.csv'
            if not os.path.exists(csv_file):
                with open(csv_file, 'w') as f:
                    f.write('filename,category\n')
            # append filename and predicted category to csv file
            with open(csv_file, 'a') as f:
                f.write(filename + ',' + predicted_category + '\n')
        else:
            continue
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', type=str, default='resumes', help='input directory containing resumes')
    args = parser.parse_args()
    main(args.input_dir)
    print("Resume Categorization Completed")
