package redblacktree;

import java.io.*;
/*-------Node��ʵ�ֵ���Ҫ�Ƕ���ڵ�����Ժ���ز������Ա������������--------*/
public class Node{
	 int NData;                 //����ڵ�����ֵ
	 Node parent;              //�ڵ�ĸ�ĸ�ڵ�
	 Node leftChild;           //�ڵ�����ӽڵ�
	 Node rightChild;          //�ڵ���Һ��ӽڵ�
	 boolean color;            //�ڵ����ɫ

	 
 //���ýڵ����ֵ
  public void setNode(int i){
	  this.NData=i;
  }
 //����ڵ������Ϣ
  public void displayNode(){
	  System.out.println("Data:"+this.NData+";color:"+this.color);
  }
 //ȡ�ýڵ������ֵ
  public int getValue(){
	  return this.NData;
  }
  //ȡ�ýڵ����ɫ
  public String getColor(){
	  if(this.color==true) return "B";
	  else return "R";
  }
  
  
}












