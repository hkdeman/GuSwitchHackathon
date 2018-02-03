import java.util.*;
class Fibonacci {
	public static void main(String[] args) {
		ArrayList<Integer> f = new ArrayList<>();
		f.add(1);
		f.add(1);
		System.out.println(f.get(0));
		System.out.println(f.get(1));
		for(int i=2;i<100;i++) {
			f.add(f.get(i-1)+f.get(i-2));
			System.out.println(f.get(i));
			
		}	
	}
}
