
"""
数据库导出csv文件
"""
import pymysql
import csv
import codecs


class CsvExport(object):

    def connect(self,**kwargs):
        """
        连接数据库
        :param kwargs:
        :return:
        """
        db = pymysql.connect(host=kwargs.get("host"), port=kwargs.get("port"),
                             user=kwargs.get("user"), password=kwargs.get("password"),
                             db=kwargs.get("db"), charset=kwargs.get("charset"))
        return db

    def export(self,filePath,colums,sql):
        """
         导出数据到csv
        :param filePath 导出路径
        :return:
        """
        with codecs.open(filename=filePath, mode='w', encoding='utf-8') as f:
            write = csv.writer(f, dialect='excel')
            write.writerow(colums)
            db = self.connect(host="117.136.179.52", port=3306, db="course-study",
                              password="dreamtech%IT", user="root", charset="utf8")
            cursor = db.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            for res in results:
                write.writerow(res)
            print('导出成功')


if __name__ == '__main__':

    csvexport = CsvExport()
    columns = ['ID', '用户ID', '课程ID', '课程节ID', '客户端类型', '单次学习时长(单位秒)', '创建时间','提交时间']
    sql = "select f_id, f_member_id, f_course_id, f_section_id, f_client_type, f_study_time, FROM_UNIXTIME(FLOOR(f_create_time/1000),'%Y-%m-%d %h:%i:%s'), FROM_UNIXTIME(FLOOR(f_commit_time/1000),'%Y-%m-%d %h:%i:%s') from t_course_section_study_log"
    csvexport.export('c:/tools/a.csv',columns,sql)


