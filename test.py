from unittest import TestCase, main
from whiteboard import solution


class WhiteboardTestCase(TestCase):
    
    def test_1_zero(self):
        self.assertEqual(solution(0), 0)
    
    def test_2_100(self):
        self.assertEqual(solution(100), 1)

    def test_3_positive(self):
        self.assertEqual(solution(5678),  8765) 

    def test_4_negative(self):
        self.assertEqual(solution(-5678),  -8765) 

    def test_4_negative_200(self):
        self.assertEqual(solution(-200), -2)


if __name__ == "__main__":
    main()