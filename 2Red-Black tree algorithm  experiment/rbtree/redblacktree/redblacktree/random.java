package redblacktree;
import java.util.Random; 


/*-------------------------���δ���ʵ��������������ظ���1-300000����(������һ������ģ�-----------*/
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
	//	System.out.print("��������Ƿ�����������˲��ظ���1-300000������������ԣ�1+����+30w=4.500015E10��\n");
		
   //		System.out.print("�������sum="+sum);
		
		
		
	} //end of setRandom
}//end of random