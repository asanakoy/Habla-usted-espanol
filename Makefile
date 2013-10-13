
all: sust verb adj
	foma -l combine.foma

sust:
	make -C sustantivo all
	cp sustantivo/SustantivoNormal.bin .
	cp sustantivo/GuesserSustantivo.bin .

verb:
	make -C verbo all
	cp verbo/VerboNormal.bin .

adj:
	make -C adjetivo all
	cp adjetivo/NormalAdjetivo.bin .
	cp adjetivo/GuesserAdjetivo.bin .

clean:
	find . -name \*.bin -type f -delete 
