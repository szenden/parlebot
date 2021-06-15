import sqlite3

cnx = sqlite3.connect ('parlebot.db')



@app.route('/',methods=['GET','POST'])
def get_data():
 return render_template("kamervragen_beantwoorden.html")
  if request.method=='POST':
    title=request.form['title']
    question1=request.form['question1']
    question2=request.form['question2']
    cursor = db.cursor()
    cursor.execute("""
    INSERT INTO test(title,question1,question2) \
    VALUES (%s,%s,%s) """, (title,question1,question2))
    cursor.close()
    return "nothing fucked"


cursor = cnx.cursor()
cursor.execute(insert_query)

cnx.commit()
cursor.close()
cnx.close()