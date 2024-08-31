import webbrowser,sqlite3,base64,os
db=sqlite3.connect('db.db')
db.execute('create table if not exists PRODUCTOS(COLLECION,ENLACE,NOMBRE,PRECIO float,IMAGEN)')
contactos=[]
for file in os.listdir('imagenes/contactos/'):
    with open('imagenes/contactos/'+file,'rb') as imagen:contactos.append('data:image/png;base64,{}'.format(base64.b64encode(imagen.read()).decode()))
from streamlit import *
from st_clickable_images import clickable_images
col1,col2,col3,col4=columns([100,400,500,300])
with col1:image('imagenes/amazon.png',width=100)
with col2:image('imagenes/logo.png',width=200)
with col3:title("Tommy's Amazon's choices")
with col4:contacto=clickable_images(contactos,img_style={'height':'100px'})
if contacto==0:webbrowser.open_new_tab('https://www.youtube.com/@Tommys-jy9oq')
elif contacto == 1: webbrowser.open_new_tab('https://www.facebook.com/profile.php?id=61557025805896')
elif contacto == 2: webbrowser.open_new_tab('https://www.instagram.com/tommys_amazon')
casa_inteligente,ebooks,hogar,mascotas,moda,oficina,salud_y_belleza=tabs([tab[0] for tab in db.execute('select COLLECION from PRODUCTOS group by COLLECION').fetchall()])
def compra(enlace):
    webbrowser.open_new_tab(enlace)
def muestra(collecion):
    c= container()
    for producto in db.execute('select * from PRODUCTOS where COLLECION=?',(collecion,)).fetchall():
        with c:
            markdown(f':blue-background[{producto[2]}]')
            markdown(f':blue-background[€. {str(producto[3]).zfill(2)}]')
            image(producto[4])
            button('VER TODO', key=producto[1], on_click=lambda enlace=producto[1]: compra(enlace))
            markdown('-' * len(producto[2]))
with casa_inteligente:muestra('CASA INTELIGENTE')
with ebooks:muestra('EBOOKS')
with hogar:muestra('HOGAR')
with mascotas:muestra('MASCOTAS')
with moda:muestra('MODA')
with oficina:muestra('OFICINA')
with salud_y_belleza:muestra('SALUD Y BELLEZA')
db.close()