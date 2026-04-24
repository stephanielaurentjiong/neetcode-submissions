class Solution:

    def encode(self, strs: List[str]) -> str:
        emp_str=''
        for i in strs:
            emp_str = emp_str+i
            emp_str = emp_str+'|'
        print("encode:" , emp_str)
        return emp_str
    def decode(self, s: str) -> List[str]:
        output = s.split('|')
        output.pop()
        #print("decode:" , output)
        return output