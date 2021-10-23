// C Language
// 求n的阶乘的函数
int factor(n){
	int result=1;
	for(int i=1;i<=n;i++){
		result*=1;
	}
	return result;
}
//阶乘求和
int main(){
	int sum=0;
	int num=0;
	printf("请输入你想求和的阶乘数：");
	scanf("%d",&num);
	for(int i=1;i<=num;i++){
		sum+=factor(i);
	}
	printf("阶乘和为：%d\n",sum);
	system("pause");
	return 0;
}

