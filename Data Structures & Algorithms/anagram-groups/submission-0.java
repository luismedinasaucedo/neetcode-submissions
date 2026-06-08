class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> mp=new HashMap<>();
        
        for (String palabra:strs){
            char [] letra=palabra.toCharArray();
            Arrays.sort(letra);
            String palabraordenada=new String(letra);
            
            if (!mp.containsKey(palabraordenada)){
                mp.put(palabraordenada,new ArrayList<>());
            }
            mp.get(palabraordenada).add(palabra);


        }

        return new ArrayList<>(mp.values());
    }
}
