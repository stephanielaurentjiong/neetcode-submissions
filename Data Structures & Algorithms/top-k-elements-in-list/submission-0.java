class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        //Make a hashmap to count occurences of each number 
        Map<Integer, Integer> result = new HashMap<>();

       for (int num : nums) {
        result.put(num, result.getOrDefault(num, 0) + 1);
       }

        //Create the bucket to store 
        //Freq[i] is the frequencies
        //The list is to store which number have that frequencies
        List<Integer>[] freq = new List[nums.length + 1];
        for (int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<>();
        }

        //Populate bucket
        //Index as frequencies, element as the "key"
        for (Map.Entry<Integer, Integer> entry : result.entrySet()) {
                freq[entry.getValue()].add(entry.getKey());
        }

        int[] res = new int[k];
        int count = 0;
        for (int i = freq.length -1; i > 0; i--) {
            //Check if this bucket empty
            if (!freq[i].isEmpty()) {
                for (int entry : freq[i]) {
                    //Add each number to the result to be retunred
                    res[count] = entry;
                    count++;
                }

                if (count == k) {
                    return res;
                }
            }

        }

        return res;
    }
}
