/**
  * Created by max on 11/12/15.
  */
class Timer {

  var timers = scala.collection.mutable.Map.empty[String, Long]
  private var output:String = ""

  def timer(timerName:String): String = {
    if (timers contains timerName) {
      this.output = s"$timerName  ${(System.nanoTime() - timers(timerName)) / 1000 / 1000} milliseconds"
    }
    else timers(timerName) = System.nanoTime
    output
  }
}
