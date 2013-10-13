all: sust verbo adjetivo

sust:
	make -C sustantivo all
	cp sustantivo/SustantivoGrammar.bin .

verbo:
	foma -l espanol_verbo.foma

adjetivo:
	make -C adjetivo all
# 	cp adjetivo/NormalAdjetivo.bin .
	
clean:
	find . -name \*.bin -type f -delete 
