/*
*  Author: Deon
*  Date: Sept. 2023
*  Solution to 2018 S2 Sunflowers
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));
		
		int size = Integer.parseInt(scan.readLine());
		
		int[][] table = new int[size][size];
		
		for(int x = 0;x<table.length;x++) {
			String[] temp = scan.readLine().split(" ");
			for(int y = 0;y<table[x].length;y++) {
				table[x][y] = Integer.parseInt(temp[y]);
			}
		}

		while(table[0][0] > table[1][0] || table[0][0] > table[0][1]) {
			rotate(table);
		}
		
		for(int x = 0;x<table.length;x++) {
			for(int y = 0;y<table[x].length;y++) {
				System.out.print(table[x][y]+ " ");
			}
			System.out.println();
		}
		
	}
	public static void rotate(int[][] array ) {
		
		//first all of 90 degree clockwise
		//store the data inside a different array
		int[][] temp = new int[array.length][array[0].length];
		
		for(int i =0;i<array.length;i++) {
			for(int x = 0, x1 = array.length - 1;x<array.length;x++, x1--) {
				temp[i][x] =  array[x1][i];
			}
		}
		
		for(int i=0;i<array.length;i++) {
			for(int x = 0;x<array[i].length;x++) {
				array[i][x] = temp[i][x]; 
			}
		}
		
	}

}
