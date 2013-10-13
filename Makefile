sust:
	make -C sustantivo all
	cp sustantivo/SustantivoGrammar.bin .

verbo:
	foma -l espanol_verbo.foma

clean:
	rm -r *.bin
