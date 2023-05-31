class Node:
    def __init__(self, task, next=None):
        self.task = task
        self.next = next

class tareas:
    def __init__(self):
        self.head = None

    def addFront(self, task):
        self.head = Node(task, self.head)

    def addBack(self, task):
        if not self.head:
            self.head = Node(task)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(task)

    def contains(self, task):
        current = self.head
        while current:
            if current.task == task:
                return True
            current = current.next
        return False

    def display(self):
        tasks = []
        current = self.head
        while current:
            tasks.append(current.task)
            current = current.next
        return " -> ".join(tasks)

def taskManager():
    Tareas = tareas()
    while True:
        print("1. Agregar tarea importante")
        print("2. Agregar tarea no importante")
        print("3. Verificar si una tarea existe")
        print("4. Ver todas las tareas")
        print("5. Salir")
        
        option = int(input("Elige una opción: "))
        
        if option == 1:
            task = input("Ingresa la nueva tarea: ")
            Tareas.addFront(task)
        elif option == 2:
            task = input("Ingresa la nueva tarea: ")
            Tareas.addBack(task)
        elif option == 3:
            task = input("Ingresa la tarea a buscar: ")
            if Tareas.contains(task):
                print("La tarea existe en la lista.")
            else:
                print("La tarea no existe en la lista.")
        elif option == 4:
            print("Tareas: ")
            print(Tareas.display())
        elif option == 5:
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    taskManager()