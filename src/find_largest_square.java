public class find_largest_square {

    public static boolean check_num(int num){
        if(num == 1){
            return true;
        }
        else{
            return false;
        }
    }

    public static void main(String[] args){
        int [][]board = {{0,1,1,1},{1,1,1,1},{1,1,1,1},{0,0,1,0}};
        int max = 0;
        int answer = 0;

        for(int i=1; i<board.length; i++){
            for(int j=1; j<board.length; j++){
                if(check_num(board[i][j])){
                    int left = board[i][j-1];
                    int up = board[i-1][j];
                    int up_left = board[i-1][j-1];

                    int min = Math.min(left,Math.min(up,up_left));

                    board[i][j] = min + 1;

                    max = Math.max(max,min+1);
                }
            }
        }
        answer = max * max;
        System.out.println(answer);
    }
}
