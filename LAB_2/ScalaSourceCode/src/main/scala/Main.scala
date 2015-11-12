import scala.collection.mutable.ListBuffer
import scala.util.Random

/**
  * Created by max on 11/12/15.
  */
object Main extends App {
  var dataGnerator = new DataGenerator()
  val qsort = new Qsort
  val bsort = new BubbleSort
  val msort = new MergeSort

  val l = dataGnerator.generateAscendingList(100000)
  //val l = dataGnerator.generateDescendingList(100000)
  //val l = dataGnerator.generateRandomList(100000)

  qsort.sortList(l)

  println(qsort.getIter())
  println(qsort.getTime())

  bsort.sortList(l)

  println(bsort.getIter())
  println(bsort.getTime())

  msort.sortList(l)

  println(msort.getIter())
  println(msort.getTime())
}

