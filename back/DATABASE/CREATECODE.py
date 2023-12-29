import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost" , user="root" , passwd="$trawberry123" , database= "security");
cur=mycon.cursor();
cur.execute("INSERT INTO slno.createpost");
cur.execute("INSERT INTO location.createpost ");
cur.execute("INSERT INTO missingdays.createpost ");
cur.execute("INSERT INTO caption.createpost");
mycon.close();        
        
        