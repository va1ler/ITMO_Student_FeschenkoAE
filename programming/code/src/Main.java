/*public class Main {

    public static void main(String[] args) {
        long[] l = new long[7];
        for (int i = 0; i < l.length; i++) {
            l[i] = 16 - 2 * i;
        }

        double[] x = new double[19];
        for (int i = 0; i < x.length; i++) {
            x[i] = Math.random() * 15.0 - 2.0;
        }

        double[][] n = new double[7][19];
        for (int i = 0; i < n.length; i++) {
            for (int j = 0; j < n[i].length; j++) {
                n[i][j] = calculateElement(l[i], x[j]);
            }
        }

        printMatrix(n);
    }

    public static double calculateElement(long li, double x) {
        if (li == 10) {
            return Math.pow(Math.pow(Math.pow(x, 3) / (Math.cos(x) - 1), 2) / 3 / 4, Math.asin(Math.sin(x)));
        } else if (li == 8 || li == 12 || li == 16) {
            return Math.cbrt(Math.exp(Math.exp(x)));
        } else {
            return Math.cbrt(Math.cos(Math.pow((x - 3.0 / 4) / 2 / 3, 2)));
        }
    }

    public static void printMatrix(double[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.printf("%12.3f ", matrix[i][j]);
            }
            System.out.println();
        }
    }
}*/



public class Main{
    public static void main(String[] args){
        System.out.print(fun( 10,12,10));
    }
    public static double fun(int a, int b, int c){
        return (double) a+b+c+99;
    }
    public static double fun(double a, double b, double c){
        return (double) a+b+c-10000;
    }
    public static double fun(long a, long b, long c){
        return (double) a+b+c+100000000;
    }
}