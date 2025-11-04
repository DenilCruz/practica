from collections import deque
from ClaseArbolBinario import ArbolBinario


class Espejo(ArbolBinario):
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
