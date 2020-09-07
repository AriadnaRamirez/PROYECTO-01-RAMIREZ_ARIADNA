from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches #Listas importadas
usuarios = [
["lifestore", "1234"],
["ls_ventas", "2567"],
["ls_invitado", "1234"]
] #Usuarios permitidos para ingresar

ventas_productos=[]
mayor_venta=[]
vector_producto_bsuquedas=[]
busquedas_productos=[]

print('Bienvendo a la plataforma de análisis de rotación de LIFE STORE \n \n')
print("* * * * * * * * * * * *   L O G    I N   * * * * * * * * * * *\n\n")

intento=0
while intento <3: #ciclo que permite tres intentos de inicio de sesión
  intento+=1

  usuario_login = input("Ingresa tu usuario: ")
  pasword = input("Ingresa tu contraseña:")
  
  entrada=False
  for usuario in usuarios:
    if usuario_login == usuario[0] and pasword == usuario[1]:
      entrada=True
      intento=3 #Si el usuario y contraseña son correctos, permite la entrada al programa y cierra el ciclo de intentos
   

  if intento<3: 
    print("\nLos datos de inicio de sesión son incorrectos")
    print("\n------ Te quedan",3-intento, "intentos de inicio de sesión ------\n") #Si los datos de inicio de sesion son incorrectos, te muestra cuantos intentos de inicio de sesion te restan
  else:
    if entrada == False:
      print("\n****Agotaste el numero de intentos maximo de inicio de sesión****") #Si agotas el numero de intentos maximo de inicio de sesión
    else:
      print("\nHOLA!",usuario_login,"BIENVENIDO")
      entrada=1#Si permite la entrada


intento=0


while intento <3:#permite elegor entre tres opciones (a,b,c), en un maximo de tres intentos

  if entrada == 1:
    print ("\n\n¿Qué deseas hacer?\n")
    print("   a)Ver productos más vendidos y más rezagados\n   b)Ver productos por reseña de servicio\n   c)Ver reporte de ingresos\n")
    opcion=input("Opción: ")
    intento+=1

  if opcion == "a": #inicia el sub menu a
    intento=3
    print("\nHas elegido: Ver productos más vendidos y más rezagados")

    #Genera una lista que contiene el id del producto, su nombre, las ventas del producto y su categoria
    #Posteriormente ordena por mayores ventas

    for id_busqueda in lifestore_products:
      ventas_prod=0    
      for id_coincidencia in lifestore_sales:
        if id_coincidencia[1]==id_busqueda[0]:
          ventas_prod+=1
          vector_producto_ventas=[id_busqueda[0],id_busqueda[1],ventas_prod,id_busqueda[3]]
       
        else:
          ventas_prod+=0
          vector_producto_ventas=[id_busqueda[0],id_busqueda[1],ventas_prod,id_busqueda[3]]

      ventas_productos.append(vector_producto_ventas)
      vector_ventas=[]
      total=0
      for venta in ventas_productos:        
        total+=1
        vector_ventas.append(venta[2])    
      vector_ventas.sort()   


      #Genera una lista de ventas eliminando duplicados
      ventas_corto=[]  
      for indice in range (0,total): 
        if vector_ventas[indice] != vector_ventas[indice-1]:
          ventas_corto.append(vector_ventas[indice])

      
      ventas_ordenadas=[]
      for ventas in ventas_corto:
        for orden in ventas_productos:
        
          if orden[2]==ventas:
            ventas_ordenadas.append(orden)
      
    print("\n5 0   P  R  O  D  U  C  T  O  S     M  Á  S     V  E  N  D  I  D  O  S ")

    print("\nN\tID_PRODUCT \t SALES \t NAME_PRODUCT\n------------------------------------------------------------------------------------------------------------\n")
    #Imprime los 50 poductos mas vendidos y les da formato de tabla
    for indice in range(1,51):
      if int(ventas_ordenadas[-indice][0]/10) >0:
        print(indice,"\t\t",ventas_ordenadas[-indice][0],"\t ",ventas_ordenadas[-indice][2],"\t",ventas_ordenadas[-indice][1],"\n")
      else:  
        print(indice,"\t\t",ventas_ordenadas[-indice][0],"\t\t ",ventas_ordenadas[-indice][2],"\t",ventas_ordenadas[-indice][1],"\n")



    #100 prod con mayor busqueda
    for id_busqueda in lifestore_products:
      busqueda_prod=0
    
      for id_coincidencia in lifestore_searches:
        if id_coincidencia[1]==id_busqueda[0]:
          busqueda_prod+=1
          vector_producto_bsuquedas=[id_busqueda[0],id_busqueda[1],busqueda_prod,id_busqueda[3]]
        else:
          busqueda_prod+=0
          vector_producto_ventas=[id_busqueda[0],id_busqueda[1],busqueda_prod,id_busqueda[3]]
      busquedas_productos.append(vector_producto_ventas)
    


      vector_busqueda=[]
      total=0
      for busqueda in busquedas_productos:
          
        total+=1
        vector_busqueda.append(busqueda[2])    
      vector_busqueda.sort()
    


     
      busqueda_corto=[]  
      for indice in range (0,total): 
        if vector_busqueda[indice] != vector_busqueda[indice-1]:
          busqueda_corto.append(vector_busqueda[indice])
     

      busquedas_ordenadas=[]
      for busqueda in busqueda_corto:
        for orden in busquedas_productos:
        
          if orden[2]==busqueda:
            busquedas_ordenadas.append(orden)
      
    print("\n5 0   P  R  O  D  U  C  T  O  S    C  O  N     M  Á  S     B  U  S  Q  U  E  D  A  S ")

    print("\nN\tID_PRODUCT \t SEARCHES \t NAME_PRODUCT\n------------------------------------------------------------------------------------------------------------\n")
    for indice in range(1,51):
      if int(busquedas_ordenadas[-indice][0]/10) >0:
        print(indice,"\t\t",busquedas_ordenadas[-indice][0],"\t   ",busquedas_ordenadas[-indice][2],"\t\t",busquedas_ordenadas[-indice][1],"\n")
      else:  
        print(indice,"\t\t",busquedas_ordenadas[-indice][0],"\t\t   ",busquedas_ordenadas[-indice][2],"\t\t",busquedas_ordenadas[-indice][1],"\n")
    
    ##################### POR CATEGORIA ##############
    
    print("\n\n P  R  O  D  U  C  T  O  S     M  E  N  O  S     V  E  N  D  I  D  O  S  ")
    vector_categorias=[]
    total=0
  
    for category in ventas_ordenadas:       
      total+=1
      vector_categorias.append(category[3])    
     

    categorias_corto=[]  
    for categoria in ventas_ordenadas: 
      if categoria[3] not in categorias_corto:
        categorias_corto.append(categoria[3])
        
    

    for categoria in categorias_corto:
      categoria_mayusc=categoria.upper()
      print("\n",categoria_mayusc)
      print("\nN\tID_PRODUCT \t SALES \t CATEGORY \t\t\t  NAME_PRODUCT\n------------------------------------------------------------------------------------------------------------\n")
      categorias_ordenadas=[]  
      productos_por_categoria=0
      for orden in ventas_ordenadas:
        if orden[3]==categoria:
          categorias_ordenadas.append(orden)
          productos_por_categoria+=1
      for indice in range(0,int(productos_por_categoria/2)):
        if int(categorias_ordenadas[-indice][0]/10) >0:
          print(indice,"\t\t",categorias_ordenadas[indice][0],"\t",categorias_ordenadas[indice][2],"\t\t",categorias_ordenadas[indice][3],"\t\t",categorias_ordenadas[indice][1],"\n")
        else:
          print(indice,"\t\t",categorias_ordenadas[indice][0],"\t\t",categorias_ordenadas[indice][2],"\t\t",categorias_ordenadas[indice][3],"\t\t",categorias_ordenadas[indice][1],"\n")
    print("\n\n P  R  O  D  U  C  T  O  S     M  E  N  O  S     B  U  S  C  A  D  O  S ")
  
    
    for categoria in categorias_corto:
      categoria_mayusc=categoria.upper()
      print("\n",categoria_mayusc)
      print("\nN\tID_PRODUCT \t SALES \t CATEGORY \t\t\t  NAME_PRODUCT\n------------------------------------------------------------------------------------------------------------\n")
      categorias_ordenadas=[]  
      productos_por_categoria=0
      for orden in busquedas_ordenadas:
        if orden[3]==categoria:
          categorias_ordenadas.append(orden)
          productos_por_categoria+=1

      for indice in range(0,int(productos_por_categoria/2)):
        if int(categorias_ordenadas[-indice][0]/10) >0:
          print(indice,"\t\t",categorias_ordenadas[indice][0],"\t",categorias_ordenadas[indice][2],"\t\t",categorias_ordenadas[indice][3],"\t\t",categorias_ordenadas[indice][1],"\n")
        else:
          print(indice,"\t\t",categorias_ordenadas[indice][0],"\t\t",categorias_ordenadas[indice][2],"\t\t",categorias_ordenadas[indice][3],"\t\t",categorias_ordenadas[indice][1],"\n")



  elif opcion=="b":
    ############### PRODUCTOS POR RESEÑA DE SERVICIO ##############
    #Mostrar dos listados de 20 productos cada una, un listado para productos con las mejores reseñas y otro para las peores, considerando los productos con devolución.      
    intento=3
    print("\nHas elegido: Ver productos por reseña de servicio")
    for id_busqueda in lifestore_products:
      ventas_prod=0
      reseña=0
      devolucion:0
    
      for id_coincidencia in lifestore_sales:
        if id_coincidencia[1]==id_busqueda[0]:
          
          ventas_prod+=1
          reseña+=id_coincidencia[2]
          promedio_reseña=round(reseña/ventas_prod,1)
          vector_producto_ventas=[id_busqueda[0],id_busqueda[1],promedio_reseña]
      
        else:
          ventas_prod+=0
          reseña+=0
          vector_producto_ventas=[id_busqueda[0],id_busqueda[1],promedio_reseña]
      ventas_productos.append(vector_producto_ventas)

      vector_ventas=[]
      total=0
      for venta in ventas_productos:
         
        total+=1
        vector_ventas.append(venta[2])    
      vector_ventas.sort()
    
      ventas_corto=[]  
      for indice in range (0,total): 
        if vector_ventas[indice] != vector_ventas[indice-1]:
          ventas_corto.append(vector_ventas[indice])
      
      reseñas_ordenadas=[]
      for ventas in ventas_corto:
        for orden in ventas_productos:
        
          if orden[2]==ventas:
            reseñas_ordenadas.append(orden)
      
    print("\n2 0   P  R  O  D  U  C  T  O  S     C  O  N     M  E  J  O  R    R  E  S  E  Ñ  A ")

    print("\nN\tID_PRODUCT \t RESEÑA \t NAME_PRODUCT\n------------------------------------------------------------------------------------------------------------\n")
    for indice in range(1,21):
      if int(reseñas_ordenadas[-indice][0]/10) >0:
        print(indice,"\t\t",reseñas_ordenadas[-indice][0],"\t ",reseñas_ordenadas[-indice][2],"★\t\t",reseñas_ordenadas[-indice][1],"\n")
      else:  
        print(indice,"\t\t",reseñas_ordenadas[-indice][0],"\t\t ",reseñas_ordenadas[-indice][2],"★\t\t",reseñas_ordenadas[-indice][1],"\n")

    print("\n2 0   P  R  O  D  U  C  T  O  S     C  O  N     P  E  O  R    R  E  S  E  Ñ  A ")

    print("\nN\tID_PRODUCT \t RESEÑA \t NAME_PRODUCT\n------------------------------------------------------------------------------------------------------------\n")
    for indice in range(0,20):
      if int(reseñas_ordenadas[-indice][0]/10) >0:
        print(indice+1,"\t\t",reseñas_ordenadas[indice][0],"\t ",reseñas_ordenadas[indice][2],"☆\t\t",reseñas_ordenadas[indice][1],"\n")
      else:  
        print(indice+1,"\t\t",reseñas_ordenadas[indice][0],"\t\t ",reseñas_ordenadas[indice][2],"☆\t\t",reseñas_ordenadas[indice][1],"\n")      

  elif opcion=="c":
    ################### INGRESOS ####################
    #Total de ingresos y ventas promedio mensuales,total anual y meses con más ventas al año      
    intento=3
    print("\nHas elegido: Ver reporte de ingresos")  
    
    ventas_productos=[]
    for id_busqueda in lifestore_products:
      ventas_prod=0
    
      for id_coincidencia in lifestore_sales:
        if id_coincidencia[1]==id_busqueda[0]:
          ventas_prod+=1          
          total_ventas=ventas_prod*id_busqueda[2]
          vector_producto_ventas=[id_busqueda[0],total_ventas,id_busqueda[1]]
          
        else:
          ventas_prod+=0
          total_ventas=ventas_prod*id_busqueda[2]
          vector_producto_ventas=[id_busqueda[0],total_ventas,id_busqueda[1]]
      ventas_productos.append(vector_producto_ventas)
      
      vector_mes=[]
      meses_completos=[]
      mes_para_organizar=[]
      total=0
      
    for fecha in lifestore_sales:            
        total+=1
        mes=int(fecha[3][3]+fecha[3][4])
        vector_mes.append(mes)
        for venta in lifestore_products:            
          elemento=[venta[0],venta[1],mes]                
          if venta[0]==fecha[1]:
            mes_para_organizar.append(elemento)                    
    vector_mes.sort()  

    fechas_corto=[]  
    for indice in range (0,total): 
      if vector_mes[indice] != vector_mes[indice-1]:
        fechas_corto.append(vector_mes[indice])
      
    total_ventas=0
    for ventas in ventas_productos:
      total_ventas+=float(ventas[1])
    print("\n ➟  TOTAL VENTAS: $ {:,.2f}".format(total_ventas))
    
    
  else:
    if intento <3:
      print("\nLa opción que has elegido es incorrecta, intenta con a) b) o c)")
      print("\n------ Te quedan",3-intento, "intentos de inicio de sesión ------\n")
    else:
      print("\n-Has agotado el numero de intentos de elección en el menú-")
        




      








