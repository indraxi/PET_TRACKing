import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost" , user="root" , passwd="$trawberry123" , database= "security");
cur=mycon.cursor();
cur.execute("INSERT INTO  ");
cur.execute("INSERT INTO BREED.petdetails ");
cur.execute("INSERT INTO PETCOLOR.petdetails ");
cur.execute("INSERT INTO AGE.petdetails ");
cur.execute("INSERT INTO EYECOLOR.petdetails ");
cur.execute("INSERT INTO UNIQUE_IDENTIFICATION.petdetails ");
mycon.close();        
        
        