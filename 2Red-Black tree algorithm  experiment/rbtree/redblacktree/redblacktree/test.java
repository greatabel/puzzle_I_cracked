package redblacktree;
import java.util.*;
import java.io.*;
public class test{
	private static final int NUM=6;
	public static void main(String args[]){
		redblacktree rbtree=new redblacktree();
		binarySearchTree bstree=new binarySearchTree();
		
		int[] a={8,11,17,15,6,1,22,25,27};
		for(int i=0;i<a.length;i++){
			rbtree.rbInsert(a[i]);
			bstree.BSTInsert(a[i]);
			
		}
		
		System.out.println("--------------------步骤一------------------");
		System.out.println("红黑树输出：");
		rbtree.preOrder();
		System.out.println("二叉树输出：");
		bstree.preOrder();
		System.out.println("红黑树的黑高度:"+rbtree.bDepth() );
		System.out.println("-------------------步骤二------------------");
		rbtree.rbDelete(15);
		System.out.println("我们删除属性值15节点后的红黑树为：");
		rbtree.preOrder();
		System.out.println("红黑树的黑高度:"+rbtree.bDepth() );
		//System.out.println("test entrance .");
		System.out.println("-------------------步骤三------------------");
		
		countTime counta=new countTime();
		
       counta.countTime();
        System.out.println("-------------------步骤四------------------");
        long[] RTime,BSTime;
         RTime=new long[6];
         BSTime=new long[6];
        long sum1=0;
        long sum2=0;
        for(int l=0;l<NUM;l++)
        { countTime countb=new countTime();
          countb.countTime();
          RTime[l]=countb.getRBTreeTime();
          System.out.println(" 第"+l+"次:="+RTime[l]+"纳秒");
          BSTime[l]=countb.getBSTreeTime();
          System.out.println(" 第"+l+"次:="+BSTime[l]+"纳秒");
          sum1+=RTime[l];
          sum2+=BSTime[l];
          
        }
       System.out.println("红黑树"+NUM+"次平均查找所需时间:="+sum1/NUM+"纳秒");
       System.out.println("二叉查找树"+NUM+"次平均所需时间:="+sum2/NUM+"纳秒");
       
       System.out.println("--------------------步骤五---------------");
       
       redblacktree rbtreelast=new redblacktree();
		
		int[] b={1,2,3,4,5,6,7,8};
		for(int i=0;i<b.length;i++){
			rbtreelast.rbInsert(b[i]);
		}
		System.out.print("the rank of 6 is:"+rbtreelast.OSRank(6));
		
	}
}