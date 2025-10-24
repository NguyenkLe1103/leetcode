

class Solution {
    public int romanToInt(String s) {
        String str= s;
        Integer holder = 0; 
        Map<Character, Integer> result = new HashMap<>();
        result.put('I', 1);
        result.put('V', 5);
        result.put('X', 10);
        result.put('L', 50);
        result.put('C', 100);
        result.put('D', 500);
        result.put('M', 1000);

        for (int i = 0; i < s.length()-1 ;i++){
            if (result.get(s.charAt(i)) < result.get(s.charAt(i+1))){

                holder -= result.get(s.charAt(i));
            }
            else {
                holder += result.get(s.charAt(i));
                }

        }
        return holder + result.get(s.charAt(s.length()-1));
    }
}