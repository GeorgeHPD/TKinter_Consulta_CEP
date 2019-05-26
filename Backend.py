import sqlite3 as sql

class TransactionObject():
    database    = "cep.db"
    conn        = None
    cur         = None
    connected   = False

    def connect(self):
        TransactionObject.conn      = sql.connect(TransactionObject.database)
        TransactionObject.cur       = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False

    def execute(self, sql, parms = None):
        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return TransactionObject.cur.fetchall()

    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False



def initDB():
    trans = TransactionObject()
    trans.connect()
    trans.execute("CREATE TABLE IF NOT EXISTS cep (id INTEGER PRIMARY KEY , Cep NUMERIC, Valor NUMERIC, Regiao TEXT, Risco TEXT)")
    trans.persist()
    trans.disconnect()

def insert(Cep, Valor, Regiao, Risco):
    trans = TransactionObject()
    trans.connect()
    trans.execute("INSERT INTO Cep VALUES(NULL, ?,?,?,?)", (Cep, Valor, Regiao, Risco))
    trans.persist()
    trans.disconnect()


def view():
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM Cep")
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def search(Cep="", Valor="", Regiao="", Risco=""):
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM cep WHERE Cep=? or Valor=? or Regiao=? or Risco=?", (Cep,Valor,Regiao, Risco))
    rows = trans.fetchall()
    trans.disconnect()
    return rows


def delete(id):
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM Cep WHERE id = ?", (id,))
    trans.persist()
    trans.disconnect()

def update(id, Cep, Valor, Regiao, Risco):
    trans = TransactionObject()
    trans.connect()
    trans.execute("UPDATE cep SET Cep =?, Valor=?, Regiao=?, Risco=? WHERE id = ?",(Cep, Valor,Regiao, Risco, id))
    trans.persist()
    trans.disconnect()

initDB()