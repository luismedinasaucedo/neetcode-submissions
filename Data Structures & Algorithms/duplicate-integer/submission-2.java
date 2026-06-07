class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer,Integer> map=new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int actual=nums[i];
            if (map.containsKey(actual)) return true;
            map.put(actual,i);
        }
        return false;
    }
}