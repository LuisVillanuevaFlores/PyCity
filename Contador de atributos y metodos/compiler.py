
code = open("input.py","r")
metodos=0
atributos=0
is_class=False
for linea in code.readlines():
    if("class" in linea):
        is_class =True
        elements=linea.split(" ")
        name_class=elements[1]
        if(":" in name_class):
            name_class=name_class.replace(":","")
            name_class=name_class.replace("\n","")
    num_tab = 0
    iterator = 0
    tab_size = 4
    while(iterator<=len(linea)):
        if(linea[iterator:iterator+tab_size]==' '*tab_size):
            num_tab+=1
        iterator+=4
    if(num_tab==1):
        if("def" in linea):
            metodos +=1
    if(num_tab==2):
        if("self." in linea and "=" in linea):
            atributos+=1
if(not is_class):
    print("No se encontro ninguna clase")
else:
    print("La clase",name_class,"tiene:")
    print("Atributos:",atributos)
    print("Metodos:",metodos)
code.close()