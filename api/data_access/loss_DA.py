from database.database_manager import DatabaseManager


class DALoss():

    def clear_table():
        db_conn = DatabaseManager()
        sql_exec = """DELETE FROM loss"""
        db_conn.cursor.execute(sql_exec)
        db_conn.connection.commit()
        db_conn.close_connection()      

    def new_loss(producer_name, producer_email, producer_CPF, crop_local, crop_type, harvest_date, event_type):
        db_conn = DatabaseManager()
        sql_exec = """INSERT INTO loss(producer_name,
                                producer_email,
                                producer_CPF,
                                crop_local,
                                crop_type,
                                harvest_date,
                                event_type) 
                    VALUES(%s,%s,%s,%s,%s,%s,%s)"""
        loss = (producer_name,producer_email,producer_CPF,crop_local,crop_type,harvest_date,event_type)
        db_conn.cursor.execute(sql_exec,loss)
        db_conn.connection.commit()
        id = db_conn.cursor.lastrowid
        db_conn.close_connection()
        return id


    def edit_loss(id,producer_name, producer_email, producer_CPF, crop_local, crop_type, harvest_date, event_type):
        db_conn = DatabaseManager()
        sql_exec = """UPDATE loss
                      SET producer_name=%s,
                      producer_email=%s,
                      producer_CPF=%s,
                      crop_local=%s,
                      crop_type=%s,
                      harvest_date=%s,
                      event_type=%s WHERE id=%s"""
        params = (producer_name,producer_email,producer_CPF,crop_local,crop_type,harvest_date,event_type,id)
        db_conn.cursor.execute(sql_exec,params)
        db_conn.connection.commit()
        db_conn.close_connection()

    def delete_loss(id):
        db_conn = DatabaseManager()
        sql_exec = """DELETE FROM loss WHERE id=%s"""
        params = (id,)
        db_conn.cursor.execute(sql_exec,params)
        db_conn.connection.commit()
        db_conn.close_connection()

    def get_loss(id):
        db_conn = DatabaseManager()
        sql_exec = """SELECT * FROM loss WHERE id=%s"""
        params = (id,)
        db_conn.cursor.execute(sql_exec,params)
        result = db_conn.cursor.fetchone()
        db_conn.close_connection()
        return result

    def list_by_date(date):
        db_conn = DatabaseManager()
        sql_exec = """SELECT * FROM loss WHERE harvest_date=%s"""
        params = (date,)
        db_conn.cursor.execute(sql_exec,params)
        result = db_conn.cursor.fetchall()
        db_conn.close_connection()
        return result        
        
    def list_loss_by_cpf(cpf):
        db_conn = DatabaseManager()
        sql_exec = """SELECT * FROM loss WHERE producer_cpf=%s"""
        params = (cpf,)
        db_conn.cursor.execute(sql_exec,params)
        result = db_conn.cursor.fetchall()
        db_conn.close_connection()
        return result

    def list_loss():
        db_conn = DatabaseManager()
        sql_exec = """SELECT * FROM loss"""
        db_conn.cursor.execute(sql_exec)
        result = db_conn.cursor.fetchall()
        db_conn.close_connection()
        return result