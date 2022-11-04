from threading import Thread
import threading


def numeros_pares(vetor):
    
    for i in range(len(vetor)):
        if vetor[i] % 2 == 0:
            print(f"{threading.currentThread().getName()} - Imprimindo {vetor[i]}")


def numeros_imparespares(vetor):
    
    for i in range(len(vetor)):
        if vetor[i] % 2 != 0:
            print(f"{threading.currentThread().getName()} - Imprimindo {vetor[i]}")


if __name__ == '__main__':
     
    vetor = [1, 2, 3, 4, 5, 6, 7, 8]
     
    thread1 = Thread(target=numeros_imparespares,args=(vetor,))    
    thread1.start()
    thread2 = Thread(target=numeros_pares,args=(vetor,))    
    thread2.start()
    