
for i in 0.1 0.2 0.3 0.4 0.5 
do
		
		sed 's/prob/'$i'/g'  Main.py > temp.py
		python3 temp.py 
		rm temp.py

done

