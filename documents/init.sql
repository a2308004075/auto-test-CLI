#docker exec -it mysql bash
#mysql -u root -pCaes@2022 -h127.0.0.1
#use caes_autotest;

# shell获取系统当前时间
INSERT INTO test_shell (id,shell) VALUES (1,'date +"%Y-%m-%d %H:%M:%S"');

# shell获取指定时间段日志
INSERT INTO test_shell (id,shell) VALUES
(2,'
awk -F ''.'' -v start="${start_time}" -v end="${end_time}" ''
{
    # 将时间字符串转换为秒数
    log_time = $1
    log_time_seconds = mktime(gensub(/:/," ", "g", gensub(/-/," ", "g", $1)))
    start_seconds = mktime(gensub(/:/," ", "g", gensub(/-/," ", "g", start)))
    end_seconds = mktime(gensub(/:/," ", "g", gensub(/-/," ", "g", end)))

    # 检查时间是否在指定范围内
    if (log_time_seconds >= start_seconds && log_time_seconds <= end_seconds) {
        print $0
    }
}'' ${log_file}');

# sql查询超时时间
INSERT INTO test_sql (id,`sql`,type) VALUES (1,'select * from stat_swap_timeout_config where station_type=?',0);