import tkinter as tk
from tkinter import messagebox as MessageBox
import mysql.connector as mysql


if __name__ == '__main__':
    dbhost = 'localhost'
    dbuser = 'test'
    dbpass = 'test123'
    dbname = 'musorujsag'

    root = tk.Tk()
    root.geometry("930x1080")
    root.configure(bg='antiquewhite3')
    root.title("Műsorújság - 2022/11/14")

    # CSATORNA

    def t_get():
        if tvcsatornak_e_id.get() == "":
            MessageBox.showinfo("Info", "ID mező kitöltése kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('select * from musorujsag.tvcsatornak where csatornaid ="{}" '.format(tvcsatornak_e_id.get()))
            rows = cursor.fetchmany(1)
            tvcsatornak_e_nev.delete(0, 'end')
            tvcsatornak_e_nezettseg.delete(0, 'end')
            for row in rows:
                tvcsatornak_e_nev.insert(0, row[1])
                tvcsatornak_e_nezettseg.insert(0, row[2])
            con.close()

    def t_insert():
        if tvcsatornak_e_id.get() == "" or tvcsatornak_e_nev.get() == "" or tvcsatornak_e_nezettseg.get() == "":
            MessageBox.showinfo("Info", "Minden mező kitöltése kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('insert into musorujsag.tvcsatornak values("{}","{}","{}")'.format(tvcsatornak_e_id.get(), tvcsatornak_e_nev.get(), tvcsatornak_e_nezettseg.get()))
            cursor.execute('commit')
            tvcsatornak_e_id.delete(0, 'end')
            tvcsatornak_e_nev.delete(0, 'end')
            tvcsatornak_e_nezettseg.delete(0, 'end')
            MessageBox.showinfo('Info', 'Sikeres beszúrás!')
            con.close()
            t_show()

    def t_update():
        if tvcsatornak_e_id.get() == "" or tvcsatornak_e_nev.get() == "" or tvcsatornak_e_nezettseg.get() == "":
            MessageBox.showinfo("Info", "Minden mező kötelező")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('update musorujsag.tvcsatornak set nev="{}", nezettseg="{}" where csatornaid="{}"'.format(tvcsatornak_e_nev.get(), tvcsatornak_e_nezettseg.get(), tvcsatornak_e_id.get()))
            cursor.execute('commit')
            tvcsatornak_e_id.delete(0, 'end')
            tvcsatornak_e_nev.delete(0, 'end')
            tvcsatornak_e_nezettseg.delete(0, 'end')
            MessageBox.showinfo('Info', 'Sikeres frissítés')
            con.close()
            t_show()

    def t_delete():
        if tvcsatornak_e_id.get() == "":
            MessageBox.showinfo("Info", "ID mező kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('delete from musorujsag.tvcsatornak where csatornaid="{}"'.format(tvcsatornak_e_id.get()))
            cursor.execute('commit')
            tvcsatornak_e_id.delete(0, 'end')
            tvcsatornak_e_nev.delete(0, 'end')
            tvcsatornak_e_nezettseg.delete(0, 'end')
            MessageBox.showinfo('Info', 'Sikeresen törölted a csatornát!')
            con.close()
            t_show()

    def t_show():
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from musorujsag.tvcsatornak')
        rows = cursor.fetchall()
        list.delete(0, list.size())
        for row in rows:
            insertData = 'A(z) {}. ID-s csatorna neve: {} nézettsége: {} fő'.format(row[0], row[1], row[2])
            list.insert(list.size() + 1, insertData)
        con.close()

    tvcsatornak_xhely = 20
    tvcsatornak_yhely = 10

    tvcsatornak_cim = tk.Label(root, text='TV Csatornák', font=('bold', 15), bg='moccasin')
    tvcsatornak_cim.place(x=tvcsatornak_xhely, y=tvcsatornak_yhely)

    tvcsatornak_id = tk.Label(root, text='Csatorna ID:', font=('bold', 10), bg='antiquewhite2', highlightthickness=2)
    tvcsatornak_id.place(x=tvcsatornak_xhely, y=tvcsatornak_yhely + 40)
    tvcsatornak_e_id = tk.Entry(highlightthickness=2 ,highlightcolor='black')
    tvcsatornak_e_id.place(x=tvcsatornak_xhely + 130, y=tvcsatornak_yhely + 43)

    tvcsatornak_nev = tk.Label(root, text='Név:', font=('bold', 10), bg='antiquewhite2', highlightthickness=2)
    tvcsatornak_nev.place(x=tvcsatornak_xhely, y=tvcsatornak_yhely + 70)
    tvcsatornak_e_nev = tk.Entry(highlightthickness=2 ,highlightcolor='black')
    tvcsatornak_e_nev.place(x=tvcsatornak_xhely + 130, y=tvcsatornak_yhely + 73)

    tvcsatornak_nezettseg = tk.Label(root, text='Nézettség:', font=('bold', 10), bg='antiquewhite2', highlightthickness=2)
    tvcsatornak_nezettseg.place(x=tvcsatornak_xhely, y=tvcsatornak_yhely + 100)
    tvcsatornak_e_nezettseg = tk.Entry(highlightthickness=2 ,highlightcolor='black')
    tvcsatornak_e_nezettseg.place(x=tvcsatornak_xhely + 130, y=tvcsatornak_yhely + 103)

    tvcsatornak_insert_button = tk.Button(root, text=' Beszúr ', font=('italic', 10), bg='antiquewhite', command=t_insert)
    tvcsatornak_insert_button.place(x=tvcsatornak_xhely, y=tvcsatornak_yhely + 140)

    tvcsatornak_update_button = tk.Button(root, text="Frissít", font=('italic', 10), bg='antiquewhite', command=t_update)
    tvcsatornak_update_button.place(x=tvcsatornak_xhely + 65, y=tvcsatornak_yhely + 140)

    tvcsatornak_get_button = tk.Button(root, text="Lekér", font=('italic', 10), bg="antiquewhite", command=t_get)
    tvcsatornak_get_button.place(x=tvcsatornak_xhely + 116.5, y=tvcsatornak_yhely + 140)

    tvcsatornak_delete_button = tk.Button(root, text="Törlés", font=('italic', 10), bg="brown3", command=t_delete)
    tvcsatornak_delete_button.place(x=tvcsatornak_xhely + 165, y=tvcsatornak_yhely + 140)

    tvcsatornak_show_button = tk.Button(root, text="Össz.", font=('italic', 10), bg="olivedrab", command=t_show)
    tvcsatornak_show_button.place(x=tvcsatornak_xhely + 215, y=tvcsatornak_yhely + 140)

    # MŰSOROK

    def m_get():
        if musorok_e_id.get()== "":
            MessageBox.showinfo("Info", "ID mező kitöltése kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('select * from musorujsag.musorok where musorid="{}"'.format(musorok_e_id.get()))
            rows = cursor.fetchmany(1)
            musorok_e_cim.delete(0, 'end')
            musorok_e_tipus.delete(0, 'end')
            musorok_e_hossz.delete(0, 'end')
            musorok_e_korhatar.delete(0, 'end')
            for row in rows:
                musorok_e_cim.insert(0, row[1])
                musorok_e_tipus.insert(0, row[2])
                musorok_e_hossz.insert(0, row[3])
                musorok_e_korhatar.insert(0, row[4])
            con.close()

    def m_insert():
        if musorok_e_id.get() == "" or musorok_e_cim.get() == "" or musorok_e_tipus.get() == "" or musorok_e_hossz.get() == "" or musorok_e_korhatar.get() == "":
            MessageBox.showinfo("Info", "Minden mező kitöltése kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('insert into musorujsag.musorok values("{}","{}","{}","{}","{}")'.format(musorok_e_id.get(), musorok_e_cim.get(), musorok_e_tipus.get(), musorok_e_hossz.get(), musorok_e_korhatar.get()))
            cursor.execute('commit')
            musorok_e_id.delete(0, 'end')
            musorok_e_cim.delete(0, 'end')
            musorok_e_tipus.delete(0, 'end')
            musorok_e_hossz.delete(0, 'end')
            musorok_e_korhatar.delete(0, 'end')
            MessageBox.showinfo('Info', 'Sikeres beszúrás!')
            con.close()
            m_show()

    def m_update():
        if musorok_e_id.get() == "" or musorok_e_cim.get() == "" or musorok_e_tipus.get() == "" or musorok_e_hossz.get() == "" or musorok_e_korhatar.get() == "":
            MessageBox.showinfo("Info", "Minden mező kitöltése kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('update musorujsag.musorok set cim="{}", tipus="{}", hossz="{}", korhatar="{}" where musorid="{}"'.format(musorok_e_cim.get(), musorok_e_tipus.get(), musorok_e_hossz.get(), musorok_e_korhatar.get(), musorok_e_id.get()))
            cursor.execute('commit')
            musorok_e_id.delete(0, 'end')
            musorok_e_cim.delete(0, 'end')
            musorok_e_tipus.delete(0, 'end')
            musorok_e_hossz.delete(0, 'end')
            musorok_e_korhatar.delete(0, 'end')
            MessageBox.showinfo('Info', 'Sikeres frissítés')
            con.close()
            m_show()

    def m_delete():
        if musorok_e_id.get() == "":
            MessageBox.showinfo("Info", "ID mező kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('delete from musorujsag.musorok where musorid="{}"'.format(musorok_e_id.get()))
            cursor.execute('commit')
            musorok_e_id.delete(0, 'end')
            musorok_e_cim.delete(0, 'end')
            musorok_e_tipus.delete(0, 'end')
            musorok_e_hossz.delete(0, 'end')
            musorok_e_korhatar.delete(0, 'end')
            MessageBox.showinfo('Info', 'Sikeresen törölted a műsort!')
            con.close()
            m_show()

    def m_show():
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from musorujsag.musorok')
        rows = cursor.fetchall()
        list.delete(0, list.size())
        for row in rows:
            insertData = '{} - {} - {} - {} - {}'.format(row[0], row[1], row[2], row[3], row[4])
            list.insert(list.size() + 1, insertData)
        con.close()

    m_xhely = 20
    m_yhely = 210

    musorok_cim = tk.Label(root, text='Műsorok', font=('bold', 15), bg='moccasin')
    musorok_cim.place(x=m_xhely, y=m_yhely)

    musorok_id = tk.Label(root, text='Műsor ID:', font=('bold', 10), bg='antiquewhite2', highlightthickness=2)
    musorok_id.place(x=m_xhely, y=m_yhely + 40)
    musorok_e_id = tk.Entry(highlightthickness=2, highlightcolor='black')
    musorok_e_id.place(x=m_xhely + 130, y=m_yhely + 43)

    musorok_cim = tk.Label(root, text='Cím:', font=('bold', 10), bg='antiquewhite2', highlightthickness=2)
    musorok_cim.place(x=m_xhely, y=m_yhely + 70)
    musorok_e_cim = tk.Entry(highlightthickness=2 , highlightcolor='black')
    musorok_e_cim.place(x=m_xhely + 130, y=m_yhely + 73)

    musorok_tipus = tk.Label(root, text='Műfaj:', font=('bold', 10), bg='antiquewhite2', highlightthickness=2)
    musorok_tipus.place(x=m_xhely, y=m_yhely + 100)
    musorok_e_tipus = tk.Entry(highlightthickness=2, highlightcolor='black')
    musorok_e_tipus.place(x=m_xhely + 130, y=m_yhely + 103)

    musorok_hossz = tk.Label(root, text='Hossz:', font=('bold', 10), bg='antiquewhite2', highlightthickness=2)
    musorok_hossz.place(x=m_xhely, y=m_yhely + 130)
    musorok_e_hossz = tk.Entry(highlightthickness=2, highlightcolor='black')
    musorok_e_hossz.place(x=m_xhely + 130, y=m_yhely + 133)

    musorok_korhatar = tk.Label(root, text='Korhatár:', font=('bold', 10), bg='antiquewhite2', highlightthickness=2)
    musorok_korhatar.place(x=m_xhely, y=m_yhely + 160)
    musorok_e_korhatar = tk.Entry(highlightthickness=2, highlightcolor='black')
    musorok_e_korhatar.place(x=m_xhely + 130, y=m_yhely + 163)

    musorok_insert_button = tk.Button(root, text=' Beszúr ', font=('italic', 10), bg='antiquewhite', command=m_insert)
    musorok_insert_button.place(x=m_xhely, y=m_yhely + 197)

    musorok_update_button = tk.Button(root, text="Frissít", font=('italic', 10), bg='antiquewhite', command=m_update)
    musorok_update_button.place(x=m_xhely + 65, y=m_yhely + 197)

    musorok_get_button = tk.Button(root, text="Lekér", font=('italic', 10), bg="antiquewhite", command=m_get)
    musorok_get_button.place(x=m_xhely + 116.5, y=m_yhely + 197)

    musorok_delete_button = tk.Button(root, text="Törlés", font=('italic', 10), bg="brown3", command=m_delete)
    musorok_delete_button.place(x=m_xhely + 165, y=m_yhely + 197)

    musorok_show_button = tk.Button(root, text="Össz.", font=('italic', 10), bg="olivedrab", command=m_show)
    musorok_show_button.place(x=m_xhely + 215, y=m_yhely + 197)

    # SZEREPLŐK

    def sz_get():
        if szereplok_e_id.get() == "":
            MessageBox.showinfo("Info", "ID mező kitöltése kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('select * from musorujsag.szereplok where szereploid ="{}" '.format(szereplok_e_id.get()))
            rows = cursor.fetchmany(1)
            szereplok_e_nev.delete(0, 'end')
            szereplok_e_szulido.delete(0, 'end')
            szereplok_e_szarhely.delete(0, 'end')
            for row in rows:
                szereplok_e_nev.insert(0, row[1])
                szereplok_e_szulido.insert(0, row[2])
                szereplok_e_szarhely.insert(0, row[3])
            con.close()

    def sz_insert():
        if szereplok_e_id.get() == "" or szereplok_e_nev.get() == "" or szereplok_e_szulido.get() == "" or szereplok_e_szarhely.get() == "":
            MessageBox.showinfo("Info", "Minden mező kitöltése kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('insert into musorujsag.szereplok values("{}","{}","{}","{}")'.format(szereplok_e_id.get(), szereplok_e_nev.get(), szereplok_e_szulido.get(), szereplok_e_szarhely.get()))
            cursor.execute('commit')
            szereplok_e_id.delete(0, 'end')
            szereplok_e_nev.delete(0, 'end')
            szereplok_e_szulido.delete(0, 'end')
            szereplok_e_szarhely.delete(0, 'end')
            MessageBox.showinfo('Info', 'Sikeres beszúrás!')
            con.close()
            sz_show()

    def sz_update():
        if szereplok_e_id.get() == "" or szereplok_e_nev.get() == "" or szereplok_e_szulido.get() == "" or szereplok_e_szarhely.get() == "":
            MessageBox.showinfo("Info", "Minden mező kitöltése kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('update musorujsag.szereplok set nev="{}", szuletesiido="{}", szarmazasihely="{}" where szereploid="{}"'.format(szereplok_e_nev.get(), szereplok_e_szulido.get(), szereplok_e_szarhely.get(), szereplok_e_id.get()))
            cursor.execute('commit')
            szereplok_e_id.delete(0, 'end')
            szereplok_e_nev.delete(0, 'end')
            szereplok_e_szulido.delete(0, 'end')
            szereplok_e_szarhely.delete(0, 'end')
            MessageBox.showinfo('Info', 'Sikeres frissítés')
            con.close()
            sz_show()

    def sz_delete():
        if szereplok_e_id.get() == "":
            MessageBox.showinfo("Info", "ID mező kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('delete from musorujsag.szereplok where szereploid="{}"'.format(szereplok_e_id.get()))
            cursor.execute('commit')
            szereplok_e_id.delete(0, 'end')
            szereplok_e_nev.delete(0, 'end')
            szereplok_e_szulido.delete(0, 'end')
            szereplok_e_szarhely.delete(0, 'end')
            MessageBox.showinfo('Info', 'Sikeresen törölted a szereplőt!')
            con.close()
            sz_show()

    def sz_show():
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from musorujsag.szereplok')
        rows = cursor.fetchall()
        list.delete(0, list.size())
        for row in rows:
            insertData = '{}-{}--{}---{}'.format(row[0], row[1], row[2], row[3])
            list.insert(list.size() + 1, insertData)
        con.close()

    sz_xhely = 20
    sz_yhely = 468

    szereplok_cim = tk.Label(root, text='Szereplők', font=('bold', 15), bg='moccasin')
    szereplok_cim.place(x=sz_xhely, y=sz_yhely)

    szereplok_id = tk.Label(root, text='Szereplő ID:', font=('bold', 10), bg='antiquewhite2', highlightthickness=2)
    szereplok_id.place(x=sz_xhely, y=sz_yhely + 40)
    szereplok_e_id = tk.Entry(highlightthickness=2, highlightcolor='black')
    szereplok_e_id.place(x=sz_xhely + 130, y=sz_yhely + 43)

    szereplok_nev = tk.Label(root, text='Név:', font=('bold', 10), bg='antiquewhite2', highlightthickness=2)
    szereplok_nev.place(x=sz_xhely, y=sz_yhely + 70)
    szereplok_e_nev = tk.Entry(highlightthickness=2, highlightcolor='black')
    szereplok_e_nev.place(x=sz_xhely + 130, y=sz_yhely + 73)

    szereplok_szulido = tk.Label(root, text='Születési idő:', font=('bold', 10), bg='antiquewhite2', highlightthickness=2)
    szereplok_szulido.place(x=sz_xhely, y=sz_yhely + 100)
    szereplok_e_szulido = tk.Entry(highlightthickness=2, highlightcolor='black')
    szereplok_e_szulido.place(x=sz_xhely + 130, y=sz_yhely + 103)

    szereplok_szarhely = tk.Label(root, text='Származási hely:', font=('bold', 10), bg='antiquewhite2', highlightthickness=2)
    szereplok_szarhely.place(x=sz_xhely, y=sz_yhely + 130)
    szereplok_e_szarhely = tk.Entry(highlightthickness=2, highlightcolor='black')
    szereplok_e_szarhely.place(x=sz_xhely + 130, y=sz_yhely + 133)

    szereplok_insert_button = tk.Button(root, text=' Beszúr ', font=('italic', 10), bg='antiquewhite', command=sz_insert)
    szereplok_insert_button.place(x=sz_xhely, y=sz_yhely + 170)

    szereplok_update_button = tk.Button(root, text="Frissít", font=('italic', 10), bg='antiquewhite', command=sz_update)
    szereplok_update_button.place(x=sz_xhely + 65, y=sz_yhely + 170)

    szereplok_get_button = tk.Button(root, text="Lekér", font=('italic', 10), bg="antiquewhite", command=sz_get)
    szereplok_get_button.place(x=sz_xhely + 116.5, y=sz_yhely + 170)

    szereplok_delete_button = tk.Button(root, text="Törlés", font=('italic', 10), bg="brown3", command=sz_delete)
    szereplok_delete_button.place(x=sz_xhely + 165, y=sz_yhely + 170)

    szereplok_show_button = tk.Button(root, text="Össz.", font=('italic', 10), bg="olivedrab", command=sz_show)
    szereplok_show_button.place(x=sz_xhely + 215, y=sz_yhely + 170)

    # KÖZVETÍT

    def k_get():
        if kozvetit_e_csatornaid.get() == "" or kozvetit_e_idopont.get() == "":
            MessageBox.showinfo("Info", "CsatornaID és Időpont mező kitöltése kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('select * from musorujsag.tvcsatornak where csatornaid="{}"'.format(kozvetit_e_csatornaid.get()))
            csatornaid_check = 0
            for row in cursor:
                csatornaid_check += 1
            cursor.execute('select * from musorujsag.kozvetit where idopont="{}"'.format(kozvetit_e_idopont.get()))
            idopont_check = 0
            for row in cursor:
                idopont_check += 1
            con.close()
            if csatornaid_check == 0 and idopont_check == 0:
                MessageBox.showinfo("Info", "Nem létezik a megadott ID-val Csatorna illetve ebben az időpontban műsor!")
            elif csatornaid_check == 0:
                MessageBox.showinfo("Info", "Nem létezik a megadott ID-val Csatorna!")
            elif idopont_check == 0:
                MessageBox.showinfo("Info", "Nem létezik a megadott időpontban műsor!")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('select * from musorujsag.kozvetit where tv_csatornaid="{}" and idopont="{}"'.format(kozvetit_e_csatornaid.get(), kozvetit_e_idopont.get()))
            rows = cursor.fetchmany(1)
            kozvetit_e_musorid.delete(0, 'end')
            for row in rows:
                kozvetit_e_musorid.insert(0, row[1])
            con.close()

    def k_insert():
        if kozvetit_e_csatornaid.get() == "" or kozvetit_e_musorid.get() == "" or kozvetit_e_idopont == "":
            MessageBox.showinfo("Info", "Minden mező kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(
                'select * from musorujsag.tvcsatornak where csatornaid="{}"'.format(kozvetit_e_csatornaid.get()))
            k_csatornaid_check = 0
            for row in cursor:
                k_csatornaid_check += 1
            cursor.execute('select * from musorujsag.musorok where musorid="{}"'.format(kozvetit_e_musorid.get()))
            k_musorid_check = 0
            for row in cursor:
                k_musorid_check += 1
            con.close()
            if k_csatornaid_check == 0 and k_musorid_check == 0:
                MessageBox.showinfo("Info", "Nem létezik ilyen ID-val Csatorna illetve Műsor! Próbáld újra!")
            elif k_csatornaid_check == 0:
                MessageBox.showinfo("Info", "Nem létezik ilyen ID-val Csatorna!")
            elif k_musorid_check == 0:
                MessageBox.showinfo("Info", "Nem létezik ilyen ID-val Műsor! Próbáld újra!")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('insert into musorujsag.kozvetit values("{}","{}","{}")'.format(kozvetit_e_csatornaid.get(), kozvetit_e_musorid.get(), kozvetit_e_idopont.get()))
                cursor.execute('commit')
                kozvetit_e_csatornaid.delete(0, 'end')
                kozvetit_e_musorid.delete(0, 'end')
                kozvetit_e_idopont.delete(0, 'end')
                MessageBox.showinfo("Info", "Sikeres beszúrás!")
                con.close()
                k_show()

    def k_delete():
        if kozvetit_e_csatornaid.get() == "" or kozvetit_e_idopont.get() == "":
            MessageBox.showinfo("Info", "Csatorna ID és Időpont mezőket kötelező megadni!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('select * from musorujsag.tvcsatornak where csatornaid="{}"'.format(kozvetit_e_csatornaid.get()))
            k_csatornaid_check = 0
            for row in cursor:
                k_csatornaid_check += 1
            cursor.execute('select * from musorujsag.kozvetit where idopont="{}"'.format(kozvetit_e_idopont.get()))
            idopont_check = 0
            for row in cursor:
                idopont_check += 1
            con.close()
            if k_csatornaid_check == 0 and idopont_check == 0:
                MessageBox.showinfo("Info", "Nem létezik ilyen CsatornaID illetve Időpont!")
            elif k_csatornaid_check == 0:
                MessageBox.showinfo("Info", "Nem létezik ilyen CSatornaID!")
            elif idopont_check == 0:
                MessageBox.showinfo("Info", "Nem létezik ilyen időpont!")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('delete from musorujsag.kozvetit where tv_csatornaid="{}" and m_musorid="{}" and idopont="{}"'.format(kozvetit_e_csatornaid.get(), kozvetit_e_musorid.get(), kozvetit_e_idopont.get()))
                cursor.execute('commit')
                kozvetit_e_csatornaid.delete(0, 'end')
                kozvetit_e_idopont.delete(0, 'end')
                kozvetit_e_musorid.delete(0, 'end')
                MessageBox.showinfo("Info", "Sikeres törlés!")
                con.close()
                k_show()

    def k_show():
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from musorujsag.kozvetit')
        rows = cursor.fetchall()
        list.delete(0, list.size())
        for row in rows:
            insertData = '{}-{}--{}'.format(row[0], row[1], row[2])
            list.insert(list.size() + 1, insertData)
        con.close()

    k_xhely = 20
    k_yhely = 695

    kozvetit_cim = tk.Label(root, text='Közvetít', font=('bold', 15), bg='moccasin')
    kozvetit_cim.place(x=k_xhely, y=k_yhely)

    kozvetit_csatornaid = tk.Label(root, text='Csatorna ID:', font=('bold', 10), bg='antiquewhite2', highlightthickness=2)
    kozvetit_csatornaid.place(x=k_xhely, y=k_yhely + 40)
    kozvetit_e_csatornaid = tk.Entry(highlightthickness=2, highlightcolor='black')
    kozvetit_e_csatornaid.place(x=k_xhely + 130, y=k_yhely + 43)

    kozvetit_musorid = tk.Label(root, text='Műsor ID:', font=('bold', 10), bg='antiquewhite2', highlightthickness=2)
    kozvetit_musorid.place(x=k_xhely, y=k_yhely + 70)
    kozvetit_e_musorid = tk.Entry(highlightthickness=2, highlightcolor='black')
    kozvetit_e_musorid.place(x=k_xhely + 130, y=k_yhely + 73)

    kozvetit_idopont = tk.Label(root, text='Időpont:', font=('bold', 10), bg='antiquewhite2', highlightthickness=2)
    kozvetit_idopont.place(x=k_xhely, y=k_yhely + 100)
    kozvetit_e_idopont = tk.Entry(highlightthickness=2, highlightcolor='black')
    kozvetit_e_idopont.place(x=k_xhely + 130, y=k_yhely + 103)

    kozvetit_insert_button = tk.Button(root, text=' Beszúr ', font=('italic', 10), bg='antiquewhite', command=k_insert)
    kozvetit_insert_button.place(x=k_xhely, y=k_yhely + 140)

    kozvetit_get_button = tk.Button(root, text="Lekér", font=('italic', 10), bg="antiquewhite", command=k_get)
    kozvetit_get_button.place(x=k_xhely + 65, y=k_yhely + 140)

    kozvetit_delete_button = tk.Button(root, text="Törlés", font=('italic', 10), bg="brown3", command=k_delete)
    kozvetit_delete_button.place(x=k_xhely + 113, y=k_yhely + 140)

    kozvetit_show_button = tk.Button(root, text="Össz.", font=('italic', 10), bg="olivedrab", command=k_show)
    kozvetit_show_button.place(x=k_xhely + 163, y=k_yhely + 140)

    # JÁTSZIK

    def j_insert():
        if jatszik_e_szereploid.get() == "" or jatszik_e_musorid == "":
            MessageBox.showinfo("Info", "Minden mező kitöltése kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('select * from musorujsag.szereplok where szereploid="{}"'.format(jatszik_e_szereploid.get()))
            szereploid_check = 0
            for row in cursor:
                szereploid_check += 1
            cursor.execute('select * from musorujsag.musorok where musorid="{}"'.format(jatszik_e_musorid.get()))
            musorid_check = 0
            for row in cursor:
                musorid_check += 1
            con.close()
            if szereploid_check == 0 and musorid_check == 0:
                MessageBox.showinfo("Info", "Nem létezik ilyen ID-val Szereplő illetve Műsor sem! Próbáld újra!")
            elif szereploid_check == "":
                MessageBox.showinfo("Info", "Nem létezik ilyen ID-val Szereplő! Próbáld újra!")
            elif musorid_check == "":
                MessageBox.showinfo("Info", "Nem létezik ilyen ID-val Műsor! Próbáld újra!")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('insert into musorujsag.jatszik values("{}","{}")'.format(jatszik_e_musorid.get(), jatszik_e_szereploid.get()))
                cursor.execute('commit')
                jatszik_e_szereploid.delete(0, 'end')
                jatszik_e_musorid.delete(0, 'end')
                MessageBox.showinfo('Info', 'Sikeres beszúrás!')
                con.close()
                j_show()

    def j_delete():
        if jatszik_e_szereploid.get() == "" or jatszik_e_musorid.get() =="":
            MessageBox.showinfo("Info", "Minden mezőt adj meg!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('select * from musorujsag.szereplok where szereploid="{}"'.format(jatszik_e_szereploid.get()))
            szereploid_check = 0
            for row in cursor:
                szereploid_check += 1
            cursor.execute('select * from musorujsag.musorok where musorid="{}"'.format(jatszik_e_musorid.get()))
            musorid_check = 0
            for row in cursor:
                musorid_check += 1
            con.close()
            if szereploid_check == 0 and musorid_check == 0:
                MessageBox.showinfo("Info", "Nem létezik ilyen Szereplő ID illetve Műsor ID!")
            elif szereploid_check == 0:
                MessageBox.showinfo("Info", "Nem létezik ilyen Szereplő ID!")
            elif musorid_check == 0:
                MessageBox.showinfo("Info", "Nem létezik ilyen Műsor ID!")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('delete from musorujsag.jatszik where musorid="{}" and szereploid="{}"'.format(jatszik_e_musorid.get(), jatszik_e_szereploid.get()))
                cursor.execute('commit')
                jatszik_e_musorid.delete(0, 'end')
                jatszik_e_szereploid.delete(0, 'end')
                MessageBox.showinfo("Info", "Sikeresen töröltél!")
                con.close()
                j_show()

    def j_show():
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from musorujsag.jatszik')
        rows = cursor.fetchall()
        list.delete(0, list.size())
        for row in rows:
            insertData = '{} - {}'.format(row[0], row[1])
            list.insert(list.size() + 1, insertData)
        con.close()

    j_xhely = 350
    j_yhely = 10

    jatszik_cim = tk.Label(root, text='Játszik', font=('bold', 15), bg='moccasin')
    jatszik_cim.place(x=j_xhely, y=j_yhely)

    jatszik_musorid = tk.Label(root, text='Műsor ID:', font=('bold', 10), bg='antiquewhite2', highlightthickness=2)
    jatszik_musorid.place(x=j_xhely, y=j_yhely + 40)
    jatszik_e_musorid = tk.Entry(highlightthickness=2, highlightcolor='black')
    jatszik_e_musorid.place(x=j_xhely + 130, y=j_yhely + 43)

    jatszik_szereploid = tk.Label(root, text='Szereplő ID:', font=('bold', 10), bg='antiquewhite2', highlightthickness=2)
    jatszik_szereploid.place(x=j_xhely, y=j_yhely + 70)
    jatszik_e_szereploid = tk.Entry(highlightthickness=2, highlightcolor='black')
    jatszik_e_szereploid.place(x=j_xhely + 130, y=j_yhely + 73)

    jatszik_insert_button = tk.Button(root, text=' Beszúr ', font=('italic', 10), bg='antiquewhite', command=j_insert)
    jatszik_insert_button.place(x=j_xhely, y=j_yhely + 140)

    jatszik_delete_button = tk.Button(root, text="Törlés", font=('italic', 10), bg="brown3", command=j_delete)
    jatszik_delete_button.place(x=j_xhely + 65, y=j_yhely + 140)

    jatszik_show_button = tk.Button(root, text="Össz.", font=('italic', 10), bg="olivedrab", command=j_show)
    jatszik_show_button.place(x=j_xhely + 115, y=j_yhely + 140)

    #ÖSSZETETT LEKÉRDEZÉSEK

    osszetett_cim = tk.Label(root, text='Összetett lekérdezések', font=('bold', 15), bg='moccasin')
    osszetett_cim.place(x=300, y=468)

    #MELYIK MUSORT MELYIK CSATORNA ADJA

    def musortkozvetit():
        if musorok_e_id.get() == "":
            MessageBox.showinfo("Info", "Műsor ID mező kötelező")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('SELECT m.cim, GROUP_CONCAT(DISTINCT tv.nev) FROM musorujsag.musorok as m INNER JOIN musorujsag.kozvetit as k ON k.m_musorid = m.musorid INNER JOIN musorujsag.tvcsatornak as tv ON tv.csatornaid = k.tv_csatornaid WHERE m.musorid="{}" GROUP BY m.musorid;'.format(musorok_e_id.get()))
            rows = cursor.fetchall()
            list.delete(0, list.size())
            for row in rows:
                insertData = '{}--{}'.format(row[0], row[1])
                list.insert(list.size() + 1, insertData)
            con.close()

    musortkozvetit_button = tk.Button(root, text="Közvetít", font=('italic', 10), bg="antiquewhite", command=musortkozvetit)
    musortkozvetit_button.place(x=300, y=628)

    #LEGIDŐSEBB SZEREPLŐ

    def legidosebb():
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('SELECT sz.nev, m.cim, sz.szuletesiido FROM  musorok AS m INNER JOIN jatszik AS j ON j.musorid = m.musorid RIGHT JOIN szereplok AS sz ON sz.szereploid = j.szereploid WHERE sz.szuletesiido = (SELECT MIN(DATE(szereplok.szuletesiido)) FROM szereplok);')
        rows = cursor.fetchall()
        list.delete(0, list.size())
        for row in rows:
            insertData = '{} - {} - {}'.format(row[0], row[1], row[2])
            list.insert(list.size() + 1, insertData)
        con.close()

    legidosebb_button = tk.Button(root, text="Legidősebb szereplő", font=('italic', 10), bg="antiquewhite", command=legidosebb)
    legidosebb_button.place(x=300, y=568)

    #LEGFIATALABB SZEREPLŐ

    def legfiatalabb():
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('SELECT sz.nev, m.cim, sz.szuletesiido FROM  musorok AS m INNER JOIN jatszik AS j ON j.musorid = m.musorid RIGHT JOIN szereplok AS sz ON sz.szereploid = j.szereploid WHERE sz.szuletesiido = (SELECT MAX(DATE(szereplok.szuletesiido)) FROM szereplok);')
        rows = cursor.fetchall()
        list.delete(0, list.size())
        for row in rows:
            insertData = '{} - {} - {}'.format(row[0], row[1], row[2])
            list.insert(list.size() + 1, insertData)
        con.close()

    legfiatalabb_button = tk.Button(root, text="Legfiatalabb szereplő", font=('italic', 10), bg="antiquewhite", command=legfiatalabb)
    legfiatalabb_button.place(x=300, y=538)

    #MŰSORSZÁMLÁLÓ

    def mosszegzo():
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('SELECT tv.csatornaid, tv.nev, COUNT(DISTINCT m.musorid) FROM tvcsatornak AS tv INNER JOIN kozvetit AS k ON k.tv_csatornaid = tv.csatornaid INNER JOIN musorok AS m ON m.musorid = k.m_musorid GROUP BY tv.csatornaid;')
        rows = cursor.fetchall()
        list.delete(0, list.size())
        for row in rows:
            insertData = 'A(z) {}. ID-s, {} nevű csatornán közvetített műsorok száma: {}db'.format(row[0], row[1], row[2])
            list.insert(list.size() + 1, insertData)
        con.close()

    mosszegzo_button = tk.Button(root, text="Műsorszámláló", font=('italic', 10), bg="antiquewhite", command=mosszegzo)
    mosszegzo_button.place(x=300, y=598)

    #LEGHOSSZABB MUSOR

    def leghosszabbm():
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('SELECT m.cim, m.tipus, m.hossz, GROUP_CONCAT(DISTINCT tv.nev) FROM musorujsag.musorok AS m INNER JOIN musorujsag.kozvetit AS k ON k.m_musorid = m.musorid INNER JOIN tvcsatornak AS tv ON tv.csatornaid = k.tv_csatornaid WHERE m.hossz = (SELECT MAX(musorok.hossz) FROM musorok) GROUP BY m.musorid;')
        rows = cursor.fetchall()
        list.delete(0, list.size())
        for row in rows:
            insertData = '{} - {} - {}'.format(row[0], row[1], row[2])
            list.insert(list.size() + 1, insertData)
        con.close()

    leghosszabbm_button = tk.Button(root, text="Leghosszabb műsor(ok)", font=('italic', 10), bg="antiquewhite", command=leghosszabbm)
    leghosszabbm_button.place(x=300, y=508)

    list = tk.Listbox(root, bg='antiquewhite', highlightthickness=2, highlightcolor='black')
    list.config(width=100, height=14)
    list.place(x=300, y=207)

    root.mainloop()