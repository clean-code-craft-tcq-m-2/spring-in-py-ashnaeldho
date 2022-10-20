import unittest
import statistics
import math as m

class StatsTest(unittest.TestCase):
  def test_report_min_max_avg(self):
    computedStats = statistics.calculateStats([1.5, 8.9, 3.2, 4.5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats[0], 4.525, delta=epsilon)
    self.assertAlmostEqual(computedStats[1], 1.5, delta=epsilon)
    self.assertAlmostEqual(computedStats[2], 8.9, delta=epsilon)

  def test_avg_is_nan_for_empty_input(self):
    computedStats = statistics.calculateStats([])
    self.assertEqual(computedStats, None)
   # numberset[] = { 0 }
   # setlength = len(numberset) / len(numberset[0]);
   # computedStats = statistics.calculateStats([numberset, setlength])
   # self.assertTrue(math.isnan(computedStats[0]))
   # self.assertTrue(math.isnan(computedStats[1]))
   # self.assertTrue(math.isnan(computedStats[2]))
    
    # --  computedStats = statistics.calculateStats([])
    # -- self.assertEqual(computedStats, None)
    # All fields of computedStats (average, max, min) must be
    # nan (not-a-number), as defined in the math package
    # Design the assert here.
    # Use nan and isnan in https://docs.python.org/3/library/math.html

  def test_raise_alerts_when_max_above_threshold(self):
    emailAlert = statistics.EmailAlert()
    ledAlert = statistics.LEDAlert()
    maxThreshold = 10.5
    statsAlerter = StatsAlerter(maxThreshold, [emailAlert, ledAlert])
    # statsAlerter.checkAndAlert([22.6, 12.5, 3.7])
    self.assertTrue(emailAlert.emailSent)
    self.assertTrue(ledAlert.ledGlows)
    #self.assertTrue(emailAlert.emailSent)
    #self.assertTrue(ledAlert.ledGlows)

if __name__ == "__main__":
  unittest.main()
