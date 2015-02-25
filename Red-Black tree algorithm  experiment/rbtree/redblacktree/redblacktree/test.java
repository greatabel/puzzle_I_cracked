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
		
		System.out.println("--------------------����һ------------------");
		System.out.println("����������");
		rbtree.preOrder();
		System.out.println("�����������");
		bstree.preOrder();
		System.out.println("������ĺڸ߶�:"+rbtree.bDepth() );
		System.out.println("-------------------�����------------------");
		rbtree.rbDelete(15);
		System.out.println("����ɾ������ֵ15�ڵ��ĺ����Ϊ��");
		rbtree.preOrder();
		System.out.println("������ĺڸ߶�:"+rbtree.bDepth() );
		//System.out.println("test entrance .");
		System.out.println("-------------------������------------------");
		
		countTime counta=new countTime();
		
       counta.countTime();
        System.out.println("-------------------������------------------");
        long[] RTime,BSTime;
         RTime=new long[6];
         BSTime=new long[6];
        long sum1=0;
        long sum2=0;
        for(int l=0;l<NUM;l++)
        { countTime countb=new countTime();
          countb.countTime();
          RTime[l]=countb.getRBTreeTime();
          System.out.println(" ��"+l+"��:="+RTime[l]+"����");
          BSTime[l]=countb.getBSTreeTime();
          System.out.println(" ��"+l+"��:="+BSTime[l]+"����");
          sum1+=RTime[l];
          sum2+=BSTime[l];
          
        }
       System.out.println("�����"+NUM+"��ƽ����������ʱ��:="+sum1/NUM+"����");
       System.out.println("���������"+NUM+"��ƽ������ʱ��:="+sum2/NUM+"����");
       
       System.out.println("--------------------������---------------");
       
       redblacktree rbtreelast=new redblacktree();
		
		int[] b={1,2,3,4,5,6,7,8};
		for(int i=0;i<b.length;i++){
			rbtreelast.rbInsert(b[i]);
		}
		System.out.print("the rank of 6 is:"+rbtreelast.OSRank(6));
		
	}
}