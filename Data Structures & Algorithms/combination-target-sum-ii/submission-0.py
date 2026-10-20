class Solution:
    def generate(self, candidates, target, index, take, soln, trace):
        if (target < 0) or (index >= len(candidates)):
            return
        if (take):
            trace.append(candidates[index]) 
            if (target == 0):
                soln.append(trace.copy())
                trace.pop()
                return
            new_index = index + 1 
            if (new_index >= len(candidates)):
                trace.pop()
                return 
            self.generate(candidates, target - candidates[new_index], new_index, True, soln, trace)
            self.generate(candidates, target, new_index, False, soln, trace)
            trace.pop()
            return
        else:
            new_index = index + 1
            if new_index < len(candidates):
                if (candidates[new_index] == candidates[index]):
                    self.generate(candidates, target, new_index, False, soln, trace)
                    return
                if (target - candidates[index] < 0):
                    return 
                self.generate(candidates, target - candidates[new_index], new_index, True, soln, trace)
                self.generate(candidates, target, new_index, False, soln, trace)
            else:
                return


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        soln = []
        trace = [] 
        self.generate(candidates, target - candidates[0], 0, True, soln, trace)
        self.generate(candidates, target, 0, False, soln, trace)
        return soln