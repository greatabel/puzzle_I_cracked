package redblacktree;
import java.util.Random; 


/*-------------------------本段代码实现了随机生成无重复的1-300000的数(星期天一下午调的）-----------*/
public class random{
	static int[] theR ;
	void setRandom(){
		int j=0;
		double k;
		theR=new int[300000];
		Random rand=new Random();
		
		for(int i=1;i<=300000;i++)
		{
			//if(i==300000) System.out.print("i="+i);
		do{
			k=rand.nextDouble();
			j=(int)(k*10000000%300000);
			
		  }
		while(theR[j]!=0);
		if( theR[j]==0) theR[j]=i;
		}//end of for
		double sum=0;
		for(int l=0;l<300000;l++)
			sum+=theR[l];
	//	System.out.print("下面测试是否是随机生成了不重复的1-300000，以求和来测试（1+……+30w=4.500015E10）\n");
		
   //		System.out.print("程序算出sum="+sum);
		
		
		
	} //end of setRandom
}//end of random