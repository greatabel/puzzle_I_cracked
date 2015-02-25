package redblacktree;
import java.util.*;
import java.io.*;
import java.util.Random; 

public class countTime {
	public long time1,time2;
	public long getRBTreeTime()
	{return this.time1;
	
	}
	public long getBSTreeTime()
	{
		return this.time2;
	}
	
	public void countTime(){
	random myrandom=new random();
	myrandom.setRandom();
	countTime A=new countTime();
	
	 binarySearchTree randTree1=new binarySearchTree();
	   for(int j = 0; j < 300000; j++){
	       randTree1.rbInsert(random.theR[j]);
	   }
	   long  begin1=System.nanoTime();
	   Node node1 = randTree1.search(15000);
	long       end1=System.nanoTime();
	 time1 =end1 -begin1;
	System.out.println("\n二叉排序树花费的时间time="+time1+"纳秒");

	
	
	redblacktree randTree2 = new redblacktree();	
    for(int i = 0; i < 300000; i++){
        randTree2.rbInsert(random.theR[i]);
                                   }
long  begin=System.nanoTime();
        Node node = randTree2.search(15000);
   long       end=System.nanoTime();
    time2 =end -begin;
   System.out.println("红黑树花费的时间time="+time2+"纳秒");
   
	   }
	}

	   
