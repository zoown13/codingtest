import java.util.ArrayList;
import java.util.Collections;

public class desc_integer {
    public static void main(String[] args) {
        long answer = 0;
        String temp_ans = "";
        long remainder = 0;
        long n = 10;
        ArrayList<Long> arr = new ArrayList<>();

        for(int i=1;i<11;i++){
            remainder = n % 10;
            arr.add(remainder);
            n = n / 10;
            if(n==0){
                break;
            }
        }

        arr.sort(null);
        Collections.reverse(arr);

        for(int i=0;i<arr.size();i++){
            temp_ans = temp_ans + arr.get(i);
        }
        answer = Long.parseLong(temp_ans);
        System.out.println(answer);

    }
}