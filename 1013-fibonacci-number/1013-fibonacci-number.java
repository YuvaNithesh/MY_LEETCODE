// //class Solution {
//   //  public int fib(int n) {
//     //    if(n==0||n==1){
//       //      return n;
//         //}
//         //else{
//         //return n-1;
//         //}
//    // }
// //}
// class Solution {
//     public int fib(int n) {
//         if (n <= 1) return n;
//         int a = 0, b = 1;
//         for (int i = 2; i <= n; i++) {
//             int temp = a + b;
//             a = b;
//             b = temp;
//         }
//         return b;
//     }
// }
class Solution {
    int[] memo = new int[31];
    public int fib(int n) {
        if (n <= 1) return n;
        if(memo[n] > 0) return memo[n];
        memo[n] = fib(n - 1) + fib(n - 2);

        return memo[n];
   }
}

