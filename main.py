import sqlite3
db=sqlite3.connect('db.db')
db.execute('create table if not exists PRODUCTOS(COLLECION,ENLACE,NOMBRE,PRECIO float,IMAGEN)')
from streamlit import *
contactos={'YOUTUBE':'https://www.youtube.com/@Tommys-jy9oq','FACEBOOK':'https://www.facebook.com/profile.php?id=61557025805896','INSTAGRAM':'https://www.instagram.com/tommys_amazon'}
col1,col2,col3,col4=columns([100,400,500,300])
with col1:image('imagenes/amazon.png',width=100)
with col2:image('imagenes/logo.png',width=200)
with col3:title("Tommy's Amazon's choices")
with col4:
    for label,enlace in contactos.items():link_button(label=label,url=enlace)
casa_inteligente,ebooks,hogar,mascotas,moda,oficina,salud_y_belleza=tabs([tab[0] for tab in db.execute('select COLLECION from PRODUCTOS group by COLLECION').fetchall()])
db.close()
def muestra(collecion):
    c= container()
    db=sqlite3.connect('db.db')
    for producto in db.execute('select * from PRODUCTOS where COLLECION=?',(collecion,)).fetchall():
        with c:
            markdown(f':blue-background[{producto[2]}]')
            markdown(f':blue-background[€. {str(producto[3]).zfill(2)}]')
            image(producto[4])
            link_button('VER TODO',url=producto[1])
            markdown('-' * len(producto[2]))
    db.close()
with casa_inteligente:muestra('CASA INTELIGENTE')
with ebooks:muestra('EBOOKS')
with hogar:muestra('HOGAR')
with mascotas:muestra('MASCOTAS')
with moda:muestra('MODA')
with oficina:muestra('OFICINA')
with salud_y_belleza:muestra('SALUD Y BELLEZA')
