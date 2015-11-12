import java.util.Random

import scala.collection.mutable.ListBuffer

/**
  * Created by max on 11/12/15.
  */
class DataGenerator {

  private var randomGnerator = new Random();

  def generateRandomList(n:Int): List[Int] ={
    var i:Int = 0
    var list:List[Int] = List()
    var nr = new ListBuffer[Int]()
    while(i < n){
      nr += randomGnerator.nextInt();
      i += 1
    }
    list = nr.toList
    list
  }

  def generateAscendingList(n:Int): List[Int] ={
    var i:Int = 0
    var list:List[Int] = List()
    var nr = new ListBuffer[Int]()
    while(i < n){
      nr += i
      i += 1
    }
    list = nr.toList
    list
  }

  def generateDescendingList(n:Int): List[Int] ={
    var i:Int = n
    var list:List[Int] = List()
    var nr = new ListBuffer[Int]()
    while(i >= 0){
      nr += i
      i -= 1
    }
    list = nr.toList
    list
  }
}
