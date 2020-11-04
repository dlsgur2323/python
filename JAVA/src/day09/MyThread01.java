package day09;

public class MyThread01 {
	public static void main(String[] args) {
		for(int i = 0 ; i< 100000;i++) {
			System.out.print(i+"\t");
			if((i+1)%100 == 0) {
				System.out.println();
			}
		}
		
		for(int i = 0 ; i< 100000;i++) {
			System.out.print((char)i+"\t");
			if((i+1)%100 == 0) {
				System.out.println();
			}
		}
	}
	
	
}
