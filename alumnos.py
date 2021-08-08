class estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def verNombre(self):
        return self.nombre

    def verNota(self):
        return self.nota
    
    def nuevoNombre(self, nueNombre):
        self.nombre = nueNombre
    
    def nuevaNota(self, nueNota):
        self.nota = nueNota
    