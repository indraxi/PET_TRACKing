import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost" , user="root" , passwd="$trawberry123" , database= "security");
cur=mycon.cursor();
cur.execute("INSERT INTO NAME.personal details ");
cur.execute("INSERT INTO AGE.personal details ");
cur.execute("INSERT INTO EMAIL.personal details ");
cur.execute("INSERT INTO PHONENO.personal details ");
cur.execute("INSERT INTO COUNTRY.personal details ");
cur.execute("INSERT INTO STATE.personal details ");
cur.execute("INSERT INTO ADDRESS.personal details ");
cur.execute("INSERT INTO BIO.personal details ");
mycon.close();        
        
        
