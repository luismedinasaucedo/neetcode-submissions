class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length()!=t.length()) return false;

        Map<Character,Integer> map1=new HashMap<>();
        Map<Character,Integer> map2=new HashMap<>();

        int a;
        char b;

        for (int i = 0; i < s.length(); i++) {

            b=s.charAt(i);

            if (map1.containsKey(b)){

                a=map1.get(b);
                map1.put(b,++a);
            }
            else map1.put(b,1);


            b=t.charAt(i);
            if (map2.containsKey(b)){
                a=map2.get(b);
                map2.put(b,++a);
            }
            else map2.put(b,1);

        }



        for (char letra:map1.keySet()){
            if (map2.get(letra)==null) return false;
            if (!Objects.equals(map2.get(letra), map1.get(letra))) return false;
        }

        return true;
    }
}
