from odps.udf import annotate


@annotate("bigint,bigint->bigint")
class Demo06_UDF(object):

    def evaluate(self, arg0, arg1):
        return


