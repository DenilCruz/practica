from ClaseNodo import ClaseNodo
from collections import deque

class ArbolBinario:

    def __init__(self):
        self._raiz = None

    '''
    nota:inserta un nuevo valor en el árbol binario de búsqueda.
    argumentos: recibe un numero entero
    retorna: nada, pero actualiza la raíz del árbol. 
    '''

    def insertar(self, valor):
        self._raiz = self._insertarRecursivo(self._raiz, valor)

    '''
    nota: función auxiliar recursiva que busca la posición correcta
          e inserta el nuevo valor dentro del árbol binario de búsqueda.
    argumentos: 
        - raizAux: nodo actual (puede ser None si llegamos a un lugar vacío).
        - valor: número entero que se quiere insertar.
    retorna: 
        - un objeto ClaseNodo que representa la raíz del subárbol modificado.
    '''

    def _insertarRecursivo(self, raizAux, valor):
        #Caso Base
        if raizAux is None:
            raizAux = ClaseNodo(valor)
            return raizAux
        else:
            if valor < raizAux.getValor():
                raizAux.setHijoIzquierdo(self._insertarRecursivo(raizAux.getHijoIzquierdo(), valor))
            else:
                raizAux.setHijoDerecho(self._insertarRecursivo(raizAux.getHijoDerecho(), valor))
            return raizAux
    """
    Nota:Inserta un nuevo nodo en el árbol binario.
    Argumentos:
        valor: El valor que se desea insertar en el árbol.
    Retorna:
        None. (El método no retorna nada, solo modifica la estructura del árbol).
    """
    def insertarIterativo(self, valor):
        nuevoNodo = ClaseNodo(valor)
        if self._raiz is None:
            self._raiz = nuevoNodo
            return
        nodoActual = self._raiz
        while True:
            if valor < nodoActual.getValor():
                if nodoActual.getHijoIzquierdo() is None:
                    nodoActual.setHijoIzquierdo(nuevoNodo)
                    return
                nodoActual = nodoActual.getHijoIzquierdo()
            else:
                if nodoActual.getHijoDerecho() is None:
                    nodoActual.setHijoDerecho(nuevoNodo)
                    return
                nodoActual = nodoActual.getHijoDerecho()

                

    '''
    nota: verifica si el árbol está vacío.
    argumentos: ninguno.
    retorna: True si la raíz es None (árbol vacío), False en caso contrario.
    '''
    def isVacio(self):
        return self._raiz is None
    


    '''
    nota: determina si un nodo es hoja (no tiene hijos).
    argumentos: 
        - nodo: objeto de tipo ClaseNodo.
    retorna: True si el nodo no tiene hijos izquierdo ni derecho,
             False en caso contrario.
    '''
    def esHoja(self, nodo):
        return nodo.getHijoIzquierdo() == None and nodo.getHijoDerecho() == None
    

    """
    Nota:Busca un valor en el árbol binario de búsqueda.
    Argumentos:
        valor (int): El valor que se desea buscar en el árbol.
    Retorna:
        bool: True si el valor se encuentra en el árbol, False en caso contrario.
    """
    def buscar(self, valor):
        return self._buscarRecursivo(self._raiz, valor)
    
    """
    Nota:Función auxiliar recursiva para realizar la búsqueda en el árbol.
    Argumentos:
        nodo (ClaseNodo | None): El nodo actual del árbol desde donde se realiza la búsqueda.
        valor (int): El valor que se desea buscar.
    Retorna:
        bool: True si el valor está en el subárbol a partir del nodo dado,
              False si no se encuentra.
    """
    def _buscarRecursivo(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.getValor() == valor:
            return True
        elif valor < nodo.getValor():
            return self._buscarRecursivo(nodo.getHijoIzquierdo(), valor)
        else:
            return self._buscarRecursivo(nodo.getHijoDerecho(), valor)
    
    """
    Nota:Busca un valor en el árbol binario de búsqueda de forma iterativa.
    Argumentos:
        valor (int): El valor que se desea buscar en el árbol.
    Retorna:
        bool: True si el valor se encuentra en el árbol, False en caso contrario.
    """
    def buscarIterativo(self, valor):
        nodoActual = self._raiz
        while nodoActual is not None:
            if nodoActual.getValor() == valor:
                return True
            elif valor < nodoActual.getValor():
                nodoActual = nodoActual.getHijoIzquierdo()
            else:
                nodoActual = nodoActual.getHijoDerecho()
        return False
    
    
    """
    nota:Recorre el árbol binario de búsqueda en orden (in-order) de manera iterativa.
    Retorna:
        list[int]: Una lista con los valores del árbol en orden ascendente.
    """
    def inOrden(self):
        listado = []
        pila = []
        nodoActual = self._raiz

        while nodoActual is not None or pila:
            while nodoActual is not None:
                pila.append(nodoActual)
                nodoActual = nodoActual.getHijoIzquierdo()

            nodoActual = pila.pop()
            listado.append(nodoActual.getValor())
            
            nodoActual = nodoActual.getHijoDerecho()

        return listado
    

    """
    Recorre el árbol binario de búsqueda en orden (in-order) de manera recursiva.
    Retorna:
        list[int]: Una lista con los valores del árbol en orden ascendente.
    """
    def inOrdenRecursivo(self):
        listado = []
        self._inOrdenRecursivoAux(self._raiz, listado)
        return listado
    
    """
    Función auxiliar recursiva para recorrer el árbol en orden.
    Argumentos:
        nodo (ClaseNodo | None): Nodo actual del recorrido.
        listado (list[int]): Lista en la que se almacenan los valores recorridos.
    Retorna:
        None. (Modifica la lista `listado` directamente).
    """
    def _inOrdenRecursivoAux(self, nodo, listado):
        if nodo is not None:
            self._inOrdenRecursivoAux(nodo.getHijoIzquierdo(), listado)
            listado.append(nodo.getValor())
            self._inOrdenRecursivoAux(nodo.getHijoDerecho(), listado)


    """
    Recorre el árbol binario de búsqueda en postorden (post-order) de manera iterativa.
    Retorna:
        list[int]: Una lista con los valores del árbol en orden postorden.
    """
    def posOrden(self):
        listado = []
        if self._raiz is None:
            return listado

        pila1 = [self._raiz]
        pila2 = []

        while pila1:
            nodo = pila1.pop()
            pila2.append(nodo)

            if nodo.getHijoIzquierdo() is not None:
                pila1.append(nodo.getHijoIzquierdo())
            if nodo.getHijoDerecho() is not None:
                pila1.append(nodo.getHijoDerecho())

        while pila2:
            listado.append(pila2.pop().getValor())

        return listado


    """
    Recorre el árbol binario de búsqueda en postorden (post-order) de manera recursiva.
    Retorna:
        list[int]: Una lista con los valores del árbol en orden postorden.
    """
    def posOrdenRecursivo(self):
        listado = []
        self._posOrdenRecursivoAux(self._raiz, listado)
        return listado
    """
    Función auxiliar recursiva para recorrer el árbol en postorden.
    Argumentos:
        nodo (ClaseNodo | None): Nodo actual del recorrido.
        listado (list[int]): Lista en la que se almacenan los valores recorridos.
    Retorna:
        None. (Modifica directamente la lista `listado`).
    """
    def _posOrdenRecursivoAux(self, nodo, listado):
        if nodo is not None:
            self._posOrdenRecursivoAux(nodo.getHijoIzquierdo(), listado)
            self._posOrdenRecursivoAux(nodo.getHijoDerecho(), listado)
            listado.append(nodo.getValor())


    """
    Recorre el árbol binario de búsqueda en preorden (pre-order) de manera iterativa.
    Retorna:
        list[int]: Una lista con los valores del árbol en orden preorden.
    """
    def preOrden(self):
        listado = []
        if self._raiz is None:
            return listado

        pila = [self._raiz]

        while pila:
            nodo = pila.pop()
            listado.append(nodo.getValor())

            if nodo.getHijoDerecho() is not None:
                pila.append(nodo.getHijoDerecho())
            if nodo.getHijoIzquierdo() is not None:
                pila.append(nodo.getHijoIzquierdo())

        return listado
    

    """
    Recorre el árbol binario de búsqueda en preorden (pre-order) de manera recursiva.
    Retorna:
        list[int]: Una lista con los valores del árbol en orden preorden.
    """
    def preOrdenRecursivo(self):
        listado = []
        self._preOrdenRecursivoAux(self._raiz, listado)
        return listado
    """
    Función auxiliar recursiva para recorrer el árbol en preorden.
    Argumentos:
        nodo (ClaseNodo | None): Nodo actual del recorrido.
        listado (list[int]): Lista en la que se almacenan los valores recorridos.
    Retorna:
        None. (Modifica directamente la lista `listado`).
    """
    def _preOrdenRecursivoAux(self, nodo, listado):
        if nodo is not None:
            listado.append(nodo.getValor())
            self._preOrdenRecursivoAux(nodo.getHijoIzquierdo(), listado)
            self._preOrdenRecursivoAux(nodo.getHijoDerecho(), listado)

    """
    Calcula la altura del árbol binario de búsqueda de manera recursiva.
    Retorna: (int) La altura del árbol.
    """
    
    def altura(self):
        return self._alturaAux(self._raiz)
    """
    Función auxiliar recursiva para calcular la altura del árbol.
    Argumentos: nodo (ClaseNodo | None): Nodo actual del recorrido.
    Retorna: (int) La altura del árbol.
    """
    def _alturaAux(self, nodo):
        if nodo is None:
            return 0
        altura_izquierda = self._alturaAux(nodo.getHijoIzquierdo())
        altura_derecha = self._alturaAux(nodo.getHijoDerecho())
        return 1 + max(altura_izquierda, altura_derecha)
    
    """
    Funcion iterativa para contar nodos
    Retorna: (int) La cantidad de nodos en el árbol.
    """
    def alturaIt(self):
        alturaDelArbol = 0
        if not self.isVacio():
            cola = deque([self._raiz])
            while cola:
                cantNodosEnLaCola = len(cola)
                for _ in range(cantNodosEnLaCola):
                    nodoAux = cola.popleft()
                    if nodoAux.getHijoIzquierdo() is not None:
                        cola.append(nodoAux.getHijoIzquierdo())
                    if nodoAux.getHijoDerecho() is not None:
                        cola.append(nodoAux.getHijoDerecho())
                alturaDelArbol += 1
        return alturaDelArbol


    """
    Funcion recursiva para contar nodos
    Retorna: (int) La cantidad de nodos en el árbol.
    """
    def cantidadNodos(self):
        return self._cantidadNodosAux(self._raiz)

    """
    Funcion auxiliar recursiva para contar nodos
    Argumentos: nodo (ClaseNodo | None): Nodo actual del recorrido.
    Retorna: (int) La cantidad de nodos en el árbol.
    """
    def _cantidadNodosAux(self, nodo):
        if nodo is None:
            return 0
        cantidad_izquierda = self._cantidadNodosAux(nodo.getHijoIzquierdo())
        cantidad_derecha = self._cantidadNodosAux(nodo.getHijoDerecho())
        return 1 + cantidad_izquierda + cantidad_derecha

    """
    Funcion iterativa para contar nodos
    Retorna: (int) La cantidad de nodos en el árbol.
    """
    def cantidadNodosIt(self):
        if self.isVacio():
            return 0
        cantidad = 0
        cola = deque([self._raiz])
        while cola:
            nodo = cola.popleft()
            cantidad += 1
            if nodo.getHijoIzquierdo() is not None:
                cola.append(nodo.getHijoIzquierdo())
            if nodo.getHijoDerecho() is not None:
                cola.append(nodo.getHijoDerecho())
        return cantidad


    """
    Realiza un recorrido por amplitud (nivel por nivel) del árbol binario.
    Retorna: (list[int]) Los valores de los nodos en el orden en que fueron visitados.
    """
    def amplitud(self):
        if self.isVacio():
            return []

        resultado = []
        cola = deque([self._raiz])

        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.getValor())

            if nodo.getHijoIzquierdo() is not None:
                cola.append(nodo.getHijoIzquierdo())
            if nodo.getHijoDerecho() is not None:
                cola.append(nodo.getHijoDerecho())

        return resultado


    """
    recorrido por niveles recursivo
    retorna: (list[int]) Los valores de los nodos en el orden en que fueron visitados.
    """
    def amplitudRecursivo(self):
        resultado = []
        h = self.altura() 

        for nivel in range(1, h + 1):
            self._amplitudRecursivoAux(self._raiz, nivel, resultado)

        return resultado
    """
    Funcion auxiliar para recorrer el árbol por niveles.
    Argumentos: nodo (ClaseNodo | None): Nodo actual del recorrido.
                nivel (int): Nivel actual del recorrido.
                resultado (list[int]): Lista para almacenar los valores de los nodos visitados.
    retorna: (list[int]) Los valores de los nodos en el orden en que fueron visitados.
    """
    def _amplitudRecursivoAux(self, nodo, nivel, resultado):
        if nodo is None:
            return
        if nivel == 1:
            resultado.append(nodo.getValor())
        elif nivel > 1:
            self._amplitudRecursivoAux(nodo.getHijoIzquierdo(), nivel - 1, resultado)
            self._amplitudRecursivoAux(nodo.getHijoDerecho(), nivel - 1, resultado)

    
    """
    Elimina un valor del árbol binario de búsqueda.
    Argumentos:
        valor (int): El valor a eliminar del árbol.
    Retorna:
        None. (El árbol se actualiza internamente).
    """
    def eliminar(self, valor):
        self._raiz = self._eliminarRecursivo(self._raiz, valor)

    """
    Función auxiliar recursiva para eliminar un nodo en el árbol.
    Argumentos:
        nodo (ClaseNodo | None): Nodo actual del recorrido.
        valor (int): El valor a eliminar.
    Retorna:
        ClaseNodo | None: La nueva referencia del subárbol después de la eliminación.
    """
    def _eliminarRecursivo(self, nodo, valor):
        if nodo is None:
            return None

        if valor < nodo.getValor():
            nodo.setHijoIzquierdo(self._eliminarRecursivo(nodo.getHijoIzquierdo(), valor))
        elif valor > nodo.getValor():
            nodo.setHijoDerecho(self._eliminarRecursivo(nodo.getHijoDerecho(), valor))
        else:
            # Caso 1: sin hijos
            if nodo.getHijoIzquierdo() is None and nodo.getHijoDerecho() is None:
                return None
            # Caso 2: un hijo
            elif nodo.getHijoIzquierdo() is None:
                return nodo.getHijoDerecho()
            elif nodo.getHijoDerecho() is None:
                return nodo.getHijoIzquierdo()
            # Caso 3: dos hijos
            else:
                sucesor = self._minValorNodo(nodo.getHijoDerecho())
                nodo.setValor(sucesor.getValor())
                nodo.setHijoDerecho(self._eliminarRecursivo(nodo.getHijoDerecho(), sucesor.getValor()))

        return nodo

    """
    Encuentra el nodo con el valor mínimo en un subárbol.
    Argumentos:
        nodo (ClaseNodo): Raíz del subárbol.
    Retorna:
        ClaseNodo: El nodo con el valor mínimo.
    """
    def _minValorNodo(self, nodo):
        actual = nodo
        while actual.getHijoIzquierdo() is not None:
            actual = actual.getHijoIzquierdo()
        return actual

    """
    Obtiene la raíz del árbol.
    Retorna: ClaseNodo | None: La raíz del árbol.
    """
    def getRaiz(self):
        return self._raiz
    
    def limpiarArbol(self):
        """Limpiar todo el árbol"""
        self._raiz = None

    def obtenerEstructuraVisual(self):
        """Obtener una representación visual simple del árbol"""
        if self.isVacio():
            return "Árbol vacío"
        return self._estructuraVisualRecursiva(self._raiz, "", True)

    def _estructuraVisualRecursiva(self, nodo, prefijo, esUltimo):
        if nodo is None:
            return ""
        
        resultado = prefijo + ("└── " if esUltimo else "├── ") + str(nodo.getValor()) + "\n"
        
        hijos = []
        if nodo.getHijoIzquierdo() is not None:
            hijos.append(("izq", nodo.getHijoIzquierdo()))
        if nodo.getHijoDerecho() is not None:
            hijos.append(("der", nodo.getHijoDerecho()))
        
        for i, (tipo, hijo) in enumerate(hijos):
            esUltimoHijo = i == len(hijos) - 1
            nuevoPrefijo = prefijo + ("    " if esUltimo else "│   ")
            resultado += self._estructuraVisualRecursiva(hijo, nuevoPrefijo, esUltimoHijo)
        
        return resultado
    
    def encontrarNivelesEspejoConteo(self):
        if self.isVacio():
            return {}, 0

        resultados_espejo = {}
        conteo_niveles_espejo = 0
        
        cola = deque([self._raiz])
        nivel_actual = 0

        while cola:
            cantidad_nodos_nivel = len(cola)
            valores_nivel_estructura = [] 
            valores_nivel_reales = []   
            proximo_nivel_existe = False 

            for _ in range(cantidad_nodos_nivel):
                nodo = cola.popleft()
                
                if nodo is not None:
                    valores_nivel_estructura.append(True)
                    valores_nivel_reales.append(nodo.getValor())
                    
                    hijo_izq = nodo.getHijoIzquierdo()
                    hijo_der = nodo.getHijoDerecho()
                    
                    cola.append(hijo_izq)
                    cola.append(hijo_der)
                    
                    if hijo_izq is not None or hijo_der is not None:
                        proximo_nivel_existe = True
                else:
                    valores_nivel_estructura.append(False)
                    cola.append(None)
                    cola.append(None)

            if nivel_actual > 0:
                es_espejo = (valores_nivel_estructura == valores_nivel_estructura[::-1])
                
                if es_espejo and any(valores_nivel_estructura):
                    
                    resultados_espejo[nivel_actual] = [True]

                    conteo_niveles_espejo += 1

            if not proximo_nivel_existe:
                break 
                
            nivel_actual += 1
        return resultados_espejo, conteo_niveles_espejo
    

    def amplitud_por_nivel(self):
        amplitud_por_nivel = {}
        if self._raiz is None:
            return amplitud_por_nivel
        nivel = -1

        cola = [self._raiz]
        while cola:
            nivel += 1
            amplitud_actual = len(cola)

            amplitud_por_nivel[nivel] = amplitud_actual
            for datos in range(amplitud_actual):
                nodo = cola.pop(0)
                if nodo.getHijoIzquierdo() is not None:
                    cola.append(nodo.getHijoIzquierdo())
                if nodo.getHijoDerecho() is not None:
                    cola.append(nodo.getHijoDerecho())
        return amplitud_por_nivel

    def recorrido_por_nivel(self):
        diccionario = {}
        if self._raiz is None:
            return diccionario

        cola = [self._raiz]
        nivel = -1

        while cola:

            tam = len(cola)
            nivel += 1
            diccionario[nivel] = []

            for datos in range(tam):
                nodo = cola.pop(0)
                diccionario[nivel].append(nodo.getValor())

                if nodo.getHijoIzquierdo() is not None:
                    cola.append(nodo.getHijoIzquierdo())
                if nodo.getHijoDerecho() is not None:
                    cola.append(nodo.getHijoDerecho())
        return diccionario
    

    def obtener_frontera(self):
        lista = []
        self._frontera_mascara(self._raiz, lista)
        return lista
    def _frontera_mascara(self, nodo, lista):
        if nodo is not None:
            self._frontera_mascara(nodo.getHijoIzquierdo(), lista)
            if nodo.getHijoIzquierdo() is None and nodo.getHijoDerecho() is None:
                lista.append(nodo.getValor())
            self._frontera_mascara(nodo.getHijoDerecho(), lista)

    
    def sumar_nivel(self, nivel_objetivo):
        return self._sumar_nivel_mascara(self._raiz, nivel_objetivo, 0)

    def _sumar_nivel_mascara(self, nodo, nivel_objetivo, nivel_actual):
        if nodo is None:
            return 0

        if nivel_actual == nivel_objetivo:
            return nodo.getValor()
        izq = self._sumar_nivel_mascara(nodo.getHijoIzquierdo(),nivel_objetivo,nivel_actual +1)
        der = self._sumar_nivel_mascara(nodo.getHijoDerecho(),nivel_objetivo,nivel_actual +1)

        return izq + der
    
    
    def sumar_nivel2(self, nivel_objetivo):
        suma = 0
        nivel = 0
        if self._raiz is None:
            return suma


        cola = [self._raiz]
        while cola:

            tam = len(cola)

            if nivel > nivel_objetivo:
                break

            for dato in range(tam):

                nodo = cola.pop(0)

                if nivel == nivel_objetivo:
                    suma += nodo.getValor()

                if nodo.getHijoDerecho() is not None:
                    cola.append(nodo.getHijoDerecho())
                if nodo.getHijoIzquierdo() is not None:
                    cola.append(nodo.getHijoIzquierdo())

            nivel += 1
        return suma



    def ancestro_comun(self, v1 , v2):
        return self._ancestro_mascara(self._raiz, v1, v2)
    def _ancestro_mascara(self, nodo, v1, v2):
        if nodo is None:
            return None

        if nodo.getValor() < v1 and nodo.getValor() < v2:
            self._ancestro_mascara(nodo.getHijoDerecho(), v1, v2)
        if nodo.getValor() > v1 and nodo.getValor() > v2:
            self._ancestro_mascara(nodo.getHijoIzquierdo(), v1, v2)

        else:
            return nodo.getValor()
        

    def espejos_por_nivel(self):
        diccionario = {}
        comprobacion = []
        nivel = 0
        conteo_espejos = 0
        if self._raiz is None:
            diccionario["total"] = 0
            return diccionario
        cola = [self._raiz]
        while cola:
            tam = len(cola)
            comprobacion = []

            for datos in range(tam):
                nodo = cola.pop(0)

                if nodo.getHijoIzquierdo() is not None:
                    cola.append(nodo.getHijoIzquierdo())
                    comprobacion.append(True)
                else:
                    comprobacion.append(False)

                if nodo.getHijoDerecho() is not None:
                    cola.append(nodo.getHijoDerecho())
                    comprobacion.append(True)
                else:
                    comprobacion.append(False)

            if not any(comprobacion):
                break

            es_espejo = (comprobacion == comprobacion[::-1])

            diccionario[nivel + 1] = es_espejo

            if es_espejo:
                conteo_espejos += 1

            nivel += 1

        diccionario["total"] = conteo_espejos
        return diccionario
    
    def rango(self, valor_min, valor_max):
        lista = []
        self._rango_mascara(self._raiz, valor_min, valor_max, lista)
        return lista

    def _rango_mascara(self, nodo, valor_min, valor_max, lista):
        if nodo is not None:
            self._rango_mascara(nodo.getHijoIzquierdo(), valor_min, valor_max, lista)
            if valor_min <= nodo.getValor() <= valor_max:
                lista.append(nodo.getValor())
            self._rango_mascara(nodo.getHijoDerecho(), valor_min, valor_max, lista)


    def invertir(self):
        self._invertir_mascara(self._raiz)

    def _invertir_mascara(self, nodo):
        if nodo is None:
            return
        
        aux_izq = nodo.getHijoIzquierdo()
        aux_der = nodo.getHijoDerecho()

        nodo.setHijoIzquierdo(aux_der)
        nodo.setHijoDerecho(aux_izq)

        self._invertir_mascara(nodo.getHijoIzquierdo())
        self._invertir_mascara(nodo.getHijoDerecho())

    
    def es_estricto(self):
        return self._estricto_mascara(self._raiz)

    def _estricto_mascara(self, nodo):
        if nodo is None:
            return True
        izq = nodo.getHijoIzquierdo()
        der = nodo.getHijoDerecho()

        if izq is None and der is None:
            return True
        if izq is not None and der is not None:
            return self._estricto_mascara(izq) and self._estricto_mascara(der)
        return False

    def anchura_maxima(self):
        diametro = 0
        if self._raiz is None:
            return diametro
        cola = [self._raiz]
        while cola:
            tam = len(cola)
            comprobacion = []

            for datos in range(tam):
                nodo = cola.pop(0)

                if nodo.getHijoIzquierdo() is not None:
                    cola.append(nodo.getHijoIzquierdo())
                    comprobacion.append(True)
                else:
                    comprobacion.append(False)

                if nodo.getHijoDerecho() is not None:
                    cola.append(nodo.getHijoDerecho())
                    comprobacion.append(True)
                else:
                    comprobacion.append(False)

            if len(comprobacion) > diametro:
                diametro = len(comprobacion)

        return diametro
    
    def diametro(self):
        self.maximo_diametro = 0
        self._diametro_mascara(self._raiz)
        return self.maximo_diametro

    def _diametro_mascara(self, nodo):
        if nodo is None:
            return 0

        altura_izq = self._diametro_mascara(nodo.getHijoIzquierdo())
        altura_der = self._diametro_mascara(nodo.getHijoDerecho())
        diametro_actual = altura_izq + altura_der

        if diametro_actual > self.maximo_diametro:
            self.maximo_diametro = diametro_actual

        return max(altura_izq, altura_der) + 1
    

    def obtener_camino_diametro(self):
        self.camino_maximo = []

        self._camino_diametro_mascara(self._raiz)

        return self.camino_maximo

    def _camino_diametro_mascara(self, nodo):
        if nodo is None:
            return []

        camino_izq_abajo = self._camino_diametro_mascara(nodo.getHijoIzquierdo())
        camino_der_abajo = self._camino_diametro_mascara(nodo.getHijoDerecho())


        diametro_actual = camino_izq_abajo[::-1] + [nodo.getValor()] + camino_der_abajo
        if len(diametro_actual) > len(self.camino_maximo):
            self.camino_maximo = diametro_actual


        if len(camino_izq_abajo) > len(camino_der_abajo):
            return [nodo.getValor()] + camino_izq_abajo
        else:
            return [nodo.getValor()] + camino_der_abajo
        

    def k_esimo_menor(self, k):
        aux = [0, None]
        self._k_esimo_mascara(self._raiz, k, aux)
        return aux[1]


    def _k_esimo_mascara(self, nodo, k, aux):
        if nodo is None:
            return aux
        self._k_esimo_mascara(nodo.getHijoIzquierdo(),k,aux)
        aux[0] += 1
        if aux[0] == k:
            aux[1] = nodo.getValor()

        self._k_esimo_mascara(nodo.getHijoDerecho(),k , aux)

    
    
    def obtener_ancestros(self, objetivo):
        lista = []
        self._obtener_ancestros_mascara(self._raiz, objetivo, lista)
        return lista
    def _obtener_ancestros_mascara(self, nodo, objetivo, lista):
        if nodo is None:
            return
        if objetivo < nodo.getValor():
            lista.append(nodo.getValor())
            self._obtener_ancestros_mascara(nodo.getHijoIzquierdo(),objetivo, lista)
        if objetivo > nodo.getValor():
            lista.append(nodo.getValor())
            lista.append(self._obtener_ancestros_mascara(nodo.getHijoDerecho(), objetivo, lista))
        if objetivo == nodo.getValor():
            return


    def obtener_ancestros2(self, objetivo):
        lista = []
        nodo_actual = self._raiz
        while nodo_actual is not None:
            valor_actual = nodo_actual.getValor()
            if objetivo == valor_actual:
                break

            lista.append(valor_actual)

            if objetivo < valor_actual:
                nodo_actual = nodo_actual.getHijoIzquierdo()
            else:
                nodo_actual = nodo_actual.getHijoDerecho()

        return lista
    
    def anchura_maxima_2(self):
        if self._raiz is None:
            return 0

        ancho_max = 0
        cola = [self._raiz]

        while cola:
            cantidad_en_nivel = len(cola)

            if cantidad_en_nivel > ancho_max:
                ancho_max = cantidad_en_nivel

            for _ in range(cantidad_en_nivel):
                nodo = cola.pop(0)
                if nodo.getHijoIzquierdo():
                    cola.append(nodo.getHijoIzquierdo())
                if nodo.getHijoDerecho():
                    cola.append(nodo.getHijoDerecho())

        return ancho_max
    
    
if __name__ == "__main__":
    arbol1 = ArbolBinario()
    arbol1.insertarIterativo(100)
    arbol1.insertarIterativo(90)
    arbol1.insertarIterativo(80)
    arbol1.insertarIterativo(85)
    arbol1.insertarIterativo(110)
    arbol1.insertarIterativo(120)
    arbol1.insertarIterativo(115)

    #print(arbol1.encontrarNivelesEspejoConteo())
    #print("----------------")
    #print("el arbol es vacio? = " , arbol1.isVacio())
    #print(arbol1.buscar(99))
    #print(arbol1.buscarIterativo(55))    
    #print("recoridos iterativos")
    
    #print(arbol1.inOrden())
    #print(arbol1.posOrden())
    #print(arbol1.preOrden())
    
    #print("recorridos recursivos")

    #print(arbol1.inOrdenRecursivo())   
    #print(arbol1.posOrdenRecursivo())
    #print(arbol1.preOrdenRecursivo())

    #print("altura del arbol: ", arbol1.altura())
    #print("altura del arbol (iterativa): ", arbol1.alturaIt())

    #print("cantidad de nodos: ", arbol1.cantidadNodos())
    #print("cantidad de nodos (iterativa): ", arbol1.cantidadNodosIt())

    #print("amplitud del arbol: ", arbol1.amplitud())
    #print("recorrido por niveles recursivo: ", arbol1.amplitudRecursivo())

    #print(arbol1.amplitud_por_nivel())
    #print(arbol1.recorrido_por_nivel())
    #print(arbol1.obtener_frontera())
    #print(arbol1.sumar_nivel(2))
    #print(arbol1.ancestro_comun(85,115))
    #print(arbol1.obtenerEstructuraVisual())
    #print(arbol1.rango(85,115))
    #print(arbol1.invertir())
    #print(arbol1.obtenerEstructuraVisual())
    print(arbol1.anchura_maxima_2())

