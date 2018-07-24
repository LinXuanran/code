public class Main {

    public static void main(String[] args) {
        int[] a={1,2,3,4,5,6,6,2,8,7};
        int i = hire_assistant(a);
        System.out.println(i);
    }

    public static int hire_assistant(int []man){
        int n =man.length;
        System.out.println(n);
        int best=0,cost=0,interview=2,hire=25;
        for (int i =0;i<n;i++){
            cost=cost+interview;
            if (best<man[i]) {
                best=man[i];
                cost=hire+cost;
            }
        }
        return cost;
    }



}
