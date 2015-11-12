/**
  * Created by max on 11/12/15.
  */
class BubbleSort extends SortAlgorithm{

  ///BubbleSort Function

    def sortIterative(input: Array[Int]): Array[Int] = {
    this.timer.timer("BubbleSort")
      val limit = input.size - 1
      for (a <- 1 to limit) {
          this.iterations +=1
        for (b <- limit to a by -1) {
          if (input(b) < input(b - 1)) {
            val x = input(b)
            input(b) = input(b - 1)
            input(b - 1) = x
          }
        }
      }
    this.time = this.timer.timer("BubbleSort")
      input
    }


  ///DataCollector

  def sortList(l:List[Int]) ={
      sortIterative(l.toArray)

  }

}
