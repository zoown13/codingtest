public class kakao_friends_block {

    public static String[][] init_board(int m, int n, String[] board){
        String[][] init_board = new String[m][n];
        for(int i=0;i<m;i++){
            String row = board[i];
            for(int j=0;j<n;j++){
                init_board[i][j] = String.valueOf(row.charAt(j));
            }//j
        }//i

        return init_board;
    }

    public static void main(String[] args){
        int m = 4;
        int n = 5;

        int i = 0;
        int j = 0;

        int count = 0;

        boolean changed = false;

        //String[] board={"TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"};
        String[] board={"CCBDE", "AAADE", "AAABF", "CCBBF"};
        String[][] current_board = init_board(m,n,board);
        String[] changed_board = new String[n];


        do{
            changed = false;
            String[][] deleting_board = new String[m][n];

            /**
             * This loop checks if there are any blocks to delete.
             */
            for(i=1;i<m;i++){
                for(j=1;j<n;j++){
                    if(!current_board[i][j].equals("") && current_board[i-1][j-1].equals(current_board[i-1][j]) && current_board[i-1][j].equals(current_board[i][j-1]) && current_board[i][j-1].equals(current_board[i][j])){
                        deleting_board[i][j] = current_board[i][j];
                        changed = true;
                    }//if
                    else{
                        deleting_board[i][j] = "";
                    }//else
                }//j
            }//i

            /**
             * This loop deletes the 2*2 blocks.
             */
            for(i=1;i<m;i++){
                for(j=1;j<n;j++) {
                    if(deleting_board[i][j] != ""){
                        current_board[i-1][j-1] = "";
                        current_board[i][j-1] = "";
                        current_board[i-1][j] = "";
                        current_board[i][j] = "";
                    }//if
                }//j
            }//i

            /**
             * This loop cleans up the current board.
             */
            for(j=0;j<n;j++){
                String temp = "";
                for(i=0;i<m;i++){
                    temp = temp + current_board[i][j];
                    current_board[i][j]="";
                }//i
                changed_board[j] = temp;
            }//j

            for(j=0;j<n;j++){
                String temp = changed_board[j];
                int rows = m-1;
                for(i=temp.length()-1;i>=0;i--){
                  current_board[rows][j] = String.valueOf(temp.charAt(i));
                  rows--;
                }//i
            }//j
        }while (changed);

        String temp_origin = "";
        String temp_changed = "";

        for(i=0;i<m;i++){
            temp_origin = board[i] + temp_origin;
        }
        for(j=0;j<n;j++){
            temp_changed = changed_board[j] + temp_changed;
        }

        count = temp_origin.length() - temp_changed.length();
        System.out.println(count);

    }


}
