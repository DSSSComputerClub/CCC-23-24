/*
* Author: Deon Jerom
* Date: Sept. 2023
* Solution to 2015 J3 Rövarspråket
* Problem Type -> Implementation
*/

import java.io.*;
import java.util.*;

public class Main

	/*
	 * Ascii Code 
	 * - 97, 101, 105, 111, 117
	 */
{
	public static void main(String[] args) throws NumberFormatException, IOException {
	    
		BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
		
		String consonant = "";
		
		String word = rd.readLine();
		
		ArrayList<Integer> list = new ArrayList<>();
		
		int[] slot = {97,101,105,111,117};

		for(int i=0;i<word.length();i++) {
			
			
			int as = (int) word.charAt(i);
			
			if(as == 97 || as == 101 || as ==  105 || as ==  111 || as ==  117) {
				
				consonant += word.charAt(i);
				
			}else {
				
				consonant += word.charAt(i);
				
				for(int x =0;x<slot.length;x++) {
					
					if(as > slot[x]) {
						list.add((as - slot[x]));
					}else {
						list.add((slot[x] - as));
					}
				}
				
				int a = Collections.min(list);
				
				consonant += (char) slot[list.indexOf(a)];

				if((as) == 122){
					consonant +=  (char) (as);
				}else {
					if((as + 1) == 97 || (as + 1) == 101 || (as + 1) ==  105 || (as + 1) ==  111 || (as + 1) ==  117) {
						consonant +=  (char) (as + 2);
					}else {
						consonant +=  (char) (as + 1);
					
					}
				}
				
				
				list.removeAll(list);
				
			}
			
				
		}
		
		System.out.println(consonant);
		

	}
}
