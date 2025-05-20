import io
import sys
from looping import happy_new_year

class TestHappyNewYear:
    def test_prints_10_to_1_hny(self):
        '''prints 10 to 1 countdown then "Happy New Year!"'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        happy_new_year()
        sys.stdout = sys.__stdout__
        answer = captured_out.getvalue()

        # Split output into lines
        answer_list = answer.strip().split('\n')

        # Expected countdown
        expected_output = [str(i) for i in range(10, 0, -1)] + ["Happy New Year!"]

        assert answer_list == expected_output, f"Expected output {expected_output}, but got {answer_list}"
