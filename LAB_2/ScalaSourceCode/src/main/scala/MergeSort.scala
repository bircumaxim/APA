import scala.annotation.tailrec

/**
  * Created by max on 11/12/15.
  */
class MergeSort extends SortAlgorithm{

  private implicit def IntIntLessThan(x: Int, y: Int) = x < y

  //MergeSortFunctino

  private def mergeSort[T](xs: List[T])(implicit pred: (T, T) => Boolean): List[T] = {
      this.iterations += 1
    val m = xs.length / 2
    if (m == 0) xs
    else {
      def merge(ls: List[T], rs: List[T], acc: List[T] = List()): List[T] = (ls, rs) match {
        case (Nil, _) => acc ++ rs
        case (_, Nil) => acc ++ ls
        case (l :: ls1, r :: rs1) =>
          if (pred(l, r)) merge(ls1, rs, acc :+ l)
          else merge(ls, rs1, acc :+ r)
      }
      val (l, r) = xs splitAt m
      merge(mergeSort(l), mergeSort(r))
    }
  }

  //DataCollector

  def sortList(l:List[Int]) ={
    this.timer.timer("mergeSort")
    mergeSort(l)
    this.time = this.timer.timer("mergeSort")
  }
}
