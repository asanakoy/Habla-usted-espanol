all: clean sust verb adj
	foma -l combine.foma
	make -C apply all

adj:
	make -C adjetivo all
	cp adjetivo/AdjetivoNormal.bin .
	cp adjetivo/GuesserAdjetivo.bin .
	
sust:
	make -C sustantivo all
	cp sustantivo/SustantivoNormal.bin .
	cp sustantivo/GuesserSustantivo.bin .

verb:
	make -C verbo all
	cp verbo/VerboNormal.bin .
	cp verbo/GuesserVerbo.bin .

clean:
	find . -name \*.bin -type f -delete 
