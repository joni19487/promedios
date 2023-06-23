import pandas as pd


cuit='27279397385'
def corrector_comillas():
    nuevo=open('Mis Comprobantes Emitidos '+cuit+'.csv','w')
    try:
        g=open('Mis Comprobantes Emitidos - CUIT '+cuit+'.csv',"r")
        for dato in g.readlines():    
            if '"' in dato:
                dato= dato.replace('"','')        
                nuevo.write(str(dato))
    except:
        g=open('Mis Comprobantes Emitidos.csv',"r")
        for dato in g.readlines():    
            if '"' in dato:
                dato= dato.replace('"','')        
                nuevo.write(str(dato))

def resultado_mis_comprobantes():
    corrector_comillas()
    df = pd.read_csv('Mis Comprobantes Emitidos '+cuit+'.csv', encoding="latin-1")
    total=0
    for row, datos in df.iterrows():        
        tipo=datos[1]
        importe=float(datos['Imp. Total'])
        if tipo[5]=='F':
            total=importe+total
        elif tipo[5]=='N':
            importe=importe*-1
            total=importe+total
        
    return total
total=resultado_mis_comprobantes()

print(total)

