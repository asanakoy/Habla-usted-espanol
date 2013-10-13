al: clean adj sust verb
	foma -l combine.foma
adj:
	make -C adjetivo all
	cp adjetivo/NormalAdjetivo.bin .
	cp adjetivo/GuesserAdjetivo.bin .
	
sust:
	make -C sustantivo all
	cp sustantivo/SustantivoNormal.bin .
	cp sustantivo/GuesserSustantivo.bin .
	
verb:
	make -C verbo all
	cp verbo/VerboNormal.bin .
clean:
	find . -name \*.bin -type f -delete 
