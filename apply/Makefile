all:
	cat spanish.txt.test.clean | flookup ../Espanol.bin > result.txt
	python apply.py
	mv answer.txt answer_test.txt
	cat spanish.txt.learn | flookup ../Espanol.bin > result.txt
	python apply.py
	mv answer.txt answer_train.txt
