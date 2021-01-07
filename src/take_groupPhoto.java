import java.util.*;

public class take_groupPhoto {
    static HashSet<String> lineset;

    /**
     * This method creates the whole sequences of friends
     * friends: the list of friends
     * line: the current sequence of friends
     * used: the list of whether the friend is in the line
     * */
    public static void DFS(String[] friends, String line, boolean[] used){
        if(line.length()==8){
            lineset.add(line);
            return;
        }

        else{
            for(int i=0;i<8;i++){
                if(used[i] == true) continue;
                else{
                    line = line + friends[i];
                    used[i] = true;
                    DFS(friends, line, used);
                    used[i] = false;
                    line = line.substring(0,line.length()-1);
                }//else
            }//for
        }//else
        return;
    }//DFS

    /**
     * This method creates the sequences which follow the rules
     * friends: the list of friends
     * line: the current sequence of friends
     * used: the list of whether the friend is in the line
     * data: the list of sequence rules which should be followed
     * */
    public static void DFS2(String[] friends, String line, boolean[] used, String[] data){
        if(line.length()==8){
            if(check_condition_v2(line, data)) lineset.add(line);
            return;
        }

        else{
            for(int i=0;i<8;i++){
                if(used[i] == true) continue;
                else{
                    line = line + friends[i];
                    used[i] = true;
                    DFS2(friends, line, used, data);
                    used[i] = false;
                    line = line.substring(0,line.length()-1);
                }//else
            }//for
        }//else
        return;
    }//DFS

    /**
     * This method checks whether the sequence follows the rules
     * data: the list of sequence rules which should be followed
     * Return value: the number of sequences which follows the rules
     */
    public static int check_condition(String[] data){

        HashSet<String> excluded_lineset = new HashSet<>();

        for(String condition:data){
           char friend1 = condition.charAt(0);
           char friend2 = condition.charAt(2);
           char comparator = condition.charAt(3);
           int distance = Integer.parseInt(String.valueOf(condition.charAt(4)));

           for(String line: lineset){
               int pos1 = line.indexOf(friend1);
               int pos2 = line.indexOf(friend2);

               if(!excluded_lineset.contains(line)){
                   if(comparator=='>'){
                       if(Math.abs(pos1-pos2)-1 <= distance){

                           excluded_lineset.add(line);
                           continue;
                       }
                   }//>
                   else if(comparator=='<'){
                       if(Math.abs(pos1-pos2)-1 >= distance){

                           excluded_lineset.add(line);
                           continue;
                       }
                   }//<
                   else{
                       if(Math.abs(pos1-pos2)-1 != distance){

                           excluded_lineset.add(line);
                           continue;
                       }
                   }//=
               }//excluded_lineset.contains(line)
           }//for(String line: lineset)
        }//for(String condition:data)
        return excluded_lineset.size();
    }

    /**
     * This method checks whether the sequence follows the rules
     * data: the list of sequence rules which should be followed
     * Return value: whether the sequence follows the rules(boolean)
     */
    public static boolean check_condition_v2(String line,String[] data){
        for(String condition:data){
            char friend1 = condition.charAt(0);
            char friend2 = condition.charAt(2);
            char comparator = condition.charAt(3);
            int distance = Integer.parseInt(String.valueOf(condition.charAt(4)));

            int pos1 = line.indexOf(friend1);
            int pos2 = line.indexOf(friend2);

            if(comparator=='>'){
                if(Math.abs(pos1-pos2)-1 <= distance){
                    return false;
                }
            }//>
            else if(comparator=='<'){
                if(Math.abs(pos1-pos2)-1 >= distance){
                    return false;
                }
            }//<
            else{
                if(Math.abs(pos1-pos2)-1 != distance){
                    return false;
                }
            }//=
        }//for(String condition:data)
        return true;
    }


    public static void main(String[] args){
        lineset = new HashSet<String>();
        String[] friends = {"A","C","F","J","M","N","R","T"};
        String line = "";
        boolean[] used = new boolean[8];
        Arrays.fill(used,false);
        String[] data = {"N~F=0", "R~T>2"};

        //DFS(friends, line, used);
        DFS2(friends, line, used, data);

        int answer = 0;

        //answer = lineset.size() - check_condition(data);
        answer = lineset.size();

        System.out.println(answer);

    }
}
