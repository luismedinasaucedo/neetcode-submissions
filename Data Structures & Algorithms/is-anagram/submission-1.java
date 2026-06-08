class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length()!=t.length()) return false;
        Map<Character,Integer> map=new HashMap<>();
        int a;
        char b;
        for (int i = 0; i < s.length(); i++) {
            b=s.charAt(i);
            if (map.containsKey(b)) {
                a=map.get(b);
                map.put(s.charAt(i),++a);
            }
            else map.put(b,1);
        }
        for (int i = 0; i < t.length(); i++) {
            b=t.charAt(i);
            if (map.containsKey(b)){
                a=map.get(b);
                map.put(b,--a);
                if (map.get(b)==0) map.remove(b);
            }else return false;
        }
        return true;

    }
}
