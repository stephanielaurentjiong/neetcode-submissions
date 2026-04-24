class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        # dict = {}
        for i, str in enumerate(strs):
            # dict[i] = str
            result += str + "我"
        # print(result)
        # print(dict)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        word = ""
        for char in s:
            if char == "我":
                result.append(word)
                word = ""
                continue

            word += char

        print(result)
        return result
