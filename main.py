class Node:
  def __init__(self,data):
    self.prev=None
    self.data=data
    self.next=None

class List:
  def __init__(self):
    self.head=None
    self._size=0
  
  #Додавання елемента в кінець списку 
  def PushBack(self,data):
    new_node=Node(data)
    if self.head is None:
      self.head=new_node
      self._size+=1
      return
    
    current=self.head
    while current.next:
      current=current.next
    current.next=new_node
    new_node.prev=current
    self._size+=1
    return
  
  #Виведення списку
  def to_list(self):
    current=self.head
    txt=""
    while current:
      txt+=str(current.data)+" "
      current=current.next
    return txt
  
  #Перевірка елентів на prev та next
  def check(self):
    current=self.head
    while current:
      if current.prev==None:
        print(f"Prev: {current.prev}")
      else:
        print(f"Prev: {current.prev.data}")

      print(f"Data: {current.data}")

      if current.next==None:
        print(f"Next: {current.next}")
      else:
        print(f"Next: {current.next.data}")
      print("-----")
      current=current.next

  #Виведення розміру списку
  def Get_Count(self):
    return self._size
  
  #Пошук елемента за ключем 
  def find_key(self,key):
    current=self.head
    cnt=0
    while current:
      if current.data==key:
        return f"index: {cnt}"
      current=current.next
      cnt+=1
    return "Not found!"
  
  #Додавання елемента на початок списку
  def PushFront(self,data):
    current=self.head
    new_node=Node(data)
    if self.head is None:
      self.head=new_node
      self._size+=1
      return
    else:
      new_node.next=current
      new_node.next.prev=new_node
      self.head=new_node
      self._size+=1
      return
  
  #Додавання елемента в довільне місце
  def AddBefore(self,index,data):
    current=self.head
    new_node=Node(data)
    cnt=1
    if self.head is None:
      return
    else:  
      while current.next:
        if cnt==index:
          new_node.next=current.next
          new_node.prev=current
          new_node.next.prev=new_node
          current.next=new_node
          self._size+=1
          return
        current=current.next
        cnt+=1
  
  #Видалення першого елемента списку
  def RemoveFirst(self):
    if self._size==0:
      print("Список пуст")
      return
    self.head=self.head.next
    if self.head is not None:
      self.head.prev=None
    self._size-=1
    return
  
  #Видалення останнього елемента списку
  def RemoveLast(self):
    if self._size==0:
      print("Список пуст")
      return
    if self._size==1:
      self.head=None
      self._size-=1
      return   
    current=self.head
    cnt=1
    while current.next:
      if self._size-1==cnt:
        current.next=None
        self._size-=1
        return
      current=current.next
      cnt+=1
  
  #Видалення довільного елемента списку 
  def RemoveNode(self,data):
    current=self.head
    cnt=1
    if self.head is None:
      print("Список пуст")
      return
    if self._size==1:
      if self.head.data==data:
        self.head=None
        self._size-=1
      return
    while current.next:
      if current.data==data:
        self.RemoveFirst()
        return
      if current.next.data==data:
        if current.next.next is None:
          self.RemoveLast()
          return
        current.next=current.next.next
        current.next.prev=current
        self._size-=1
        return
      current=current.next
      cnt+=1
    print(f"У списку немає такого значення елеменнта {data}!")
  
  #Завдання №1
  def task_1(self):
    current=self.head
    txt=""
    temp=0
    while current:         
      if current.data %2 ==0:
        temp=current.data  
      current=current.next

    current=self.head
    cnt=0
    while current:
      if current.data %2 != 0:
         new_node=Node(temp)
         new_node.next=current.next
         new_node.prev=current
          
         if current.next is not None:
           current.next.prev = new_node
         current.next=new_node
         self._size+=1
         current=new_node.next
      else:  
        current=current.next
    return

  #Завдання №2
  def task_2(self):
    current=self.head
    sum=0
    while current:
      if current.data>=15:
        sum+=current.data
      current=current.next
    return sum 
  
