class Solution {
    double result = 1.0;
    public double myPow(double x, int n) {
        
        if(x == 1 || n == 0){
            return result;
        }
        
       	long counter = n > 0 ? n : (long) n * -1;
        
        if (counter > 0) {
				result = calculate(x, counter);
		}
        if (n < 0){
            return 1 / result;
        }
        return result;
    }
    
    public double calculate(double x, long n) {
        if (n == 1) {
            return x;
        }
        if (n%2 == 0) {
            double result = calculate(x, n/2);
            return result * result ;
        } 
        else {
            double result = calculate(x, n/2);
            return result * result * x ;
        }
    }
}