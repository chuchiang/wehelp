**3-1**
* 使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。

```
INSERT INTO member(name,username,password,follower_count)VALUES('kitty','test','test',10);
INSERT INTO member(name,username,password,follower_count)VALUES('cindy','service1','service1',5);
INSERT INTO member(name,username,password,follower_count)VALUES('betty','service2','service2',8);
INSERT INTO member(name,username,password,follower_count)VALUES('tommy','service3','service3',2);
INSERT INTO member(name,username,password,follower_count)VALUES('kevin','service4','service4',7);
```
![](https://hackmd.io/_uploads/BypmiUts2.png)

**3-2**
*使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。
```
SELECT*FROM member;
```
![](https://hackmd.io/_uploads/Hyo5iUYj2.png)

**3-3**
* 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
```
SELECT*FROM member ORDER BY time DESC;
```
![](https://hackmd.io/_uploads/SkcRj8Yi3.png)

**3-4**
* 使⽤ SELECT 指令取得 member 資料表中第 2 到第 4 筆共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )
```
SELECT *FROM member order by time DESC LIMIT 3 OFFSET 1;
```
![](https://hackmd.io/_uploads/Hy9bnIYi2.png)

**3-5**
* 使⽤ SELECT 指令取得欄位 username 是 test 的會員資料
```
SELECT*FROM member WHERE username='test';
```
![](https://hackmd.io/_uploads/rJq4hIKo2.png)

**3-6**
* 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
```
SELECT*FROM member WHERE username='test'and password='test';
```
![](https://hackmd.io/_uploads/ryfInLYoh.png)

**3-7**
* 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2
```
UPDATE member SET name='test2' WHERE username='test';
```
![](https://hackmd.io/_uploads/SkJO3Lto2.png)

**4-1**
* 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )
```
SELECT COUNT(name) FROM member;
```
![](https://hackmd.io/_uploads/ByIp3LFs3.png)

**4-2**
* 取得 member 資料表中，所有會員 follower_count 欄位的總和
```
SELECT SUM(follower_count) FROM member;
```
![](https://hackmd.io/_uploads/SkOXTIYih.png)

**4-3**
*  取得 member 資料表中，所有會員 follower_count 欄位的平均數
```
SELECT AVG(follower_count) FROM member;
```
![](https://hackmd.io/_uploads/HyrUa8tj3.png)

**5-1**
* 在資料庫中，建立新資料表紀錄留⾔資訊，取名字為 message。資料表中必須包含以下欄位設定
```
CREATE TABLE  message(
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    member_id  BIGINT NOT NULL,
    content  VARCHAR(255) NOT NULL,
    like_count VARCHAR(255) NOT NULL DEFAULT 0,
    time DATETIME DEFAULT NOW(),
    FOREIGN KEY(member_id)REFERENCES member(id)
);
INSERT INTO message(member_id,content,like_count) VALUES(1,'HELLO',10);
INSERT INTO message(member_id,content,like_count) VALUES(1,'HI',2);
INSERT INTO message(member_id,content,like_count) VALUES(2,'HELLO cindy',25);
INSERT INTO message(member_id,content,like_count) VALUES(3,'HELLO betty',13);
INSERT INTO message(member_id,content,like_count) VALUES(4,'HELLO tommy',15);
INSERT INTO message(member_id,content,like_count) VALUES(5,'HELLO kevin',3);
```
![](https://hackmd.io/_uploads/SJacpLKsh.png)

**5-2**
* 使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者的姓名
```
SELECT message.content,member.name FROM member INNER JOIN message on member.id=message.member_id;
```
![](https://hackmd.io/_uploads/SkJppIKsn.png)

**5-3**
* 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者的姓名
```
SELECT message.content,member.name FROM member INNER JOIN message on member.id=message.member_id WHERE username='test';

```
![](https://hackmd.io/_uploads/H1MWRLKi3.png)

**5-4**
* 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數
```
SELECT AVG(message.like_count) FROM member INNER JOIN message on member.id=message.member_id WHERE username='test';
```
![](https://hackmd.io/_uploads/rk_X08Fj2.png)

















