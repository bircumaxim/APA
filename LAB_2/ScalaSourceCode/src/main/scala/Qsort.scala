/**
  * Created by max on 11/12/15.
  */
import Ordered._

class Qsort() extends SortAlgorithm {

  //QuiksortFunction

  private def qsort[A : Ordering](ls: List[A]) = {
    this.timer.timer("qsort")
    def sort(ls: List[A])(parent: List[A]): List[A] = {
    this.iterations += 1
      if (ls.size <= 1) ls ::: parent else {
        val pivot = ls.head
        val (less, equal, greater) = ls.foldLeft((List[A](), List[A](), List[A]())) {
          case ((less, equal, greater), e) => {
            if (e < pivot)
              (e :: less, equal, greater)
            else if (e == pivot)
              (less, e :: equal, greater)
            else
              (less, equal, e :: greater)
          }
        }
        sort(less)(equal ::: sort(greater)(parent))
      }
    }
    this.time = this.timer.timer("qsort")
    sort(ls)(Nil)
  }

  //DataCollector

  def sortList(l:List[Int]) = {
    qsort(l)
  }

}
