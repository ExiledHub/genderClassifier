from dataset.dataset import Dataset

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

print("Loading...")
print("Reading data...")
data = Dataset()

print("Building model...")
cv = CountVectorizer()
X  = cv.fit_transform(data.names)
y  = data.genders

classifier = MultinomialNB()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
classifier.fit(X_train, y_train)
score = classifier.score(X_test, y_test)

print("Accuracy of model is ",score*100,"%")
print("------------------------------------")

exit = False
while not exit:
	text = input('>> ')
	if(text == 'exit' or text == 'quit'):
		exit = True
	else:
		name   = [text]
		vector = cv.transform(name).toarray()
		pred   = classifier.predict(vector)
		print("Mujer" if pred == 0 else "Hombre")