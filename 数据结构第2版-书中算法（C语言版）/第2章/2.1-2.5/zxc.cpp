#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
using namespace std;
#define OK 1
#define ERROR 0
#define OVERFLOW -2
typedef int Status;   // Status 是函数返回值类型，其值是函数结果状态代码。
typedef int ElemType; // ElemType 为可定义的数据类型，此设为int类型

#define MAXSIZE 100 // 顺序表可能达到的最大长度
struct Book
{
    string id;    // ISBN
    string name;  // 书名
    double price; // 定价
};
typedef struct
{
    Book *elem; // 存储空间的基地址
    int length; // 当前长度
} SqList;

Status InitList_Sq(SqList &L)
{ // 算法2.1 顺序表的初始化
    // 构造一个空的顺序表L
    cout << "初始化顺序表" << endl;
    cout << &L << endl;
    cout << L.elem << endl;
    cout << L.length << endl;
    L.elem = new Book[MAXSIZE]; // 为顺序表分配一个大小为MAXSIZE的数组空间
    if (!L.elem)
        exit(OVERFLOW); // 存储分配失败退出
    L.length = 0;       // 空表长度为0
    return OK;
}

int main(int argc, char const *argv[])
{
    SqList L;
    InitList_Sq(L);
    return 0;
}
