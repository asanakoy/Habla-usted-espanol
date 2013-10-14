all:
	cat spanish.txt.test.clean.utf-8 | flookup ../Espanol.bin > result.txt
	python apply.py
	mv answer.txt answer_test.txt
	cat spanish.txt.learn.utf-8 | flookup ../Espanol.bin > result.txt
	python apply.py
	mv answer.txt answer_train.txt
	iconv -f utf-8 -t latin1 answer_test.txt > answer_test_latin1.txt
	iconv -f utf-8 -t latin1 answer_train.txt > answer_train_latin1.txt
	python evaluate.py spanish.txt.learn answer_train_latin1.txt


