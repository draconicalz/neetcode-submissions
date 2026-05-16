class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsDict = {}
        output = []
        for i in range(0, len(strs)):
            if "".join(sorted(strs[i])) not in strsDict:
                strsDict["".join(sorted(strs[i]))] = len(output)
                output.append([strs[i]])
            else:
                output[strsDict["".join(sorted(strs[i]))]].append(strs[i])
        return output
            

        