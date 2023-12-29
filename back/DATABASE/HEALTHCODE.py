import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost" , user="root" , passwd="$trawberry123" , database= "security");
cur=mycon.cursor();
cur.execute("INSERT INTO slno.pethealth ");
cur.execute("INSERT INTO breakfasttime.pethealth");
cur.execute("INSERT INTO lunchtime.pethealth ");
cur.execute("INSERT INTO snacktime.pethealth ");
cur.execute("INSERT INTO dinnertime.pethealth ");
cur.execute("INSERT INTO walkingtime.pethealth");
cur.execute("INSERT INTO sleepingtime.pethealth ");
cur.execute("INSERT INTO vaccinationtime.pethealth");
mycon.close();        

        