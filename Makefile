
all: sust verbo adjetivo

sust:
	make -C sustantivo all
	cp sustantivo/SustantivoNormal.bin .
	cp sustantivo/GuesserSustantivo.bin .

verbo:
	make -C verbo all
	cp verbo/VerboNormal.bin .

adjetivo:
	make -C adjetivo all
	cp adjetivo/NormalAdjetivo.bin .
	cp adjetivo/GuesserAdjetivo.bin .

clean:
	find . -name \*.bin -type f -delete 
