title: CS 2100 Notes
date: 2024-10-04

## CS2100 Lecture Notes

### Week 2

8 types

- byte MAX_VALUE: 127
- short
- int defaults to 0
- long
- float not used unless user specifies and wants to save space by doing so
- double
- boolean defaults to false
- char defaults to "null character" (not the same as null)

reference

- the memory is storing a memory address
- using new to be created is an object references
- static vs heap
- to use input, we use scanner objects

Scanner is a conveyor belt

PRIMITIVE

* camelCase
* cannot be null, defaults to values listed above
* double cannot be compared with "=="
* stored on the memory stack, passing by value

REFERENCE

* TitleCase
* can be null
* reference compared with .equals()
* on the memory stack is the reference to locate the object on the memory heap (because we
* don't know how big it's going to be)

when have a null, pointed to bootstrap location
bootstrap is a location that's activated after booting system
NullPointerException

Predetermined packages

- String
- Random
- Math

to get these class, use an import statement

- java.lang: basic functionality
- java.awt: graphics classes
- java.swing: too old
- java.text.*; import everything in text package

only 4 ways to control a program

1. sequence (line 1 -> 2 -> 3 -> ...)
2. conditional statement (if, else, switch statement)
3. loops

"y = x++" is different from "y = ++x",

* the former gives y the old value,
* the latter gives the incremented value

do while is used for data validation

* hint users to input numbers or program won't proceed

Strings come from a string pool, Java minimizes the string they have to allocate

### Week 3

Comparison

- "has-a" relationship

Inheritance

- "is-a" relationship
- everything inherits from object
- every method in object can also be found in its descendants
    - .toString()
    - .equals() - compare address
    - .clone()
    - .hashCode() - unique identifier

Object provides the default constructor

- no arguments
- allocates memory
- has a default constructor
- if you're writing a constructor the default one automatically expires, so you have to write a new one yourself

.equals()

- reflexive
- symmetric
- transitive
- side note: hahaha please this is so equivalence relation coded

How to write an equal method yourself

- Override using exact same format!
- ```java
  public boolean equals(Object obj) {
  }
  ```
- compare to ensure it's not null
- if argument is the current object, return true
- check type using ```.instanceOf()```
- recast the argument to current class ```(CurrentClass) Object```
- compare the actual data
    - == primitive
    - .equals() reference

Inheritance

* Inheritance is a mechanism by which one class acquires the properties of another class
* Don’t repeat yourself
* Declaring fields as private reserves encapsulation
* Subclass methods call superclass methods to set the values of the fields and the superclass methods enforce the
  validation rules for the data
* But calling methods incur processing overhead
* Declaring fields as protected allows them to be accessed directly by subclasses
* Classes outside the hierarchy and package must use accessors and mutators for protected fields
* Define protected fields only when high performance is necessary
* Subclasses extend superclasses
* Subclasses inherit from superclasses
* Java only supports one direct parent

### Week 5

Substitutability Principle

- A child class is a more specific class
- A Character is a kind of Object
- A Mage is a kind of Character
- If an Object is required, a Character is accepted
- If an Object is required, a Mage is accepted
- If a Character is required, a Mage is accepted
- If a Mage is required, a Character is not accepted!
- ```Integer```wraps up an integer and makes it an object of ```int```

Polymorphism requirements

- the classes are in the same hierarchy
- all subclasses override the same method
- a subclass object reference is assigned to a superclass object reference.
- the superclass object reference is used to call the method.

An example of abstract class

```Java
/* public or private */ abstract class ClassName {
// class body
}
```

Interface (接口)

```Java
public interface TimeKeeper {
    public int getTime();

    public int setTime();
}
```

- assignment Blackjack releases tomorrow
- Soccer due today
- Interface
- Introducing List

An interface is an agreed-upon means of connection between classes

- using standardized plugs and outlets allows reuse of the power network by any electrical device
- defining an interface in Java allows validation of methods specified in an interface, allowing reuse of algorithms and
  code
- interfaces promote loose-coupling, not an inheritance relationship
- a class can inherit directly from only one class, ```extend``` only one class
- ```interface``` allows a class to inherit behavior from multiple sources
- an interface typically specifies behavior that a class will implement

Using (implementing) interfaces

- interfaces are not instantiated as objects, but provide a contract between classes
- ```Java
  public class Watch implements TimeKeeper{
  }
  ```
- abstract means no implementation of methods, interface is just implementing behavior, can't have instance data

Polymorphism via interfaces

- ```Java
  Speaker current;
  ```
- the ```current``` reference can be pointed to any object of any class that implements the ```Speaker``` interface

Standard Java interfaces

- ```compareTo```

Interface hierarchies

Comparable interface

- defined the natural ordering of objects in class (i.e. default)

Implementing comparable

- ```Java
  public int compareTo(T o){
    // match the type in the class header
  }
  ```
- ```Java
  public interface Comparable<T>{
    // compare this object to other
    public int compareTo(T other);
  }
  ```

Comparator

- implement compare outside the class and takes two arguments

Function objects

- implements a specified interface
- the one method in that interfaces does the needed work

Comparator

- comparator interface provides a way to externally compare two objects
- works similar to ```compareTo()```
- ```Collections.sort(arrayListOfRacingDonkeys, new SortByWeight());```

Implementing Comparators

```Java
import java.util.Comparator;

public class CmpDogByBreedAndName implements Comparator<Dog> {
    public int compare(Dog d1, Dog d2) {
        /* Customized comparator */
        int retval = d1.getBreed().compareTo(d2.getBreed());
        if (retval != 0) {
            return retval;
        }
        /* String's default compareTo method */
        return d1.getName().compareTo(d2.getName);
    }
}
```

KEY POINT

- <b>Comparable</b> uses natural sorting
- <b>Comparator</b> uses customized sorting

<b>Abstract class</b> - what a class is, what kind of data is stored<br>
<b>Interface</b> - what it can do

### Week 6

Frameworks

- reusable OO software / code components
- set of classes developed by someone else
- partially complete
- a unified texture, works together, seamless, common interface
- e.g.: Java Collections

Java Collections Framework (JCF)

- data structures and abstract data types
- ADT: specification, what can it store, what are the implementations
- DS: implementation, how to implement in memory and operations, and what's the performance of the operations
- ADT examples:
    - list
        - ArrayList
        - LinkedList
    - set
    - map

Collection interface

- generic class
- ```Java
  import java.util.Collection;
  import java.util.Iterator;   
  public interface Collection<E> {
    public boolean add(E obj);
    public Iterator iterator();
    public int size();
    public boolean isEmpty();
    public boolean contains(E obj);
    public boolean containsAll(Collection other);
  }
  ```

List interface

```Java
import java.util.Collection;

public interface List<E> extends Collection<E> {
    public boolean add(int index, E obj);

    public E get(int index);

    public int indexOf(E obj);

    public boolean remove(int index);

    public E set(int index, E obj);

    List<E> subList(int from, int to); /* Not suggested */
}
```

Implementing a List using ArrayList (time complexities)

- create(empty) O(1) constant
- insert at end O(1)
- insert at beginning O(n)
- remove at end O(1)
- remove at beginning O(n)
- find - true O(n/2)
- find - false O(n)

Vectors

- a type of list
- keep things in order
- always random access (can get to what we want directly and does not need to go through everything before it)
- a "resizable array" - stores data in an array but hides the need to resize
    - maintains a "capacity" // how many spaces
    - maintains a "capacityIncrement" // how much to grow or shrink when required
- resizes as necessary as items are added
- concrete classes provided by Java are the ArrayList and Vector classes

Vector performance

- final sequence of items such that given any index the item in that index can be modified at constant time (the same
  amount of time regardless of how many items are there)
- insertion or deletion at the back of sequence takes only constant time on average
- have to resize? takes more time

Vectors are a generic data type

```Java
import java.util.ArrayList;
import java.util.Vector;

Vector<Integer> list1 = new Vector<Integer>();
ArrayList<Double> list2 = new Vector<Double>();
```

A size value stores the number of data elements - always <= capacity

Generic type (泛型)

- a generic class or interface that is parameterized over types
- ```Java
  import java.util.ArrayList;   
  ArrayList<T> arrlist = new ArrayList<>();
  ```

Generics ensure type safety

- without generics, the compiler would happily allow any type into ```ArrayList<Object>``` with ```Object``` being
  anything
- generics can be type-specific and type-safe

```Java
import java.util.List;

public class ArrayList<E> extends AbstractList<E> implements List<E> {

}
```

```Java
import java.util.ArrayList;

public static <T extends Comparable<T> T> largestValue(ArrayList<T> arrList) {

}
```

```Java
import java.util.LinkedList;

LinkedList<E>;
```

Abstract Model of a List Object

- add
- get
- indexOf
- remove
- set sublist
- size
- clear
- insertAtHead
- insertAtTail
- insertAt
- removeAtHead
- removeAtTail

```LinkedList```

- arrays allocate contiguous memory for data/objects
- vectors use the same approach, based on arrays
- LinkedLists connect data/objects by means of references
- the list class has a head, where the list starts
- each node links to a subsequent node
- to find an element

How ```LinkedList``` works

```Java
head =0;
tail =0;
```

Node

- a node contains:
    - a data item
    - one or more links
- a link is a pointer to a list node
- the node class is usually defined in another class

Node class

```Java
public class ListNode<T> {
    /* Data being stored in this node */
    private T data;
    /* reference to the next node in the list */
    protected ListNode<T> next;

    public ListNode(T data) {
        this.data = data;
        this.next = null;
    }

    /* getter */
    public T getData() {
        return this.data;
    }
}
```

Other types of LinkedLists
- doubly linked
- circular doubly linked
- ...

Doubly linked list
- have another pointer besides next - prev

Inserting a node into a single Linked List

```Java
import org.w3c.dom.Node;

Node bob = new Node("bob");
bob.next = harry.next;
harry.next = bob;
```

Iterator
- an iterator is an object that provides a means of processing a collection of objects one at a time
- 