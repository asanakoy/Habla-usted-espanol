
all: sust verbo adjetivo
	foma -l combine.foma

sust:
	make -C sustantivo all
	cp sustantivo/SustantivoNormal.bin .
	cp sustantivo/GuesserSustantivo.bin .
	
verbo:
	foma -l espanol_verbo.foma

adjetivo:
	make -C adjetivo all
	cp adjetivo/NormalAdjetivo.bin .
	cp adjetivo/GuesserAdjetivo.bin .
	
clean:
	find . -name \*.bin -type f -delete 
