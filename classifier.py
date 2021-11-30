from nrclex import NRCLex
def classify(inputString):
    response = NRCLex(inputString)
    return {
        'response' : inputString,
        'raw-words' : response.words,
        'emotional' : {
            'top-scores' : response.top_emotions,
            'classification' : response.top_emotions[0][0],
            'classification-confidence' : response.top_emotions[0][1],
            },
        'expectation' : 'to be added',
        }