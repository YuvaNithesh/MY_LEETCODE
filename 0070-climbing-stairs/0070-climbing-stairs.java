public class Solution {
    public int climbStairs(int n) {
        if (n==1) return 1;
        if (n==2) return 2;
        int[] a=new int[n + 1];
        a[1]=1;
        a[2]=2;
        a[3]=3;
        for (int i=4;i<=n;i++) {
            a[i]=a[i-1]+a[i-2];
        }
        return a[n];
    }
}
