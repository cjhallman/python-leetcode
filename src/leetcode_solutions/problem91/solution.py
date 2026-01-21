class Solution:
    dp = {}

    def numDecodings(self, s: str) -> int:
        """
        Assumptions:
        1. All characters are valid digits
        2. Might not be decodable
        Base Cases:
        1. len(s) == 0 -> 1 decode
        2. s[0] == 0 -> 0 decodes
        Strategy:
        1. Check the first char
         if first char is 0 -> return 0
         else -> get total decodes for string missing first char
        2. Check the first 2 chars
         if first 2 chars is valid decode -> get total decodes for string missing first 2 chars
         else -> total decodes for string missing first 2 chars = 0
        3. return total strings missing first char + total strings missing first 2 chars
        Example:
        11106
        numDecodings(1106) + numDecoding(106)
        numDecodings(106) + numDecodings(06) + numDecodings(06) + numDecodings(6)
        numDecodings(06) + numDecodings(6) + 0 + 0 + 1
        0 + 1 + 1 = 2
        """
        if s in self.dp:
            print(f"HIT: dp[{s}] is {self.dp[s]}")
            return self.dp[s]
        print(f"numDecodings({s})")
        if len(s) == 0:
            print(f"len({s}) == 0")
            self.dp[s] = 1
            return 1
        first_char = int(s[0])
        if first_char == 0:
            print(f"first_char({s}) == 0")
            self.dp[s] = 0
            return 0
        if len(s) == 1:
            print(f"len({s}) == 1")
            self.dp[s] = 1
            return 1
        # Check first char
        decodes_missing_first_char = self.numDecodings(s[1:])
        # Check first 2 chars
        first_two_chars = int(s[:2])
        print(f"fist_two_chars: {first_two_chars}")
        decodes_missing_first_two_chars = 0
        if first_two_chars <= 26:
            decodes_missing_first_two_chars = self.numDecodings(s[2:])
        self.dp[s] = decodes_missing_first_char + decodes_missing_first_two_chars
        print(self.dp)
        return self.dp[s]
