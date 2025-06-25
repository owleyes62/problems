public class TwoSum{
    public static void main(String args){
        int[] vetor = {3, 4, 5, 6};
        int target = 7;
        twoSum(vetor, target);

    }
    
    public static int[] twoSum( int[] nums, int target){
        int tamV = 0;
        int[] indiceV = new int[nums.length]; 
        for(int i = 0; i < nums.length; i++){
            int indiceAtual = i;
            for (int y = 0; y < nums.length; y++) {
                if (indiceAtual + nums[y] == target) {
                    indiceV[tamV] = indiceAtual;
                    tamV += 1;
                    indiceV[tamV] = y;
                }
            }
        }
        for (int i = 0; i < tamV; i++) {
            if (i == (tamV - 1)) {
                System.out.println(indiceV[i] + "]");
            }else{
                System.out.println("[" + indiceV[i] + " ,");
            }
        }

        return indiceV;
    }
}