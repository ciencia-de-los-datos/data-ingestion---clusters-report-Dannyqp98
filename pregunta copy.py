"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    #
    # Inserte su código aquí
    #
    data=[]
    i=0
    current_line=0
    head_pos=[]
    with open('clusters_report.txt',mode='r') as file:
        for line in file:
            
            localization=0
            if i==0:
                header=line
                for nchar in line:
                    if nchar=='\n':
                        break
                    #print(nchar)
                    pos=localization if (nchar!='' and nchar!=' ' and line[localization-1]==' ' and line[localization-2]==' ') else -1
                    if (nchar!='' and localization==0):
                        pos=localization
                    
                    localization=localization+1
                    head_pos.append(pos) if pos!=-1 else None
            i=i+1
            n_index=len(head_pos)
            n_data_element=0
            lista=[]
            for element in head_pos :
                if line[0]!='-' and len(line)>5:#head_pos[-1] :
                    CL=line
                    line=CL
                    if n_data_element<(n_index-1 ):
                        lista.append(line[head_pos[n_data_element]:head_pos[n_data_element+1]].strip()) 
                        
                    if n_data_element==(n_index-1 ):
                        lista.append(line[head_pos[-1]:].strip())
                    

                n_data_element=n_data_element+1
            
            data.append(lista) if len(lista)>0 else None

        index=0
        header=[]
        for field in data[0]:
            header.append(field+' '+data[1][index])
            index=index+1

        data[0:2]=[header]
        
        index=1
        lines=[]
        current_line=1
        concat_line=[]
        corp=[]
        for row in data[1:]:
            
            corp.append(concat_line) if (row[-1]!='' and row[1]!='') else None
            concat_line=row if (row[0]!='') else concat_line
            if (len(row[-1].join(row))==0) :
                data.pop(index) 
            else:
                nfield=0
           
            
                for field in row:
                    if row[0]=='':
                        concat_line[nfield]=concat_line[nfield]+' '+field
                        nfield=nfield+1
            
                
                

                current_line=index if (row[0]!='') else current_line
            index=index+1

            if (index!=current_line and row[0]!=''):
                data[current_line-1:index]=[concat_line]
                #index=current_line+1
            

       
    return df
