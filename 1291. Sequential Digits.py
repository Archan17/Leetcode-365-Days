class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        num_digits_low = int(log(low)//log(10)) + 1 
        num_digits_hi = int(log(high)//log(10)) + 1

        bases = [12,123,1234,12345,123456,1234567,12345678,123456789]
        increment = [11,111,1111,11111,111111,1111111,11111111,1111111111]
        answers = []

        for digits in range(num_digits_low, num_digits_hi+1):
            value = bases[digits-2]
            num_attempts = 10 - (value % 10)
            for _ in range(num_attempts):
                if low <= value <= high:
                    answers.append(value)
                value += increment[digits-2]    

        return answers            

        
