# care-classifier

A Python Classifier for labeling lesson answers with emotional expecations.

# Care-Talker:

Care-Talker is an educational project providing teachers and educators with the tools to produce interactive text-based lessons that respond to the emotional necesities of students. By classifing responses and response patterns into different emotional categories, Care-Talker will be able to approximate if a student feels frustrated, dissinterested, curious, confused, or excited by the lesson material, allowing the lesson designer to pre-program apropiate responses that will make the student feel engaged and validated through their learning process.

# Install:

run
`pipenv install`
within the environment run
`python install-data.py`
run
`flask run`
test with postman

# Routes:

get /: returns greeting
post /test: `body: { "text" : string }` returns string in all caps and all lowercase
post /classify: `body: { "text" : string }` returns emotional classification, confidence, additional top emotional cues, and processed words.
