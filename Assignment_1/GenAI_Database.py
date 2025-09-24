import sqlite3
DB = "Task_List.db"

def init():
    conn = sqlite3.connect("Task_List.db")
    curser = conn.cursor()


    curser.execute("""    
        CREATE TABLE IF NOT EXISTS Tasks(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT,
            Status Text         )
    """
    )
    conn.commit()
    conn.close()


def add_task(title):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (Title) VALUES (?)", (title,))
    conn.commit()
    conn.close()


def list_task():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Tasks")        
    rows = cursor.fetchall()
    conn.close()
    return rows


def mark_completed(ID):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()            
    cursor.execute(f"UPDATE Tasks SET Status = 'Completed' WHERE ID = {ID}")    
    conn.commit()
    conn.close()



def delete_task(ID):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor() 
    cursor.execute("DELETE FROM Tasks WHERE id=?", (ID,))    
    conn.commit()
    

