import os
#a append
#x create
#w write
#r read
class main:
    dirfile=os.getcwd()+'/'
    defectfile='texto.txt'
    file=''
    def readFile(self):
        fileName=str(input('Nombre del archivo a leer: '))
        ficherList=os.listdir()
        if fileName+'.txt' in ficherList:
            self.file=open(self.dirfile+fileName+'.txt','r')
            ficherReader=self.file.read()
            print(ficherReader)
            self.file.close()
            return
        print("Fichero no encontrado")
        
    def writeFile(self):
        ask= str(input('Quieres crear otro arcchivo o usar el por defecto? si / no:  '))
        if ask.lower() == 'si':
            filename=str(input('nombre del archivo:  '))
            print(filename)
            self.file=open(self.dirfile+filename,'w')
        else:
            self.file=open(self.dirfile+self.defectfile,'w')
        content = str(input('escribe el contenido: '))
        textsplitespace=content.split('.')
        for line in textsplitespace:
            self.file.write(line+os.linesep)

        self.file.close()
        self.file=''
    
            
mifile= main()
mifile.writeFile()
mifile.readFile()


