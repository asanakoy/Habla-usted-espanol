all: sust verbo adj

sust:
	make -C sustantivo all
	cp sustantivo/SustantivoNormal.bin .
	cp sustantivo/GuesserSustantivo.bin .
adj:

verbo:
	foma -l espanol_verbo.foma

clean:
	rm -r *.bin
