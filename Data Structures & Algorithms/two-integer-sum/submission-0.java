
class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Use hashMap
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int residual = target - nums[i];
            if (map.containsKey(residual) && map.get(residual) != i) {
                return new int[]{map.get(residual), i};
            }

            map.put(nums[i], i);
        }
        return new int[]{};
    }

    
}
