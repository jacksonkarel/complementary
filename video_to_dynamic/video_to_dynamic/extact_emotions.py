import re

def extract_emotions(description):
    # Regular expression to find words after the colon and between the commas
    emotions = re.findall(r'(?<=: )[\w\s]+(?=,|$)', description)
    
    # Strip any unnecessary whitespace and create a list
    emotions = [emotion.strip() for emotion in emotions]
    
    return emotions