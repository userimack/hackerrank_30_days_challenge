import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


class Difference {
    private int[] elements;
    public int maximumDifference;

    // Add your code here
    Difference(int[] arr){
        elements = arr;
    }
    void computeDifference(){
        //maximumDifference=elements[0];
        for(int i=0;i<elements.length;i++){
            for(int j=i+1;j<elements.length;j++){
                int diff=Math.abs(elements[i]-elements[j]);
                //maximumDifference = (diff > maximumDifference?diff:maximumDifference)
                if(diff > maximumDifference)
                    maximumDifference = diff;
            }
        }
    }

} // End of Difference class

public class Solution {

            public static void main(String[] args) {
                Scanner sc = new Scanner(System.in);
                int N = sc.nextInt();
                int[] a = new int[N];
                for (int i = 0; i < N; i++) {
                    a[i] = sc.nextInt();
                }

                Difference D = new Difference(a);

                D.computeDifference();

                System.out.print(D.maximumDifference);
            }
        }