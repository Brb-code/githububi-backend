def responder_json(estado:int, mensaje:str, datos:object):
    # Estadarizacion de datos
    # Procesamiento de la variable datos
    
    
    a = datos
    data_estandarizada = {}
    #convetir lista de tuplas
    print(type(datos))
    if(isinstance(datos, list)):
        nueva_lista = []
        nombres = ("id_usuario", "nombre", "password","email","cuenta_github","celular")
        for x in datos:
            nueva_lista.append(dict(zip(nombres, x)))
        data_estandarizada = nueva_lista            
    if(isinstance(datos, tuple)):
        nombres = ("id_usuario", "nombre", "password","email","cuenta_github","celular")
        data_estandarizada = dict(zip(nombres, datos))        
    else:
        print("otro tipo de datos")
    

    
    return {
        "status":estado,
        "mensaje":mensaje,
        "datos": data_estandarizada
    }

def responder_html():
    return {}

def responder_pdf():
    return {}